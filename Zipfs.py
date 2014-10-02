import nltk
import math
import matplotlib.pyplot as plt

filen=raw_input("Enter the 1st filename: ")
fp=open(filen,'r').read()
data=nltk.word_tokenize(fp)
f=nltk.FreqDist(data)

filen1=raw_input("Enter the 2nd filename: ")
fp1=open(filen1,'r').read()
data1=nltk.word_tokenize(fp1)
f1=nltk.FreqDist(data1)

filen2=raw_input("Enter the 3rd filename: ")
fp2=open(filen2,'r').read()
data2=nltk.word_tokenize(fp2)
f2=nltk.FreqDist(data2)

filen3=raw_input("Enter the 4th filename: ")
fp3=open(filen3,'r').read()
data3=nltk.word_tokenize(fp3)
f3=nltk.FreqDist(data3)

r=1
rank=[]
frqncy=[]
for freq in f.values():
	rank.append(math.log(r))
	frqncy.append(math.log(freq))
	r=r+1

r=1
rank1=[]
frqncy1=[]
for freq in f1.values():
	rank1.append(math.log(r))
	frqncy1.append(math.log(freq))
	r=r+1

r=1
rank2=[]
frqncy2=[]
for freq in f2.values():
	rank2.append(math.log(r))
	frqncy2.append(math.log(freq))
	r=r+1

r=1
rank3=[]
frqncy3=[]
for freq in f3.values():
	rank3.append(math.log(r))
	frqncy3.append(math.log(freq))
	r=r+1

plt.plot(rank,frqncy,'r+',label=filen)
plt.plot(rank1,frqncy1,'g+',label=filen1)
plt.plot(rank2,frqncy2,'b+',label=filen2)
plt.plot(rank3,frqncy3,'y+',label=filen3)
plt.legend(loc=1)
plt.show()

