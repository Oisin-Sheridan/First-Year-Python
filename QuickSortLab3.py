
def partitionIt(left, right, listIn, pivot):
	movingUp = left
	movingDown = right-1
	
	
	while movingUp<movingDown and movingDown>=0:
		upData = listIn[movingUp]
		upDataAhead = False
		if max(upData)>max(pivot) or (max(upData)==max(pivot) and upData>pivot):
			upDataAhead = True


		downData = listIn[movingDown]
		downDataBehind = False
		if max(downData)<max(pivot) or (max(downData)==max(pivot) and downData<pivot):
			downDataBehind = True

		if upDataAhead and downDataBehind:
			listIn[movingUp] = downData
			listIn[movingDown] = upData

		if upDataAhead==False:
			movingUp += 1
		if downDataBehind == False:
			movingDown -= 1

	adjust = 0
	if max(listIn[movingUp])<max(pivot) or (max(listIn[movingUp])==max(pivot) and listIn[movingUp]<pivot):
		adjust = 1


	temp = listIn[movingUp+adjust]
	listIn[movingUp + adjust] = listIn[right]
def partitionIt(left, right, listIn, pivot):
	movingUp = left
	movingDown = right-1
	
	
	while movingUp<movingDown and movingDown>=0:
		upData = listIn[movingUp]
		upDataAhead = False
		if max(upData)>max(pivot) or (max(upData)==max(pivot) and upData>pivot):
			upDataAhead = True


		downData = listIn[movingDown]
		downDataBehind = False
		if max(downData)<max(pivot) or (max(downData)==max(pivot) and downData<pivot):
			downDataBehind = True

		if upDataAhead and downDataBehind:
			listIn[movingUp] = downData
			listIn[movingDown] = upData

		if upDataAhead==False:
			movingUp += 1
		if downDataBehind == False:
			movingDown -= 1

	adjust = 0
	if max(listIn[movingUp])<max(pivot) or (max(listIn[movingUp])==max(pivot) and listIn[movingUp]<pivot):
		adjust = 1


	temp = listIn[movingUp+adjust]
	listIn[movingUp + adjust] = listIn[right]
	listIn[right] = temp
	return listIn, movingUp+adjust


def quicksort(left, right, listIn):
	if left>=right:
		return listIn

	pivot = listIn[right]

	listIn, partition = partitionIt(left, right, listIn, pivot)
	listIn = quicksort(left, partition-1, listIn)
	listIn = quicksort(partition+1, right, listIn)
	return(listIn)


N = int(input())
inputList = []
for i in range(N):
	inputList.append(input())

answerList = quicksort(0, len(inputList)-1, inputList)
for j in answerList:
	print(j)
	listIn[right] = temp
	return listIn, movingUp+adjust


def quicksort(left, right, listIn):
	if left>=right:
		return listIn

	pivot = listIn[right]

	listIn, partition = partitionIt(left, right, listIn, pivot)
	listIn = quicksort(left, partition-1, listIn)
	listIn = quicksort(partition+1, right, listIn)
	return(listIn)


N = int(input())
inputList = []
for i in range(N):
	inputList.append(input())

answerList = quicksort(0, len(inputList)-1, inputList)
for j in answerList:
	print(j)