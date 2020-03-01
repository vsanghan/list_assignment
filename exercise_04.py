li = [5,7,15,42,12,45,78,25,86,68,75,214,587,5358,214,5684,524,2336,885,2563]

#exercise : 4 : sum of all individual digits from a list of integers

d = 0
for j in li:
    p = str(j)
    for i in p:
        d = d + int(i)
print (d)