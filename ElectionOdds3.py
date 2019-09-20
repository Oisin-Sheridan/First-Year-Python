from random import randint

totalRuns = int(input("How many times should this run? "))
totalTrue = 0
# i.e. where the three dragons(Sean Gallagher, Gavin Duffy and Peter Casey) come last
for i in range(0,totalRuns):
	HigginsOdds = 962 #96.2%
	GallagherOdds = 15 #1.5%
	NiRiadaOdds = 12 #1.2%
	CaseyOdds = 91 #9.1%
	DuffyOdds = 2 #0.2%
	FreemanOdds = 4 #0.4%
	# All odds are from implied percentage chances, multiplied by ten for convenience
	places = [0,0,0,0,0,0]
	for i in range(0,6):
		tempOdds = HigginsOdds+GallagherOdds+NiRiadaOdds+CaseyOdds+DuffyOdds+FreemanOdds
		sim1 = randint(1,tempOdds)
		if sim1<=HigginsOdds:  #Check if Higgins wins
			places[i] = 0
			HigginsOdds = 0
		elif sim1<=GallagherOdds+HigginsOdds:  #Check if Gallagher wins
			places[i] = 1
			GallagherOdds = 0
		elif sim1<=NiRiadaOdds+GallagherOdds+HigginsOdds:  #Check if NiRiada wins
			places[i] = 0
			NiRiadaOdds = 0
		elif sim1<=CaseyOdds+NiRiadaOdds+GallagherOdds+HigginsOdds:  #Check if Casey wins
			places[i] = 1
			CaseyOdds = 0
		elif sim1<=DuffyOdds+CaseyOdds+NiRiadaOdds+GallagherOdds+HigginsOdds:  #Check if Duffy wins
			places[i] = 1
			DuffyOdds = 0
		elif sim1<= FreemanOdds+DuffyOdds+CaseyOdds+NiRiadaOdds+GallagherOdds+HigginsOdds:  #Check if Freeman wins
			places[i] = 0
			FreemanOdds = 0
	print(places)
	if places[3]+places[4]+places[5]==3:
		totalTrue += 1

print("Out of %d simulations, the three dragons came last in %d of them." %(totalRuns, totalTrue))
DragonsLoseChance = float((totalTrue/totalRuns)*100)
print("Thus, the odds of this happening are "+str(DragonsLoseChance)+" percent")