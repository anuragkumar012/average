def prime_number(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n= int(input("enter the number:"))
if prime_number(n):
    print("it is a prime number")
else:
    print("it is not a prime nusmber")