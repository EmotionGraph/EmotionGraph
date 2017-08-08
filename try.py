import numpy as nm
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet,stopwords
import os
import pandas as pd
import graph
import Sentence as sn
import re

def convert(word, from_pos, to_pos):    
    """ Transform words given from/to POS tags """
 
    synsets = wordnet.synsets(word, pos=from_pos)
 
    # Word not found
    if not synsets:
        return []
 
    # Get all lemmas of the word (consider 'a'and 's' equivalent)
    lemmas = [l for s in synsets
                for l in s.lemmas 
                if s.name.split('.')[1] == from_pos
                    or from_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)
                        and s.name.split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)]
 
    # Get related forms
    derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in lemmas]
 
    # filter only the desired pos (consider 'a' and 's' equivalent)
    related_noun_lemmas = [l for drf in derivationally_related_forms
                             for l in drf[1] 
                             if l.synset.name.split('.')[1] == to_pos
                                or to_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)
                                    and l.synset.name.split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)]
 
    # Extract the words from the lemmas
    words = [l.name for l in related_noun_lemmas]
    len_words = len(words)
 
    # Build the result in the form of a list containing tuples (word, probability)
    result = [(w, float(words.count(w))/len_words) for w in set(words)]
    result.sort(key=lambda w: -w[1])
 
    # return all the possibilities sorted by probability
    return result


emotions = ["joy","trust","fear","surprise","sadness","disgust","anger","anticipation"]
pw=[]
pwc=[]
nw=[]
nwc=[]
#words=nm.array(range(800),dtype=str).reshape(8,100)

wc=nm.zeros(shape=(5,2))
csvdata=None
fl=0
stop=set(stopwords.words('english'))
w, h = 30, 8;
words = [[0 for x in range(w)] for y in range(h)] 
#words=[[None]*100]*8
# def init(top) :
# 	global pw,pwc,nw,nwc,fl,words,wc
# 	home="A:\\Sentimental anlysis - Copy\\"
# 	i=0;
# 	for em in emotions:
# 		fn="%s.txt"%em
# 		print(os.getcwd())
# 		try:
# 			fp = open(fn,"r+")
# 			data = fp.readlines()

# 			for line in data:
# 				words[i].append(line.strip())
# 		except:
# 			print("%s is not found" % fn)

# 		i+=1
# 	fl=1

def init(top) :
	global pw,pwc,nw,nwc,fl,words,wc
	#home="A:\\Sentimental anlysis - Copy\\"
	i=0;
	for em in emotions:
		fn="%s.txt"%em
		#print(os.getcwd())
		fp = open(fn,"r+")
		data = fp.readlines()
		j=0
		for line in data:
			#print(i,j)
			#print(line.strip())
			words[i][j]=WordNetLemmatizer().lemmatize(line.strip(),'n')
			print(words[i][j])
			j+=1

		i+=1
	fl=1


def getStems(str):
	arr=[]
	for word in str.split(" "):
		word=(word.strip().lower())
		word=re.sub(r"[,.:;'\"]","",word)
		if word in stop:
			continue
		word=WordNetLemmatizer().lemmatize(word,'n')

		arr.append(word)
		#print(word+" ")
	return arr

def predict2(stemArr,l):
	global words,csvdata
	# pl=len(pw)
	# nl=len(nw)
	p=0.00
	n=0.00
	val = [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
	#print("{Positive:-")
	i=0
	while i<1:
		s=0.00
		nw=0
		for word1 in stemArr:
			to=0
			s1=0.00
			word1 = word1.encode("utf-8").decode("utf-8")
			for word2 in words[i]:
				
				word2=str(word2)
				y = []
				for w1 in wordnet.synsets(word1):
					for w2 in wordnet.synsets(word2):
						try:

							x = w1.wup_similarity(w2);
							print(x,w1,w2)
							if(type(x) == float):
								#print("Hello")
								y.append(x)

							#print("something")


						except:
							print("error")
							continue;
				#print(y)
				if len(y)>0:
					if word1==word2:
						d=1.0
						s1+=1.0
						to+=1
					else:
						d=(np.mean(y)*10)
				else:
					if word1==word2:
						d=1.0
						s1+=1.0
						to+=1
					else:
						d=0
				
				print(d,word2,word1)
				if d is not None:
					print(str(word2)+" ")
				
					
			
			if to!=0 :
				s1/=to
			else:
				s1=0
			s+=s1
			nw+=1


		#s/=nw
		val[i]+=s
		i+=1


	print(val[0])
	print("\n")
	

def predictFromFile2(fn,top):
	fn=sn.getSentenceFile(fn)
	global fl,csvdata
	csvdata=pd.DataFrame(columns=('line',"joy","trust","fear","surprise","sadness","disgust","anger","anticipation"))
	
	if fl ==0:
		init(top)
	f=open(fn,"r+")
	data = f.readlines()
	l=0
	for line in data:
		l+=1
		#top.pr  ("\n"+line)
		stemArr = getStems(line)
		#top.pr(predict2(stemArr))
		predict2(stemArr,l)

	csvdata.to_csv(fn+".csv",index=False)
	graph.plot(fn)

predictFromFile2("pred.txt","no")