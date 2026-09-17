def factorial(n):
    if n==0:
        return 1
    print(n)
    return n*factorial(n-1)
n=int(input("enter no for factorial:"))
result=factorial(n)
print("factorial is:",result)