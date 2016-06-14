#oh man i totally forgot python
#been using python 3.4 without any major issues - that also seems to be what's needed for NLTK lately

#imports - clean these up once i figure out what to do
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk, re, pprint, csv

infile="pettigrew_letters_gm.txt"
index="/Users/thomer2/GitHub/DHOxSS2016/TJPindexClean.csv"

# with open(index, 'wb') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in spamreader:
# 		print (', '.join(row))


with open(infile, 'r') as myfile:
    data=myfile.read().split('\n\n\n', '')

for i in data:
	if "Box" in data[i]:
		continue
	else:
		print ("this is data!!! and I will put it in a row eventually!")


# 		
# for i in range(10,20):
#   if 'Box' in m[i]:
# ...   print("yuppers " + m[i])
# ...  else:
# ...   continue
	
# counter = 0
# 
# with open(infile) as p:
# 	counter += 1
# 	filename="pettigrew"+str(counter)


# can break each letter on "BOX?"	

# https://pythonprogramming.net/named-entity-recognition-stanford-ner-tagger/






st = StanfordNERTagger('/Users/thomer2/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/thomer2/stanford-ner-2015-12-09/stanford-ner.jar',encoding='utf-8') 

text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

TJPtext = '''My Dear Sir, 
I only received your favour of the 16th late last night, on my return from the Syro-Egyptian, or I would have answered before.  
I shall be very happy to meet Mr Wright at the Archaeological meeting this evening, the meeting of which society indeed, I have attended on the last occasion.  
Believe me, 
My dear sir, 
Yours very sincerely, 
W. Francis Ainsworth
Wednesday Morn
Dec 17th 1845'''

len(TJPtext)
tokens=word_tokenize(TJPtext)
text=nltk.Text(tokens)
text.collocations()
def lexical_div(text):
  return len(set(text))/len(text)
long_words = [w for w in V if len(w) > 10]
sorted(long_words)
fdist=FreqDist(text)
sorted(w for w in set(text)if len(w)>2 and fdist[w]>2
nltk.pos_tag(text)
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)