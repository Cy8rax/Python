def fib(n):
    if n > -1:
        if n <= 1:
            return n
        else:
            return fib(n-1) + fib(n-2)
    if n <= -1:
        return ((-1)**(n+1)) * fib(-n)


num = int(input("enter a number: "))
print("The value of the fibonacci series for the number", num, "is: ", fib(num))