import random
import csv
#generate random number
def generateRandomnumbers():
    return random.randint(1,10)

#create 10 numbers
numbers=[generateRandomnumbers() for i in range(10)]

#write csv file
with open("randomdata.csv",mode="w", newline="") as file:
    writer=csv.writer(file)
    for number in numbers:
        writer.writerow([number])