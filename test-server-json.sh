wget --post-data 'the quick brown fox jumped over the lazy dog' 'localhost:9000/?properties={"annotators": "tokenize,ssplit,pos", "outputFormat": "json"}' -O - | jq

