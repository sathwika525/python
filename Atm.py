print("*"*10,"ATM machine","*"*10)
n=int(input("enter amount:"))
l=[500,200,100,50,20,10,5,2,1]
temp=0
count=0
for i in l:
    temp=n//i
    print(i,"notes to be drawn:",temp)
    n=n%i
    if(temp==1):
        count+=temp
print("total no.of single notes:",count)