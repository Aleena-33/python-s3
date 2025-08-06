n=int (input("enter the starting number (n):"))
m=int (input("enter the ending number(m):"))
squares={x**2 for x in range(n,m+1) if x %2 ==0}
print("Set of even numbers between {m} and {n}:")
print(squares)



