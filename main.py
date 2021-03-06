import numpy as nm
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet,stopwords
import os
import pandas as pd
import graph
import Sentence as sn
import re
from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()
emotions = ["joy","trust","fear","surprise","sadness","disgust","anger","anticipation"]
pw=[]
pwc=[]
nw=[]
nwc=[]
#words=nm.array(range(800),dtype=str).reshape(8,100)
qw=open("debug.txt","w")
wc=nm.zeros(shape=(5,2))
csvdata=None
fl=0
stop=set(stopwords.words('english'))
w, h = 100, 8;
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
	global pw,pwc,nw,nwc,fl,words,wc,st
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
			words[i][j]=(line.strip())
			#print(words[i][j])
			j+=1

		i+=1
	fl=1


def getStems(str):
	global st
	arr=[]
	for word in str.split(" "):
		word=(word.strip().lower())
		word=re.sub(r"[,.:;'\"()\[\]{}]","",word)
		if word in stop:
			continue
		word=WordNetLemmatizer().lemmatize(word,'v')
		#word=st.stem(word)
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
	
	for word1 in stemArr:
		
		
		cati=-1
		maxs=0.00
		word1 = word1.encode("utf-8").decode("utf-8")
		i=0
		while i<8:
			
			s1=0.00
			to=0
			for word2 in words[i]:
				
				word2=str(word2)
				
				y = []
				for w1 in wordnet.synsets(word1):
					for w2 in wordnet.synsets(word2):
						try:

							x = w1.path_similarity(w2);
							#print(x,w1,w2)
							if(type(x) == float):
								#print("Hello")
								y.append(x)

							#print("something")


						except:
							#print("error")
							continue;
				#print(y)
				if len(y)>0:
					if word1==word2:
						d=10.0
					else:
						d=(nm.mean(y)*10)
					to+=1
				else:
					if word1==word2:
						d=10.0
						to+=1
					else:
						d=0
				s1+=d
				
				
				# if word2 != "0":
				# 	qw.write(str(d)+" "+word1+" "+word2+" "+emotions[i]+"\n")
				
					
			
			if to!=0 :
				s1/=to
			else:
				s1=0
			
			if(s1>maxs):
				maxs=s1
				cati=i

			i+=1

		val[cati]+=maxs
		print(word1,emotions[cati],maxs)



	#i=0
	#print("line starts here")
	row=[l,val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7]]
	csvdata.loc[len(csvdata)]=row
	
	

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