# wap find the given number is prime

num = input("enter a number : ")
i = 2
while(i < num):
    if(num %i ==0 ):
        break
    i =i +1
else:
    print "prime : ",num
print "Task over"
