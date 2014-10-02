import nltk
import pos
from urllib import urlopen
urlname=raw_input("Enter the url: ")
site=urlopen(urlname).read()
fle=nltk.clean_html(site)
data=nltk.word_tokenize(fle)
p=nltk.pos_tag(data)

noun1=[]
verb1=[]
art1=[]

print "-"*10,"Noun","-"*10
noun=set([i[0] for i in p if i[1].startswith("N") and i[0].isalpha()])
rank=0
for i in noun:
	j=(rank+1,i)
	noun1.append(j)
	rank=rank+1
n=tuple(noun1)
pos.table(n,"Noun")


print "-"*10,"Verb","-"*10
verb=set([i[0] for i in p if i[1].startswith("V") and i[0].isalpha()])
rank=0
for i in verb:
	j=(rank+1,i)
	verb1.append(j)
	rank=rank+1
v=tuple(verb1)
pos.table(v,"Verb")

print "-"*10,"Article","-"*10
art=set([i[0] for i in p if i[1].startswith("DT") and i[0].isalpha()])
rank=0
for i in art:
	j=(rank+1,i)
	art1.append(j)
	rank=rank+1
a=tuple(art1)
pos.table(a,"Article")



