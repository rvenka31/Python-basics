import math

print ("-"*11)

strg = "Sundevils"
print("position and character")
print(strg)
for i in range(len(strg)):
    print (i, strg[i])

print ("-"*11)

mylist = [10, 20, 30]

print("Contents in list using range function")
# method 1
for i in range (len(mylist)):
    print (i, mylist[i])
print("Contents in list using value")
# method 2
for l in mylist:
    print (l)

print ("-"*11)

mylst1 = [10, 20, 30]
mylst2 = [100, 200, 300]

# method 1
print("Contents in list using range function")

for i in range (len(mylst1)):
    print (i, mylst1[i], mylst2[i])

print("Contents in list using zip function")

# method 2
for l1, l2 in zip (mylst1, mylst2):
    print (l1, l2)

print ("-"*11)

mydictionary = {'A':100, 'B':200, 'C':300}

print("Contents in dictionaries using keys")
# variation 1
for k in sorted(mydictionary.keys()):
    print (k, mydictionary[k])

# variation 2
for k in reversed(sorted(mydictionary.keys())):
    print (k, mydictionary[k])

print ("-"*11)

sumi = 0
print("Sum of iteration using for loop")
for i in range (5):
    sumi = sumi + i
    print (i, sumi)
    
print (sumi)

print ("-"*11)

P = [10, 20, 30]

sumP = 0
print("Sum of list")

for i in range (3):
    sumP = sumP + P[i]
    print (i, P[i], sumP)
    
print (sumP)

print ("-"*11)

P = [1, 2, 3]
Q = [10, 20, 30]

sumP = 0
sumQ = 0

for i in range (3):
    sumP = sumP + P[i]
    sumQ = sumQ + Q[i]

print ("P =", P)
print ("Q =", Q)
print ("sumP =", sumP)
print ("sumQ =", sumQ)

print ("-"*11)

P = [1, 2, 3]
Q = [10, 20, 30]

manhattan = 0
print("Manhattan distance using range function")
for i in range (3):
    manhattan = (manhattan + 
                math.fabs(P[i] - Q[i]))

print ("P =", P)
print ("Q =", Q)
print ("Manhattan Distance =", round(manhattan,2))

print ("-"*11)



