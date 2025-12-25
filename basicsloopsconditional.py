x = [2, 8, 512] 
for i  in x:
    print(i)

n = " Shruti "
print(n.strip())

#taking input from the user
name= input("Enter your name: ")
print(f"your name is : {name}")

for a in range(1,10,2):
    print(a)

print("\n")

j=0
while j<10:
    j+=1
    print(j)

print("\n")
age = 19
if age > 18: print("Eligible to Vote.")

print("\n")
a=10
if (a>18):
    print("eligible")
else:
    print("Not eligible")

print("\n")
curage=70
if (curage<=12):
    print("child")
elif (curage<=19 and curage>12):
    print("teenage")
elif (curage>19 and curage<50):
    print("youngster")
else: print("old")

# Learning : there is a difference between bitwise operator "&" , logical operator "and" 
# When you write curage > 19 & curage < 50, Python executes it in this order:
# It calculates (19 & curage) first (bitwise AND).
# Then it checks if curage is greater than that result.
# Then it checks if the final result is less than 50.
# Because of this mathematical "mess," the elif conditions are returning True even when the age is 70, so it never reaches the else block.