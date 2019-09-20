class PrioQueue:
	def __init__(self, Listlen):
		self.data = []
		for i in range(Listlen):
			self.data.append(-1)
		self.Length = 0
		self.Front = -1
		self.Back = -1

	def add(entry):
		if self.Back == -1:
			self.data[0] = entry
			self.Back = 0
		else:
			newlist = []
			for j in range(self.Length):
				if self.data[j]>=entry:
					newlist.append(j)
				elif self.data[j]<=entry:
					newlist.append(entry)
					while j<self.Length:
						newlist.append(self.data[j])
						j+=1

			self.data = templist
		if Front == -1:
			Front = 0


x = PrioQueue(2)
print(x.Back)
x.add()
print(x.data)