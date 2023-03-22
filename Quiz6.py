#Quiz 6 Vini Paradiso
#Problem 1 Ctrl + C to stop
n=1
sum=0
while n>0:
    print("n is greater than 0")

#Problem 2
i=2
sum=0
while i < 12:
    sum += i
    i += 2
print("The sum of all positive even numbers less than 12 is", sum)

#Problem 3
def sum_n(n):
    while 1<=n:
        sum = 0
        total = 0
        sum += n
        n = n-1
        total = sum + n
        print(total)
print(sum_n(5))
#Problem 4
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        result=fib(x-1)+fib(x-2)
        return result
print (fib(5))
print (fib(-3))
