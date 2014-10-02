import nltk
ch='y'
while ch=='y' or ch=='Y':
	#Reading file
	fname=raw_input("Enter the filename: ")
	fp=open(fname,'r').read()
	#Tokenize file
	data=nltk.word_tokenize(fp)
	ngram=input("Enter the ngram number: ")
	rank=input("Enter the rank: ")
	#Making ngrams
	ndata=nltk.util.ngrams(data,ngram)
	fdata=[w for w in ndata if w[0][0].isalpha()]
	f=nltk.FreqDist(fdata)
	k,n=f.items()[rank-1]
	print k
	print n
	plt=raw_input("Do you want to plot? (y/n): ")
	if plt=='y' or plt=='Y':
		f.plot(20)
	ch=raw_input("Do you want to continue? (y/n): ")

