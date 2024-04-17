# [NLGlite](https://test.pypi.org/project/NLGLite/1.0.0/)
A Lightweight NLP Solution Authored by Daniel Hartgrove for Dissertation Project @ The University of Nottingham (COMP3003). Supervised by Dr I Knight.

## Abstract
This project was developed as a part of my dissertation for my Batchelor's degree at the University of Nottingham. You can read my dissertation, when published [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Dependencies
This project requires that you have Python 3 install. This can be installed [here](https://www.python.org/downloads/)
This project also requires that you have the [NLTK](https://www.nltk.org/install.html) installed, as well as [spacy](https://spacy.io/).

## How to Run
This project is ~~delightfully simple~~ easy to install and run:
- Simply download the files from this page
- Download NLTK by opening your preferred terminal and using the command `pip install nltk`
- Download spaCy by then running the command `pip install spacy`, followed by `python -m spacy downlaod en_core_web_sm`
- Then use your preferred terminal to navigate to the location of the project files
- Run the command `python3 NLGLite` to open the application

## How to use
#### Main UI:
- The Main UI is split into sections, at the top you can input the file path of the .lcfg (liteconfig) file that you want to run.
- Next, are the options for operating on this file:
  - **Clear:** Remove all content from the config
  - **Train:** Opens the training window
  - **Edit:** Manually edit the file to tweak the config. Opens in the default text editor for your OS.
- Below that is the "generate" button. This will generate text based on the .lcfg file. This will output to the output box.
- At the bottom of the screen are two buttons, one copies the contents of the output box to the clipboard and the other will clear the output box.

#### Clear Popup:
- If you click **"Yes"**, the data will be emptied.
- If you click **"No"**, the popup will close.

#### Training UI:
- The first two entry boxes are for the .lcfg output file (which if left blank will create a new training_data file) and the .txt file to train on.
  - The program will only work on .txt files in utf-8.
- Then you can toggle the tagging method used.
  - The available methods are POS and BLOB tagging. 
- You can then Train the model, and once the button pops back up training is complete.
- You can also cancel to back out of the training UI.

## Capabilities
Currently, this project is able to produce syntactically correct, but limited nonsense text. 
It does this using a Markov and Zipfian Driven Grammar, based on the work of Markov, Zipf, Chomsky, Kelmendi and Compton.
In the future, these sentences _should_ make sense all the time.

## References
Properly formatted references will be added shortly
