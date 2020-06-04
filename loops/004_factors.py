# wap find the factors of a number
# 10 ===>>> 1, 2, 5, 10
N  = input("enter a number : ")
i = 1
print "factors : ",
while(i <= N):
    if(N % i ==0 ):
        print i,"   ",
    i = i +1
