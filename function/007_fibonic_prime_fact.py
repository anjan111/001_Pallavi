# waf for fibonic
# waf for prime
# wap for factorial
def fibonic(num =None):
    if(num == None):
        print "please provide the agumnent"
    elif(not(isinstance(num,int))):
        print"you should provide int argument"
    elif(num <= 0):
        print "Please provide more than 0 number "
    else:
        a = 1
        b = 1
        for i in range(num):
            print a,"  ",
            c = a+b
            a = b
            b =c
        
def isprime(num =None):
    pass
def factorial(num =None):
    pass
def main():
    num = input("enter num : ")
    print "fibonic elements  "
    fibonic(num)
    print num, "is prime " ,isprime(num)
    print"factorial of ",num," is ",factorial(num)
if __name__ =="__main__":
    main()
