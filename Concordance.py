import nltk
ch='y'
while (ch=='y' or ch=='Y'):
	#Reading file
	fname=raw_input("Enter the filename ")
	fil=open(fname,'r')
	#Tokenize file
	data=nltk.word_tokenize(fil.read())
	text=nltk.Text(data)
	strng=raw_input("Enter the string ")
	#Doing concordance
	if strng in data:
		text.concordance(strng)
	else:
		print "This word is not in the text"
	ch=raw_input("Do you want to continue?(y/n)")

