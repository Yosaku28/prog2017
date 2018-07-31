import csv
import random
f = open('rand.csv', 'w',newline='')    #newlineが無いと一行ごとに空行ができる
writer = csv.writer(f)

val = 0
for num in range(1100000):
    csvlist = []
    val = num
    for loop in range(0,10):
        val = random.randint(0,100)
        csvlist.append(val)
    writer.writerow(csvlist)

f.close()