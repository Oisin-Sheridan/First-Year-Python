def findLowerPrime(x):
	while True:
		i = 2
		notPrime = False
		while i<x:
			if x%i==0:
				notPrime = True
			i += 1
		if notPrime == False:
			return x
		x -= 1

def findHigherPrime(y):
	while True:
		j = 2
		notPrime = False
		while j<y:
			if y%j==0:
				notPrime = True
			j += 1
		if notPrime == False:
			return y
		y += 1

N = int(input())

if N==2:
	lowerPrime=2
else:
	lowerPrime = findLowerPrime(N)

higherPrime = findHigherPrime(N+1)

print(higherPrime-lowerPrime)