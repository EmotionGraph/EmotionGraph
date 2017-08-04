import numpy as nm
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import os
import pandas as pd
import graph

emotions = ["joy","trust","fear","surprise","sadness","disgust","anger","anticipation"]
pw=[]
pwc=[]
nw=[]
nwc=[]
words=nm.array(range(800),dtype=str).reshape(8,100)
wc=nm.array(range(800),dtype=str).reshape(8,100)
csvdata=None
fl=0

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
			words[i][j]=line.strip()
			j+=1

		i+=1
	fl=1


def getStems(str):
	arr=[]
	for word in str.split(" "):
		word=(word.strip().lower())
		arr.append(WordNetLemmatizer().lemmatize(word,'v'))
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
	while i<8:
		s=0.00
		nw=0
		for word1 in stemArr:
			to=0
			s1=0.00
			word1 = word1.encode("utf-8").decode("utf-8")
			for word2 in words[i]:
				wordFromList1 = wordnet.synsets(word1)
				wordFromList2 = wordnet.synsets(word2)

				if wordFromList1 and wordFromList2:
					d=wordFromList1[0].wup_similarity(wordFromList2[0])
					#print("%s %s"%(d,type(d)))
					if d is not None:
						s1 += d 
					elif word1==word2:
						s1+=1.0
				to+=1
			s1/=to
			s+=s1
			nw+=1


		s/=nw
		val[i]+=s
		i+=1


	i=0
	print("line starts here")
	row=[l,val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7]]
	csvdata.loc[len(csvdata)]=row
	while i<8 :
		print("%s,%f"%(emotions[i],val[i]*100))
		csvdata
		i+=1

	print("\n")
	

def predictFromFile2(fn,top):
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
	graph.plot()

predictFromFile2("pred.txt","no")