import math

pen = input("How meny pennies do you have?  ")
pen = float(pen)

dolp = 100
quap = 25
dimp = 10
nikp = 5

dol = math.floor(pen / dolp)
print("You have", dol, "dollars")

change1 = pen % dolp

qua = math.floor(change1 / quap)
print("You have", qua, "Quarters")

change2 = change1 % quap

dim = math.floor(change2 / dimp)
print("You have", dim, "dimes")
#Test

change3 = change2 % dimp

nik = math.floor(change3 / nikp)
print("You have", nik, "Nickels")

finpen = math.floor(change3 % nikp)
print("You have", finpen, "Pennies")