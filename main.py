import tweepy
from tweepy import OAuthHandler
import ui
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

 
consumer_key = 'QdlVszqNqxvc32Xs1TQIw7160'
consumer_secret = 'DP4LF5rkvZtQNd1AFD5Cj2VdvqVqmSiFheUgbzNNSyWQjJMO6C'
access_token = '3123348268-YlUFXbCQSX5bFFSEbmiiCuzZQ5J8QtVUsv09j8q'
access_secret = 'lfpY9Gk3HWAec8WSvixkf9Or55zXG4uRaWGHY8g1e7tSB'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
positiveFile="pos_base.txt"
negativeFile="neg_base.txt"
try:
	fp= open(positiveFile,"r+")
except:
	fp=open(positiveFile,"w")
	fp.close()
	fp= open(positiveFile,"r+")

try:
	fn= open(negativeFile,"r+")
except:
	fn=open(negativeFile,"w")
	fn.close()
	fn= open(negativeFile,"r+")


pw=[]
pwc=[]
nw=[]
nwc=[]
fl=0

def init(top) :
	global pw,pwc,nw,nwc,fl
	data = fp.readlines()
	for line in data:
		#top.pr  (line)
		#x=line.split(" ")
		#pw.append(x[0])
		#pwc.append(x[1])
		pw.append(line.strip())

	# for word in pw:
	# 	top.pr  (word)

	data = fn.readlines()
	for line in data:
		#top.pr  (line)
		#x=line.split(" ")
		#nw.append(x[0])
		#nwc.append(x[1])
		nw.append(line.strip())

	# for word in nw:
	# 	top.pr  (word)

	fl=1



def readTimeline() :
	for status in tweepy.Cursor(api.home_timeline).items(0):
		try:
			ui.pr  (status.text.encode("utf-8"))
		except:
			ui.pr   ("This is an error message!")

def followers():
	for friend in tweepy.Cursor(api.friends).items():
		ui.pr  (friend._json)

def tweets() :
	public_tweets = api.home_timeline()
	tw=[]
	for tweet in public_tweets:
		stri = tweet.text.encode('utf-8').decode('utf-8').strip()
		tw.append(stri)
		#ui.pr  (type(stri))
		# ui.pr  ("\n")
		# for word in stri.split(" "):
	 #    		ui.pr  (((word.encode('utf-8'))))
	return tw

def learnFromTweets():
	ui.pr  ("Enter 1 for positive sentence\nEnter 0 for negative sentence");
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		stri = tweet.text.encode('utf-8').decode('utf-8').strip()
		#ui.pr  (type(stri))

		ui.pr  ("\n")
		for word in stri.split(" "):
	    		ui.pr  (((word.encode('utf-8'))))

def getStems(str):
	arr=[]
	for word in str.split(" "):
		word=(word.strip().lower())
		arr.append(WordNetLemmatizer().lemmatize(word,'v'))
	return arr

def find(word,t):
	if t== "0" or t== 0:
		le=len(nw)
		l=0
		r=le-1
		m=0
		while l<=r:
			m=int((l+r)/2)
			if nw[m] == word :
				x=int(nwc[m])
				x=x+1
				nwc[m]=x
				return m
			elif nw[m] > word :
				r=m-1;
			else:
				l=m+1

		return m
	else :
		le=len(pw)
		l=0
		r=le-1
		m=0
		while l<=r:
			m=int((l+r)/2)
			
			if pw[m] == word :
				x=int(pwc[m])
				x= x+1
				pwc[m]=x
				return m
			elif pw[m] > word :
				r=m-1;
			else:
				l=m+1

			#ui.pr  ("%d %d %d"%(l,m,r))

		return m

	return 0


def process(t,stemArr,top=0):
	global pw,pwc,nw,nwc
	pl=len(pw)
	nl=len(nw)
	if t == "0"  or t== 0:
		for word in stemArr:
			ind=int(find(word,t))
			top.pr  ("%s %d"%(word,ind))
			if (nl>ind) and (nw[ind]==word) :
				continue
			elif nl>ind and nw[ind] < word and  ind+1<nl and nw[ind+1]>word :
				#ind+1
				nw.insert( ind+1, word)
				nwc.insert( ind+1, 1)
			elif nl>ind and nw[ind] < word  and  ind+1<nl  and  nw[ind+1]<word :
				while ind<nl  and  nw[ind] < word :
					ind+=1
				#insert
				nw.insert( ind, word)
				nwc.insert( ind, 1)
			elif nl>ind and nw[ind] > word  and  ind-1>=0 and nw[ind-1]<word:
				#ind
				nw.insert( ind, word)
				nwc.insert( ind, 1)
			elif nl>ind and nw[ind] > word  and  ind-1>=0 and nw[ind-1]>word:
				while ind>=0  and  nw[ind] > word :
					ind-=1
				#ind+1
				nw.insert( ind+1, word)
				nwc.insert( ind+1, 1)
			elif ind==0 :
				#ind
				nw.insert( ind, word)
				nwc.insert( ind, 1)
			elif ind == nl-1 and nw[ind]<word:
				nw.insert( ind+1, word)
				nwc.insert( ind, 1)
			else:
				nw.insert( ind, word)
				nwc.insert( ind, 1)
	else:
		for word in stemArr:
			ind=int(find(word,t))
			top.pr  ("%s %d"%(word,ind))
			if pl>ind and pw[ind]==word:
				continue
			elif pl>ind and pw[ind] < word  and  ind+1<pl  and  pw[ind+1]>word :
				#ind+1
				pw.insert( ind+1, word)
				pwc.insert( ind+1, 1)
			elif pl>ind and pw[ind] < word  and  ind+1<pl  and  pw[ind+1]<word :
				while ind<pl  and  pw[ind] < word :
					ind+=1
				#insert
				pw.insert( ind, word)
				pwc.insert( ind, 1)
			elif pl>ind and pw[ind] > word  and  ind-1>=0 and pw[ind-1]<word:
				#ind
				pw.insert( ind, word)
				pwc.insert( ind, 1)
			elif pl>ind and pw[ind] > word  and  ind-1>=0 and pw[ind-1]>word:
				while ind>=0  and  pw[ind] > word :
					ind-=1
				#ind+1
				pw.insert( ind+1, word)
				pwc.insert( ind+1, 1)
			elif ind==0 :
				#ind
				pw.insert( ind, word)
				pwc.insert( ind, 1)
			elif ind == nl-1 and pw[ind]<word:
				pw.insert( ind+1, word)
				pwc.insert( ind, 1)
			else:
				pw.insert( ind, word)
				pwc.insert( ind, 1)


def showFreq(top=0):
	global pw,pwc,nw,nwc
	pl=len(pw)
	nl=len(nw)
	top.pr  ("Positive :-")
	i=0
	while i<pl:
		top.pr  ("%s - %d"%(pw[i],int(pwc[i])))
		i+=1

	top.pr  ("Negative :-")
	i=0
	while i<nl:
		top.pr  ("%s - %d"%(nw[i],int(nwc[i])))
		i+=1

def writeInFile(top=0):
	global pw,pwc,nw,nwc,fp,fn
	pl=len(pw)
	nl=len(nw)
	top.pr  ("Positive :-")
	fp.close()
	fn.close()
	f= open("positive.txt","w")
	i=0
	while i<pl:
		f.write("%s %d\n"%(pw[i].strip (),int(pwc[i])))
		i+=1

	f.close()
	top.pr  ("Negative :-")
	f= open("negative.txt","w")
	i=0
	i=0
	while i<nl:
		f.write("%s %d\n"%(nw[i].strip (),int(nwc[i])))
		i+=1

	f.close()
	fp= open("positive.txt","r+")
	fn= open("negative.txt","r+")


def predict(stemArr):
	global pw,pwc,nw,nwc,fp,fn,top
	pl=len(pw)
	nl=len(nw)
	p=0
	n=0
	for word in stemArr:
		ind=int(find(word,"1"))
		pf =0
		if pw[ind]==word:
			pf= pwc[ind]

		ind=int(find(word,"0"))
		nf =0
		if nw[ind]==word:
			nf= nwc[ind]
		if pf>0 or nf>0:
			p+=(pf*100)/(pf+nf)
			n+=(nf*100)/(pf+nf)

	if p>n:
		return "Positive"
	elif p<n:
		return "Negative"
	elif p>0:
		return "Neutral"
	else:
		return "Can't ui.pr edict"

def predict2(stemArr):
	global pw,nw
	# pl=len(pw)
	# nl=len(nw)
	p=0.00
	n=0.00
	print("{Positive:-")
	for word1 in stemArr:
		s=0.00
		word1 = word1.encode("utf-8").decode("utf-8")
		#print(word1)
		for word2 in pw:
			wordFromList1 = wordnet.synsets(word1)
			wordFromList2 = wordnet.synsets(word2)
			
			if wordFromList1 and wordFromList2:
				d=wordFromList1[0].wup_similarity(wordFromList2[0])
				#print("%s %s"%(d,type(d)))
				if d is not None:
					s += d 
				
			if word1==word2:
					s+=1.0
		p+=s

	print("{Negative:-")
	for word1 in stemArr:
		word1 = word1.encode("utf-8").decode("utf-8")
		#print(word1)
		s=0.00
		for word2 in nw:
			wordFromList1 = wordnet.synsets(word1)
			wordFromList2 = wordnet.synsets(word2)
			if wordFromList1 and wordFromList2:
				d=wordFromList1[0].wup_similarity(wordFromList2[0])
				if d is not None:
					s += d 
				print(d)
			if word1==word2:
					print("matched word %s" % word2)
					s+=1.0
		n+=s

	if p>n:
		return "Positive"
	elif p<n:
		return "Negative"
	elif p>0:
		return "Neutral"
	else:
		return "%f %f Can't ui.pr edict" %(p,n)



def learnFromFile(fn,top=0):
	
	#top.pr  ("Enter 1 for positive sentence\nEnter 0 for negative sentence");
	f=open(fn,"r+")
	data = f.readlines()
	for line in data:
		x=line.split("|||")
		top.pr  ("\n"+x[0]+"(1/0)>> %s "%x[1])
		stemArr = getStems(x[0])
		t = x[1]
		
		#top.pr("You inputed: %s"% t)
		process(t,stemArr,top)

	showFreq(top)
	writeInFile(top)

def predictFromFile(fn):
	global top
	f=open(fn,"r+")
	data = f.readlines()
	for line in data:
		top.pr  ("\n"+line)
		stemArr = getStems(line)
		top.pr(predict(stemArr))

def predictFromFile2(fn,top):
	global fl
	if fl ==0:
		init(top)
	f=open(fn,"r+")
	data = f.readlines()
	for line in data:
		top.pr  ("\n"+line)
		stemArr = getStems(line)
		top.pr(predict2(stemArr))

def predictFromTweets(top):
	global fl
	if fl ==0:
		init(top)
	twe=tweets()
	for line in twe:
		top.pr  ("\n"+line)
		stemArr = getStems(line)
		top.pr(predict2(stemArr))

#init()
#learnFromFile("learn.txt")
#ui.pr edictFromFile("test.txt")
#tweets()
#readTimeline()
#followers()

    
#if __name__ == '__main__':
    #init()
    #learnFromFile("learn.txt")


