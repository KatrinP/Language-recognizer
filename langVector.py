import ngrams, pickle, os, sys
		
#make a propbability list (vector) for one language
#source_file - file with plain text
def vector_of_language(source_file):
	opened_file = open(source_file, encoding="utf-8")
	text = opened_file.read()

	unigram_probability = ngrams.probability(ngrams.count_ngrams(text,1))
	bigram_probability = ngrams.probability_of_bigram(ngrams.count_ngrams(text, 2))
	trigram_probability = ngrams.probability_of_trigram(ngrams.count_ngrams(text, 3))
	return [unigram_probability, bigram_probability, trigram_probability]

def add_language_vector(language, source_file, vector_file):
	vectors = load_vector(vector_file)
	vectors[language] =  vector_of_language(source_file)
	with open(vector_file, "wb" ) as f:
		pickle.dump(vectors, f)
	print(*("I have learned ",language,"!"), sep="")
	
	return

def load_vector(vector_file):
	if os.path.isfile(vector_file) and os.stat(vector_file).st_size > 0:
		with open(vector_file, "rb") as f:
			vectors = pickle.load(f)
	else: vectors = {}
	if vectors == {}:
		user_answer = input("File with language vectors was empty or didn't exist. New empty set of vectors will be created. OK? (Y/n): ")
		if user_answer.lower() == "n":
			sys.exit("Work with no vector file is not possible, sorry!")
	return vectors
