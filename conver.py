from nltk.corpus import wordnet as wn
import numpy as np
from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()

def nounify(verb_word):
    set_of_related_nouns = set()

    l1=wn.morphy(verb_word, wn.VERB)
    if(l1 is not None) :
        print(l1)
        for lemma in wn.lemmas(l1, pos="v"):
            for related_form in lemma.derivationally_related_forms():
                for synset in wn.synsets(related_form.name(), pos=wn.NOUN):
                    if wn.synset('person.n.01') in synset.closure(lambda s:s.hypernyms()):
                        set_of_related_nouns.add(synset)

    l1=wn.morphy(verb_word, wn.ADJ)
    if(l1 is not None) :
        print(l1)
        for lemma in wn.lemmas(l1, pos="a"):
            for related_form in lemma.derivationally_related_forms():
                for synset in wn.synsets(related_form.name(), pos=wn.NOUN):
                    if wn.synset('person.n.01') in synset.closure(lambda s:s.hypernyms()):
                        set_of_related_nouns.add(synset)

        for lemma in wn.lemmas(l1, pos="s"):
            for related_form in lemma.derivationally_related_forms():
                for synset in wn.synsets(related_form.name(), pos=wn.NOUN):
                    if wn.synset('person.n.01') in synset.closure(lambda s:s.hypernyms()):
                        set_of_related_nouns.add(synset)

    return set_of_related_nouns

word1=st.stem("happy")
word2=st.stem("happiness")

# ws1=nounify(word1)
# ws2=nounify(word2)
# print(ws1)
# print(ws2)    
y = []
for w1 in wn.synsets(word1):
    for w2 in wn.synsets(word2):
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


