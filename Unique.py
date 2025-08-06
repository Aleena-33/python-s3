lst =[]
n=int(input("enter number of elements :"))
for i in range(n):
    value = int(input("enter element :"))
    lst.append(value)
unique =[]
for item in lst :
    if item not in  unique:
        unique.append(item)
print("unique element",unique) 