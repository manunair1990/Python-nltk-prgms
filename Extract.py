import nltk
#Reading file
fname=raw_input("Enter the file name ")
f=open(fname,"r")
#Tokenize the file
data=nltk.word_tokenize(f.read())
ch='y'
while(ch=='y' or ch=='Y'):
	#Menu
	print "-"*35
	print "Menu"
	print "1.Startswith"
	print "2.endswith"
	print "3.Containing substring"
	cho=input("Choice from Menu ")
	print "-"*35
	if (cho ==1):
		#Startswith function
		strng=raw_input("Enter the srting ")
		sw=set([w for w in data if w.startswith(strng)])
		if (not sw==set([])):
			for i in sw:
				print i,
		else:
			print "No matching words "
	elif (cho ==2):
		#Endswith function
		strng=raw_input("Enter the srting ")
		sw=set([w for w in data if w.endswith(strng)])
		if (not sw==set([])):
			for i in sw:
				print i,
		else:
			print "No matching words "
	elif (cho ==3):
		#Containing function
		strng=raw_input("Enter the srting ")
		sw=set([w for w in data if (strng in w)])
		if (not sw==set([])):
			for i in sw:
				print i,
		else:
			print "No matching words "
	else:
		print "Please Enter valid choice"
	ch=raw_input("\nDo you want to continue (y/n)?")


