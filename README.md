# [NLGlite](https://test.pypi.org/project/NLGlite/)
A Lightweight NLP Solution Authored by Daniel Hartgrove for a Dissertation Project @ The University of Nottingham (COMP3003). Supervised by Dr I Knight.

## Abstract
This project was developed as a part of my dissertation for my Bachelor's degree at the University of Nottingham. You can read my dissertation when published [here](https://www.danielhartgrove.xyz/danielhartgrove_dissertation.pdf)

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
Strubell, E., Ganesh, A., & McCallum, A. (2020). Energy and Policy Considerations for Modern Deep Learning Research. Proceedings of the AAAI Conference on Artificial Intelligence, 34(09), Article 09. https://doi.org/10.1609/aaai.v34i09.7123

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D., Wu, J., Winter, C., … Amodei, D. (2020). Language Models are Few-Shot Learners. Advances in Neural Information Processing Systems, 33, 1877–1901. 
https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html

OpenAI Platform. (n.d.). Retrieved December 7, 2023, from https://platform.openai.com

Menghani, G. (2023). Efficient Deep Learning: A Survey on Making Deep Learning Models Smaller, Faster, and Better. ACM Computing Surveys, 55(12), 259:1-259:37. https://doi.org/10.1145/3578938 

Chomsky, N. (1957). Syntactic Structures. Mouton and Co., The Hague.

OpenAI. (2023). GPT-4 Technical Report (arXiv:2303.08774). arXiv. http://arxiv.org/abs/2303.08774 

Compton, K., Kybartas, B., & Mateas, M. (2015). Tracery: An Author-Focused Generative Text Tool. In H. Schoenau-Fog, L. E. Bruni, S. Louchart, & S. Baceviciute (Eds.), Interactive Storytelling (pp. 154–161). Springer International Publishing. https://doi.org/10.1007/978-3-319-27036-4_14

A. Markov (1906). Extension of the law of large numbers to dependent quantities (in Russian). Izvestiia Fiz.-Matem. Obsch. Kazan Univ 15: 135–156.

A. M. Turing (1950). Computing Machinery and Intelligence. Mind, 49, 433-460.

Gardner, M., Grus, J., Neumann, M., Tafjord, O., Dasigi, P., Liu, N., Peters, M., Schmitz, M., & Zettlemoyer, L. (2018, March 20). AllenNLP: A Deep Semantic Natural Language Processing Platform. arXiv.Org. 
https://arxiv.org/abs/1803.07640v2
Modular (2023) Modular Docs – Mojo 🔥 programming manual.. Available at: https://docs.modular.com/mojo/programming-manual.html  (Accessed 1st December 2023).

Kelmendi, L. (2020). English Language Sentences According to Structure (SSRN Scholarly Paper 3559057). https://doi.org/10.2139/ssrn.3559057

Loria S, TextBlob Documentation (n.d.). textblob.readthedocs.io/en/dev/

Vermeer, S., & Trilling, D. (2020). Toward a Better Understanding of News User Journeys: A Markov Chain Approach. Journalism Studies, 21(7), 879–894. https://doi.org/10.1080/1461670X.2020.1722958

Marcus, M. P., Santorini, B., & Marcinkiewicz, M. A. (1993). Building a large annotated corpus of English: The Penn Treebank. Computational Linguistics, 19(2), 313–330

Frequency Data | Open American National Corpus. (n.d.). Retrieved March 14, 2024, from https://anc.org/data/anc-second-release/frequency-data/ 

NVIDIA (n.d.) Cuda Zone - Library of Resources; NVIDIA Developer. Retrieved March 14, 2024, from https://developer.nvidia.com/cuda-zone 

Llama 2: Open Foundation and Fine-Tuned Chat Models | Research—AI at Meta. (n.d.). Retrieved March 25, 2024, from https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/ 

Zehra, F., Javed, M., Khan, D., & Pasha, M. (2020). Comparative Analysis of C++ and Python in Terms of Memory and Time (2020120516). Preprints. https://doi.org/10.20944/preprints202012.0516.v1 

Engelfriet, J., & Rozenberg, G. (1997). Node replacement graph grammars. In Handbook of Graph Grammars and Computing by Graph Transformation (pp. 1–94). WORLD SCIENTIFIC. https://doi.org/10.1142/9789812384720_0001

Martinez, A. R. (2012). Part-of-speech tagging. WIREs Computational Statistics, 4(1), 107–113. https://doi.org/10.1002/wics.195 

Manning, Christopher D., Mihai Surdeanu, John Bauer, Jenny Finkel, Steven J. Bethard, and David McClosky. (2014). The Stanford CoreNLP Natural Language Processing Toolkit In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pp. 55-60

Yan, S. Y. (1998). An Introduction To Formal Languages And Machine Computation. World Scientific.

Mahfuz, F. (2021). MARKOV CHAINS AND THEIR APPLICATIONS. Math Theses. https://scholarworks.uttyler.edu/math_grad/10

Vayadande, K., Sheth, P., Shelke, A., Patil, V., Shevate, S., & Sawakare, C. (2022). Simulation and Testing of Deterministic Finite Automata Machine. INTERNATIONAL JOURNAL OF COMPUTER SCIENCES AND ENGINEERING, 10, 2022. https://doi.org/10.26438/ijcse/v10i1.1317

Kristina Toutanova and Christopher D. Manning. 2000. Enriching the Knowledge Sources Used in a Maximum Entropy Part-of-Speech Tagger. In Proceedings of the Joint SIGDAT Conference on Empirical Methods in Natural Language Processing and Very Large Corpora (EMNLP/VLC-2000), pp. 63-70.

Indu et al. (2016) International Journal of Recent Research Aspects ISSN: 2349-7688, Vol. 3, Issue 2, June
2016, pp. 62-64 


