#oh man i totally forgot python
#been using python 3.4 without any major issues - that also seems to be what's needed for NLTK lately

#imports - clean these up once i figure out what to do
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk, re, pprint, csv

infile="pettigrewSubset.txt"
# index="/Users/thomer2/GitHub/DHOxSS2016/TJPindexClean.csv"

with open(infile, 'r') as myfile:
	datas=myfile.read()
	datas=datas.split('\n\n\n')
	
outfile = open("someData.csv","a")
w=csv.writer(outfile)

indBox=[]
allBoxes=[]

for i in datas:
	if i.startswith("Box"):
		allBoxes.append(indBox)
#		print(allBoxes)
		indBox=[]
		indBox.append(i)
#		print(indBox)
		
	else:
		indBox.append(i)
#		print(indBox)
allBoxes.append(indBox) #necessary to close loop and append last box

#silly counter printer that takes up less printspace than full thingy

for i in allBoxes:
	if i==[]:
		pass
	else:
		print("bop")
		for n in i:
			print ("beep")

indLetter=[]
allLetters=[]
countyMcCountFace=0

for box in allBoxes:
	if box ==[]:
		pass
	else:
		letters=box[1::]
		for i in letters:
			indLetter=[box[0]]
			tokens=word_tokenize(i)
			text=nltk.Text(tokens)
			coll=text.collocations()
			V=set(text)
			long_words = [w for w in V if len(w) > 10]
			indLetter.append(i)
			indLetter.append(coll)
			indLetter.append(long_words)			
			allLetters.append(indLetter)
			countyMcCountFace=countyMcCountFace+1
			print(countyMcCountFace)
			print(indLetter)
			indLetter=[]
print ('found ', len(allLetters), ' of Pettigrew\'s papers!')


# 
# len(TJPtext)
# tokens=word_tokenize(TJPtext)
# text=nltk.Text(tokens)
# text.collocations()
# def lexical_div(text):
#	return len(set(text))/len(text)
# long_words = [w for w in V if len(w) > 10]
# sorted(long_words)
# fdist=FreqDist(text)
# sorted(w for w in set(text)if len(w)>2 and fdist[w]>2
# nltk.pos_tag(text)
# tokenized_text = word_tokenize(text)
# classified_text = st.tag(tokenized_text)
# 
# print(classified_text)

		




# st = StanfordNERTagger('/Users/thomer2/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/thomer2/stanford-ner-2015-12-09/stanford-ner.jar',encoding='utf-8') 
# 
# text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
# 
TJPtext = '''My Dear Sir, 
I only received your favour of the 16th late last night, on my return from the Syro-Egyptian, or I would have answered before.  
I shall be very happy to meet Mr Wright at the Archaeological meeting this evening, the meeting of which society indeed, I have attended on the last occasion.  
Believe me, 
My dear sir, 
Yours very sincerely, 
W. Francis Ainsworth
Wednesday Morn
Dec 17th 1845'''
	
# 	print(allBoxes)
# 		while status =0
# 			if "Box" in maybetext:
# 				status=1
# 			else:
# 				w.writerow([folder,name,maybetext])
# 				next=datas.index(i)+1
# 				maybetext=datas[next]
# 			continue
# 		print(text)



#		text=datas.next()
#		w.writerow([folder,name])
		
#		else:
#			boxMeta.append[i]
#			print(boxMeta)
# 
#		continue #or pass works equally well
#	else:
#		print ("this is data!!! and I will put it in a row!")
#		w.writerow([boxMeta[0]],[boxMeta[1]],[i])

