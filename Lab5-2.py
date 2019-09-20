N = int(input())
WordList = []
for m in range(N):
	line = input()
	WordList.append(line)

n = len(WordList)
temp = WordList[0]
for i in range(1,n):
	temp = WordList[i]
	j = i
	while j>0:
		if len(WordList[j-1])<len(temp):
			WordList[j]=temp
			break
		elif len(WordList[j-1])==len(temp) and WordList[j-1].lower()<=temp.lower():
			WordList[j]=temp
			break
		else:
			WordList[j] = WordList[j-1]
		j -= 1
	if j==0:
		WordList[0] = temp

answer = WordList[0]
k = 1
while k<len(WordList):
	answer = answer+" "+WordList[k]
	k+=1
print(answer)
