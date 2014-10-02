from __future__ import division
import nltk
import re

fname1=raw_input("Enter the file name: ")
fle1=open(fname1,"r").read()

fname2=raw_input("Enter the file name: ")
fle2=open(fname2,"r").read()

fname3=raw_input("Enter the file name: ")
fle3=open(fname3,"r").read()

fname4=raw_input("Enter the file name: ")
fle4=open(fname4,"r").read()

print "calculating......"
word1=nltk.word_tokenize(fle1)
word2=nltk.word_tokenize(fle2)
word3=nltk.word_tokenize(fle3)
word4=nltk.word_tokenize(fle4)
wcount1=len(word1)
wcount2=len(word2)
wcount3=len(word3)
wcount4=len(word4)

sent1=nltk.sent_tokenize(fle1)
sent2=nltk.sent_tokenize(fle2)
sent3=nltk.sent_tokenize(fle3)
sent4=nltk.sent_tokenize(fle4)
scount1=len(sent1)
scount2=len(sent2)
scount3=len(sent3)
scount4=len(sent4)

ccount1=len(re.findall('[a-zA-Z0-9]',fle1))
ccount2=len(re.findall('[a-zA-Z0-9]',fle2))
ccount3=len(re.findall('[a-zA-Z0-9]',fle3))
ccount4=len(re.findall('[a-zA-Z0-9]',fle4))

ari1=4.71*(ccount1/wcount1)+0.5*(wcount1/scount1)-21.43
ari2=4.71*(ccount2/wcount2)+0.5*(wcount2/scount2)-21.43
ari3=4.71*(ccount3/wcount3)+0.5*(wcount3/scount3)-21.43
ari4=4.71*(ccount4/wcount4)+0.5*(wcount4/scount4)-21.43

print "\n"
print "Filename"+" "*17+"ARI"
print "--------"+" "*17+"---"
print fname1+"-"*(20-len(fname1)),ari1
print fname2+"-"*(20-len(fname2)),ari2
print fname3+"-"*(20-len(fname3)),ari3
print fname4+"-"*(20-len(fname4)),ari4
print "\n"

