'''
Simple tagger service that uses CoreNLP Sever 
to produce a tag file for brat.

See README.md for instructions.

'''

from flask import Flask
from flask import request
import requests
import json
app = Flask(__name__)

CORENLP_HOST = "http://skynet001:9000"
API_HOST = "0.0.0.0"
API_PORT = 47111
 
@app.route('/', methods = ['GET', 'POST'])
def home():
    #Fetch
    result = {}
    if request.method == "POST":
        indata = request.data
        r = requests.post(CORENLP_HOST + '/?properties={"annotators": "tokenize,ssplit,pos", "outputFormat": "json"}', data=indata)         
        data = json.loads(r.content)
        print(data)
        counter = 0
        for s in data['sentences']:
             for t in s['tokens']:                
                #e_id = str(t["index"])
                e_id = str(counter)
                e_type = t["pos"]
                e_offset_start = t["characterOffsetBegin"]
                e_offset_end = t["characterOffsetEnd"]
                e_text = t["word"]
                next_entry = {}
                next_entry["type"] = e_type
                next_entry["offsets"] = [[e_offset_start, e_offset_end]]
                next_entry["texts"] = [e_text]
                result[e_id] = next_entry
                counter=counter+1
        return result
    else:
        return '<h3>This is the CoreNLP-brat API<br><br> POST some words bro!</h3>'

if __name__ == '__main__':
    app.run(debug=True, host=API_HOST, port=API_PORT)