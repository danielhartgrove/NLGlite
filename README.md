# [NLGlite](https://test.pypi.org/project/NLGlite/)
A Lightweight NLP Solution Authored by Daniel Hartgrove for a Dissertation Project @ The University of Nottingham (COMP3003). Supervised by Dr I Knight.

## Abstract
This project was developed as a part of my dissertation for my Bachelor's degree at the University of Nottingham. You can read my dissertation when published [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Dependencies
This project requires that you have Python 3 installed. This can be installed [here](https://www.python.org/downloads/)
This project also requires that you have the [NLTK](https://www.nltk.org/install.html) installed, as well as [spacy](https://spacy.io/).

# NLGlite
A Lightweight NLP Solution authored by Daniel Hartgrove for a Dissertation Project at The University of Nottingham. Supervised by Dr I Knight.

## Abstract
This project was developed as a part of my dissertation for my Batchelor's degree at the University of Nottingham. You can read my dissertation when published [here](https://www.danielhartgrove.xyz/dissertation)

## Dependencies
This project requires that you have Python 3 installed. This can be installed [here](https://www.python.org/downloads/)
You must also have `nltk` and `textblob` installed also. This can be done by simply running the following commands:
- `pip install nltk`
- `pip install -U textblob`

## Instructions for Use
- Import the object using the command; `from NLGLite.NLGLite import NLGlite_ as nlglite`
- Create an instance of the object using the command; `nlg = nlglite()`
- Ask the object to create a `.lcfg` file by running the command; `nlg.make_new_config_file("path_to_file")`, alternatively run the command `nlg.set_config_file_path("path_to_file")`
- Train the object on a `.txt` file. You can do this by running the command; `nlg.train("path_to_text", "method")`
- You can then run the command; `nlg.generate_sentences(number of sentences, trace)` to generate random text.
  - If you want to see a trace of the output, you should pass `true` into this function. Otherwise, pass `false`
  - False is the default value for `trace`

- Various constants are returned on success and failure:
  ```
  NOT_ENOUGH_DATA = 15082003
  NO_FILE = 29122002
  BAD_OS = 18012007
  BAD_FILE = 14061978
  GOOD = 26061976
  ```
  
## Capabilities
Currently, this project can produce syntactically correct, but limited nonsense text. The project has only been
tested on training data of around 2000 KB in size.


## References
Properly formatted references will be added shortly
