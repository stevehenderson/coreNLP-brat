# CoreNLP-to-brat API


## Overview

This webservice recieves a text blob to tokenize for parts of speech, send this to a CoreNLP server, and then returns the result in a brat compatible format

For example, this sentenance:


```
"mary had a little lamb and john was happy. George likes Angel.  Dan hit Sam hard"
```

When sent to CorenLP yields:

```
{
  "sentences": [
    {
      "index": 0,
      "tokens": [
        {
          "index": 1,
          "word": "mary",
          "originalText": "mary",
          "characterOffsetBegin": 0,
          "characterOffsetEnd": 4,
          "pos": "NN",
          "before": "",
          "after": " "
        },
        {
          "index": 2,
          "word": "had",
          "originalText": "had",
          "characterOffsetBegin": 5,
          "characterOffsetEnd": 8,
          "pos": "VBD",
          "before": " ",
          "after": " "
        },
        {
          "index": 3,
          "word": "a",
          "originalText": "a",
          "characterOffsetBegin": 9,
          "characterOffsetEnd": 10,
          "pos": "DT",
          "before": " ",
          "after": " "
        },
        {
          "index": 4,
          "word": "little",
          "originalText": "little",
          "characterOffsetBegin": 11,
          "characterOffsetEnd": 17,
          "pos": "JJ",
          "before": " ",
          "after": " "
        },
        {
          "index": 5,
          "word": "lamb",
          "originalText": "lamb",
          "characterOffsetBegin": 18,
          "characterOffsetEnd": 22,
          "pos": "NN",
          "before": " ",
          "after": " "
        },
        {
          "index": 6,
          "word": "and",
          "originalText": "and",
          "characterOffsetBegin": 23,
          "characterOffsetEnd": 26,
          "pos": "CC",
          "before": " ",
          "after": " "
        },
        {
          "index": 7,
          "word": "john",
          "originalText": "john",
          "characterOffsetBegin": 27,
          "characterOffsetEnd": 31,
          "pos": "NN",
          "before": " ",
          "after": " "
        },
        {
          "index": 8,
          "word": "was",
          "originalText": "was",
          "characterOffsetBegin": 32,
          "characterOffsetEnd": 35,
          "pos": "VBD",
          "before": " ",
          "after": " "
        },
        {
          "index": 9,
          "word": "happy",
          "originalText": "happy",
          "characterOffsetBegin": 36,
          "characterOffsetEnd": 41,
          "pos": "JJ",
          "before": " ",
          "after": ""
        },
        {
          "index": 10,
          "word": ".",
          "originalText": ".",
          "characterOffsetBegin": 41,
          "characterOffsetEnd": 42,
          "pos": ".",
          "before": "",
          "after": " "
        }
      ]
    },
    {
      "index": 1,
      "tokens": [
        {
          "index": 1,
          "word": "George",
          "originalText": "George",
          "characterOffsetBegin": 43,
          "characterOffsetEnd": 49,
          "pos": "NNP",
          "before": " ",
          "after": " "
        },
        {
          "index": 2,
          "word": "likes",
          "originalText": "likes",
          "characterOffsetBegin": 50,
          "characterOffsetEnd": 55,
          "pos": "VBZ",
          "before": " ",
          "after": " "
        },
        {
          "index": 3,
          "word": "Angel",
          "originalText": "Angel",
          "characterOffsetBegin": 56,
          "characterOffsetEnd": 61,
          "pos": "NNP",
          "before": " ",
          "after": ""
        },
        {
          "index": 4,
          "word": ".",
          "originalText": ".",
          "characterOffsetBegin": 61,
          "characterOffsetEnd": 62,
          "pos": ".",
          "before": "",
          "after": "  "
        }
      ]
    },
    {
      "index": 2,
      "tokens": [
        {
          "index": 1,
          "word": "Dan",
          "originalText": "Dan",
          "characterOffsetBegin": 64,
          "characterOffsetEnd": 67,
          "pos": "NNP",
          "before": "  ",
          "after": " "
        },
        {
          "index": 2,
          "word": "hit",
          "originalText": "hit",
          "characterOffsetBegin": 68,
          "characterOffsetEnd": 71,
          "pos": "VBD",
          "before": " ",
          "after": " "
        },
        {
          "index": 3,
          "word": "Sam",
          "originalText": "Sam",
          "characterOffsetBegin": 72,
          "characterOffsetEnd": 77,
          "pos": "NNP",
          "before": " ",
          "after": " "
        },
        {
          "index": 4,
          "word": "hard",
          "originalText": "hard",
          "characterOffsetBegin": 78,
          "characterOffsetEnd": 82,
          "pos": "RB",
          "before": " ",
          "after": ""
        }
      ]
    }
  ]
}
```

After translation for brat, it should yield:

```
{   "0": {"type": "NNP", "offsets": [[0, 4]], "texts": ["mary"]}, 
    "1": {"type": "VBD", "offsets": [[5, 8]], "texts": ["had"]}, 
    "2": {"type": "DT", "offsets": [[9, 10]], "texts": ["a"]}, 
    "3": {"type": "JJ", "offsets": [[11, 17]], "texts": ["little"]}, 
    "4": {"type": "NN", "offsets": [[18, 22]], "texts": ["lamb"]}, 
    "5": {"type": "CC", "offsets": [[23, 26]], "texts": ["and"]}, 
    "6": {"type": "NNP", "offsets": [[27, 31]], "texts": ["john"]}, 
    "7": {"type": "VBD", "offsets": [[32, 35]], "texts": ["was"]}, 
    "8": {"type": "JJ", "offsets": [[36, 41]], "texts": ["happy"]}, 
    "9": {"type": ".", "offsets": [[41, 42]], "texts": ["."]}, 
    "10": {"type": "NNP", "offsets": [[43, 49]], "texts": ["George"]}, 
    "11": {"type": "VBZ", "offsets": [[50, 55]], "texts": ["likes"]}, 
    "12": {"type": "NNP", "offsets": [[56, 61]], "texts": ["Angel"]}, 
    "13": {"type": ".", "offsets": [[61, 62]], "texts": ["."]}, 
    "14": {"type": "_SP", "offsets": [[63, 64]], "texts": [" "]}, 
    "15": {"type": "NNP", "offsets": [[64, 67]], "texts": ["Dan"]}, 
    "16": {"type": "VBD", "offsets": [[68, 71]], "texts": ["hit"]}, 
    "17": {"type": "NNP", "offsets": [[72, 77]], "texts": ["Sam"]}, 
    "18": {"type": "RB", "offsets": [[78, 82]], "texts": ["hard"]}}
```

## Usage

### Standalone

#### Install (one time)

Create and activate virtual environment.
Install the required libraires:

```
python3 -m venv ve-api
source bin/ve-api/activate
pip install -r requirements.txt
deactivate
```

#### Start stand-alone

```
source bin/ve-api/activate
python corenlp_brat_api.py
```

### Docker

Build

```
docker build . -t corenlp-brat-api
```

Run

```
./start
```

Stop

```
./stop
```

## Testing

Create a tools.cfg inside a brat collection.  Set the annotators URL to the URL of this webservice

```
[options]

[search]
Google          <URL>:http://www.google.com/search?q=%s
Wikipedia       <URL>:http://en.wikipedia.org/wiki/%s

[normalization]

[annotators]
SNER-CoNLL      tool:Stanford_NER, model:CoNLL, <URL>:http://skynet001:47111/

[disambiguators]
```
*Note: The strings "SNER-CoNLL" and "tool:Stanford_NER, model:CoNL" don't seem to matter other than to name buttons in the brat interface.*


Then, login to brat and load a collection and document.  Mouse over the top of the document window until you see the popup menu with `Collection`, `Data`, `Search`.  Click `data` and then click the CoNLL button.  This should generate q request to this web service.
