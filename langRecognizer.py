import ngrams, operator, collections, langVector, sys, argparse 

#HOW TO IMPROVE: use collections.OrderedDict (pro záznam skóre), ask for creating new vector file
#TODO: shoda u určení jazyků
#TODO: váhy! - viz HOW TO IMROVE
#MAYBE: improve the command line arguments???
#TODO: vyřešit ten pitomý logaritmus!


#count a score for sentence from vector of a language ~ probability for ngrams in the language (suma of logarithms)
def count_ngram_score(sentence, vector, n):
	score = 0
	ngrams_array = ngrams.make_ngrams(sentence, n)
	for ngram in ngrams_array:	
		if ngram in vector[n-1]:
			score += vector[n-1][ngram]
			#print("add ", vector[n-1][ngram], "for ", ngram)
		else:
			print("not found ", ngram)
			score += 20 #TODO poladit tuto penalizaci --> nějak implementovat add one smoothing
	return score

#n = number of kinds of ngrams (uni + bi + trigram = 3)
def recognize_language(sentence, vectors, n):
	scores = []
	for i in range(0,n):
		scores.append({})
		for language in vectors.keys():
			print("work with ", language)
			scores[i][language] = count_ngram_score(sentence, vectors[language], i+1)
	print(scores)
	#result for uni/bi/trigrams - 0 ~ uni etc.
	result = []
	for i in range(0,n):
		#find the language with largest score for i-gram
		result.append(min(scores[i].items(), key=operator.itemgetter(1))[0])
	counted_result = collections.Counter(result)
	#find the languge which is mostly appeared - dořešit váhy!!!
	language = max(counted_result.items(), key=operator.itemgetter(1))[0]
	probability = counted_result[language] / sum(counted_result.values())
	return language, probability


#parser = argparse.ArgumentParser(description='Recognize language of given sentence (text).')
#parser.add_argument('-s', metavar='Text', dest='sentence', help='sentence (text) you want to recognize', action='store_const', const="notext58")
#parser.add_argument('--vector_file', '-vf', metavar='File name', type=str, dest="vector_file", help='file with vetors of languages', default='language_vector.p')
#args = parser.parse_args()   

if len(sys.argv) > 2:
	sentence = sys.argv[1]
	vector_file = sys.argv[2]
elif len(sys.argv) == 2:
	sentence = sys.argv[1]
	vector_file = "language_vector.p"
else:	
	sentence = input("Your sentence: ")
	vector_file = "language_vector.p"

#if args.sentence == "notext58": 
#	sentence = input("Your sentence: ")
#else:
#	sentnce = args.sentence

vectors = langVector.load_vector(vector_file)
print(recognize_language(sentence, vectors, 3))

