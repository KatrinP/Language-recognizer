import ngrams, operator, collections, langVector, sys, argparse 

#HOW TO IMPROVE: use collections.OrderedDict (pro záznam skóre), ask for creating new vector file
#TODO: shoda u určení jazyků
#TODO: váhy! - viz HOW TO IMROVE
#MAYBE: improve the command line arguments???

#count a score for sentence from vector of a language ~ probability for ngrams in the language (suma of logarithms)
def count_ngram_score(sentence, vector, n):
	score = 0
	ngrams_array = ngrams.make_ngrams(sentence, n)
	#smoothing - for ngrams which don't appear in vector of language
	smoothing = max(vector[n-1].items(), key=operator.itemgetter(1))[0]

	for ngram in ngrams_array:	
		if ngram in vector[n-1]:
			score += vector[n-1][ngram]
			#print("add ", vector[n-1][ngram], "for ", ngram)
		else:
			#print("not found ", ngram, "add ", vector[n-1][smoothing] )
			score += vector[n-1][smoothing]/1.5 #zde pořešit míru, 1 byla moc přísná 
	return score

#n = number of kinds of ngrams (uni + bi + trigram = 3)
def recognize_language(sentence, vectors, n):
	scores = []
	for i in range(0,n):
		scores.append({})
		for language in vectors.keys():
			#print("work with ", language)
			scores[i][language] = count_ngram_score(sentence, vectors[language], i+1)
	print(scores)
	#result for uni/bi/trigrams - 0 ~ uni etc.
	result = []
	#result2 = {}
	result2 = collections.defaultdict(int)

	for i in range(0,n):
		#find the language with largest score for i-gram
		#result.append(min(scores[i].items(), key=operator.itemgetter(1))[0])
		a = min(scores[i].items(), key=operator.itemgetter(1))[0] 
		result2[a] += (i+1) * 1 #number is the weight
		print("tomuto přičítám jedničku: ",result2[a], a)
		result.append(a)
		#for j in range(0,i):
		#	result.append(a)
	print("result2: ",result2)		
	#counted_result = collections.Counter(result)
	#find the languge which is mostly appeared - dořešit váhy!!!
#	language = max(counted_result.items(), key=operator.itemgetter(1))[0]
	highest = max(result2.values())
	same_result = []
	for key, value in result2.items():
		if value == highest:
			same_result.append(key)
	if len(same_result) > 1:
		out = False
		for i in range(n, 0, - 1):
			for language in same_result:
				if result[i-1] == language:
					language2 = language
					print(language)
					out = True
					break
			if out:
				break
	else:
		language2 = same_result[0]#max(result2.items(), key=operator.itemgetter(1))[0]
	
	probability = result2[language2] / sum(result2.values())
#	probability = counted_result[language] / sum(counted_result.values())
	return language2, probability


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

