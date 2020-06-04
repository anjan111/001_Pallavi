# wap find the factorial of number and find the given number is prime
num = input("enter num : ") # global variable
def factorial():
    fact = 1
    for e in range(1,num+1):
        fact = fact *e
    else:
        print "factorial of ",num,' is ',fact
def isprime():
    f_c = 0
    for e in range(1, num+1):
        if(num % e == 0):
            f_c = f_c +1
    if(f_c == 2):
        print num, " is prime "
    else:
        print num," is not prime"

factorial()
isprime()
