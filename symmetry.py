from nltk.corpus import wordnet

list1 = ['xyx', 'xyx','awesome','beauty']
list2 = ['xyx', 'xyx','copy', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
list = []

for word1 in list1:
	print(word1+"--->")
	for word2 in list2:
		wordFromList1 = wordnet.synsets(word1)
		wordFromList2 = wordnet.synsets(word2)
		if wordFromList1 and wordFromList2:
			s = wordFromList1[0].wup_similarity(wordFromList2[0])
			print(s)
			list.append(s)
		elif word1==word2:
			print("1.0")

    



