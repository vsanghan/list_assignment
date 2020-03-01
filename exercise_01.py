li = [5,7,15,42,12,45,78,25,86,68,75,214,587,5358,214,5684,524,2336,885,2563]

#exercise : 1 : print all integers which are divisible by 5 or 7 from a list of integers.

op = []

for i in li:
    if i%5==0 or i%7==0:
        op.append(i)
print (op)