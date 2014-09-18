Language-recognizer
===================

First try to program something useful in python. Program should recognize a language of text input, uses the n-grams probability.

Need some improve in code and in the algorithm as well (do not give the best answers...), need to set same weight and values...

##langRecognizer.py
- already working
- try: `python3 langRecognizer.py "tell me: in witch language is this input" some_vector_file`, the vector file is not mandatory, default is language_vector.p
- `python3 langRecognizer.py` (without any argument) works as well

##ngrams.py
- can creater ngrams and count the number of ngrams in text, count the probability...

##langVector.py
- some useful function for creating vector of languages

##addVector.py
- already working
- command line script for adding a new language vector into existing (or new) file with vector
- `python3 addVector.py "language" file_with_plain_text file_with_vectors`
- last argument is optional, default is language_vector.p

##language_vector.p
- file with ready vectors, just for testing (create from small data), but you can use it for trying as well
- data source: Gutenberg.org
