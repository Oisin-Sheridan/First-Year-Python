from math import radians, sin, cos, acos
import random

class Node():
	def __init__(self, N, W, time):
		self.lat = N
		self.lon = W
		self.orderTime = time
		self.vertexList = []
		self.visited = False

class Vertex():
	def __init__(self, end1, end2):
		self.node1 = end1
		self.node1.vertexList.append(self)
		self.node2 = end2
		self.node2.vertexList.append(self)
		self.distance = nodeDistance(end1, end2)
		self.minutesToTravel = (self.distance/80)*60

def nodeDistance(node1, node2):
	dist = 6371.01 * acos(sin(radians(node1.lat))*sin(radians(node2.lat)) + cos(radians(node1.lat))*cos(radians(node2.lat))*cos(radians(node1.lon) - radians(node2.lon)))
	return dist

#line1 = "1 33 The Paddocks, Oldtown Mill, Celbridge, Co. Kildare 7:12 PM 53.3473 -6.55057".split(" ")
#Node1 = Node(float(line1[-2]), float(line1[-1]), float(line1[-4].split(":")[1]))
#Node2 = Node(53.37077, -6.48279, 12)
#Vertex1 = Vertex(Node1, Node2)
#print(Vertex1.distance)

storeNode = Node(53. , -6.59192, 0)
houseList = []
fileInput = open("BurritoAddresses.txt", "r")
lines = fileInput.readlines()
for i in lines:
	lineIn = i.split(" ")
	newNode = Node(float(lineIn[-2]), float(lineIn[-1]), float((lineIn[-4].split(":")[1])))
	houseList.append(newNode)

outputFile = open("BurritoAnswers.txt", "a+")
print("What is the current best score?")
bestScore = float(input())
print("Running...")

while True:
	ticker = 0
	currentTime = 60
	numberList = []
	for j in range(100):
		numberList.append(j)
	random.shuffle(numberList)
	currentNode = storeNode
	for k in numberList:
		nextNode = houseList[k]
		distance = nodeDistance(currentNode, nextNode)
		journeyTime = (distance/80)*60
		currentTime += journeyTime
		if currentTime - nextNode.orderTime >30:
			ticker += (currentTime - nextNode.orderTime)-30
		currentNode = nextNode

	if ticker < bestScore or bestScore == 0:
		bestScore = ticker
		outputFile.write("\n" + str(ticker) + "\n")
		print("New Best: " + str(ticker))
		outputString = ""
		for l in numberList:
			outputString = outputString + str(l+1) + ","
		outputFile.write(outputString)
		print(outputString)