# Written in 2015
# by Sena Temuçin

def isVowel(ch):
	if ch in 'aiueoIOU':
		return True
	
def hyphenate(word):
	#Creating list
	hyphenated=list(word)
	h=0
	i=0
	#Initiating The Algorithm 
	while i<(len(word)+h):
		if i==len(word)-1:
			l1=''.join(hyphenated)
			return l1.split('-')
		if isVowel(word[i]):
			i+=1
			c=5
			while c==5:
				if isVowel(word[i]):
					hyphenated.insert((i+h),"-")
					h+=1
					c=0
				else:
					if i==len(word)-1:
						l1=''.join(hyphenated)
						return l1.split('-')
					else:
						i+=1
						if isVowel(word[i]):
							hyphenated.insert((i+h-1),"-")
							c=0
							h+=1
		else:
			if i==len(word)-1:
				l1=''.join(hyphenated)
				return l1.split("-")
			else:
				i+=1
	#Algorithm Successfully Completed
	#Final Steps
	l1=''.join(hyphenated)
	return l1.split('-')
	
def lis(li):
	syllables=[]
	for word in li:
		syllables=syllables+hyphenate(word)
	return syllables
def takeLine():
	s=raw_input()
	if s[-1]!='.':
		s=s+' '
	return s
def execute():
	#Input Phase
	s=raw_input()
	nm=s.split(" ")
	n=int(nm[0])
	m=int(nm[1])
	#Maximum word and character numbers successfully taken
	words=[]
	s=takeLine()
	w=""
	for i in range(len(s)):
		if s[i]==" ":
			words=words+[w]
			words=words+[" "]
			w=""
		elif s[i]==".":
			words=words+[w]
			words=words+["."]
			w=""
		elif s[i]!="\r":
			w=w+s[i]
	allWords=[]
	while (s!='=\r ') and (s!='= '):
		allWords=allWords+words
		s=takeLine()
		for i in range(len(s)):
			if s[i]==" " and w!="":
				words=words+[w]
				words=words+[" "]
				w=""
			elif s[i]=="."and w!="":
				words=words+[w]
				words=words+["."]
				w=""
			elif s[i]!="\r":
				w=w+s[i]
	#Input Phase is over
	finalList=[' ']+lis(words[:-2])
	#All words and spaces and dots are in their respective positions
	#Getting Statistics
	stats={}
	dic={}
	checkList=[]
	for i in range(len(finalList)-1):
		if finalList[i] not in stats:
			stats[finalList[i]]={finalList[i+1]:1}
			checkList.append(finalList[i])
		elif finalList[i+1] in stats[finalList[i]]:
			stats[finalList[i]][finalList[i+1]]+=1
		else:
			stats[finalList[i]][finalList[i+1]]=1
	for syl in checkList:
		dic[syl]={}
		dic[syl][0]=max(stats[syl], key=stats[syl].get)
		del stats[syl][max(stats[syl], key=stats[syl].get)]
		if len(stats[syl])>=1:
			dic[syl][1]=max(stats[syl], key=stats[syl].get)
		if len(stats[syl])>=2:
			dic[syl][2]=max(stats[syl], key=stats[syl].get)
		if len(stats[syl])>=3:
			dic[syl][3]=max(stats[syl], key=stats[syl].get)
		if len(stats[syl])>=4:
			dic[syl][4]=max(stats[syl], key=stats[syl].get)
	#STATISTICS ARE ALL GREEN
	#GENERATING RANDOM TEXT
	from random import choice
	text=''
	wordCount=0
	startSyl=list(stats[' '])+list(stats['.'])
	while len(text)<=m and wordCount<n:
		if text=='':
			currentSyl=choice(startSyl)
			text=text+currentSyl
			wordCount+=1
		else:
			if currentSyl!= '.':
				currentSyl=choice(dic[currentSyl].values())
				text=text+currentSyl
				if currentSyl!=' ':
					wordCount+=1
			else:
				currentSyl=choice(startSyl)
				text=text+currentSyl
	return text + '.'
		
	
print execute()

