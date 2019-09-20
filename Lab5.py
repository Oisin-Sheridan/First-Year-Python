WordList = [e for e in input().split()]

n = len(WordList)
temp = WordList[0]
for i in range(1,n):
	temp = WordList[i]
	j = i
	while j>0:
		if WordList[j-1]<=temp:
			WordList[j]=temp
			break
		else:
			WordList[j] = WordList[j-1]
		j -= 1
	if j==0:
		WordList[0] = temp

m = 1
for k in WordList:
	print("%d. %s" %(m,k))
	m += 1
