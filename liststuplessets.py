list=[1,2,4,"hello"]
for i in list:
    print(i, list.index(i))

list.append("apple")
for i in list:
    print(i)

print("\n")
list.insert(1,"mango")
for i in list:
    print(i)

