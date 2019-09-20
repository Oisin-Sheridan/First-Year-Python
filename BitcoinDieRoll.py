from random import randint

try: 
	totalRolls = 0
	totalOnTime = 0
	totalRuns = 0
	for i in range(200000):
		counter = 0
		while True:
			dieRoll = randint(1,6)
			counter += 3
			if counter%600==0:
				totalOnTime += 1
				if dieRoll == 6:
					totalRuns += 1
					break

	averageRolls = totalOnTime/totalRuns
	print("Total on-time rolls: "+str(totalOnTime))
	print("Total runs: "+str(totalRuns))
	print("Average on-time rolls to get a 6: "+str(averageRolls))

except:
	averageRolls = totalOnTime/totalRuns
	print("Total on-time rolls: "+str(totalOnTime))
	print("Total runs: "+str(totalRuns))
	print("Average on-time rolls to get a 6: "+str(averageRolls))