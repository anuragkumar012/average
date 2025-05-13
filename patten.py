n = 5
for i in range (1, n):
    print(" "*(n-i)+"* "*i)
for i in range (n):
    print(" "*(i),end="")
    print("* "*(n-i),end="")
    print()