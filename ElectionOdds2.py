from random import randint
''' Indexes:
Michael D Higgins = 0
Sean Gallagher = 1
Liadh Ni Riada = 2
Peter Casey = 3
Gavin Duffy = 4
Joan Freeman = 5
'''
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
	#         = HigginsOdds+GallagherOdds+NiRiadaOdds+CaseyOdds+DuffyOdds+FreemanOdds
	# All odds are from implied percentage chances, multiplied by ten for convenience
	places = [-1,-1,-1,-1,-1,-1]
	for i in range(0,6):
		tempOdds = HigginsOdds+GallagherOdds+NiRiadaOdds+CaseyOdds+DuffyOdds+FreemanOdds
		sim1 = randint(1,tempOdds)
		if sim1<=HigginsOdds:
			places[i] = 0
			HigginsOdds = 0
		elif sim1<=GallagherOdds+HigginsOdds:
			places[i] = 1
			GallagherOdds = 0
		elif sim1<=NiRiadaOdds+GallagherOdds+HigginsOdds:
			places[i] = 2
			NiRiadaOdds = 0
		elif sim1<=CaseyOdds+NiRiadaOdds+GallagherOdds+HigginsOdds:
			places[i] = 3
			CaseyOdds = 0
		elif sim1<=DuffyOdds+CaseyOdds+NiRiadaOdds+GallagherOdds+HigginsOdds:
			places[i] = 4
			DuffyOdds = 0
		elif sim1<= FreemanOdds+DuffyOdds+CaseyOdds+NiRiadaOdds+GallagherOdds+HigginsOdds:
			places[i] = 5
			FreemanOdds = 0
	print(places)
	if places[3]+places[4]+places[5]==8:
		totalTrue += 1

print("Out of %d simulations, the three dragons came last in %d of them." %(totalRuns, totalTrue))
DragonsLoseChance = float((totalTrue/totalRuns)*100)
print("Thus, the odds of this happening are "+str(DragonsLoseChance)+" percent")