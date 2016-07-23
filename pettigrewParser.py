#oh man i totally forgot python
#python 3.4

#imports - clean these up once i figure out what to do
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk, re, pprint, csv

#infile="pettigrewSubset.txt"
#infile='inputs/pettigrew_letters_only.txt'
infile='inputs/pettigrewNERraw.txt'

with open(infile, 'r') as myfile:
	datas=myfile.read()
	datas=datas.split('\n\n\n')
	
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
			indLetter.append(long_words)	 #maybe split this up/out later		
			indLetter.append(len(i))
		
			allLetters.append(indLetter)
		
			countyMcCountFace=countyMcCountFace+1
			print(countyMcCountFace)
			print(indLetter)
			indLetter=[]
print ('found ', len(allLetters), ' of Pettigrew\'s papers!')

with open("outputs/pettigrewNERData2.csv","w",newline="") as w:
	writer=csv.writer(w)
	writer.writerows(allLetters)


TJPtext = '''My Dear Sir, 
I only received your favour of the 16th late last night, on my return from the Syro-Egyptian, or I would have answered before.  
I shall be very happy to meet Mr Wright at the Archaeological meeting this evening, the meeting of which society indeed, I have attended on the last occasion.  
Believe me, 
My dear sir, 
Yours very sincerely, 
W. Francis Ainsworth
Wednesday Morn
Dec 17th 1845'''
	
