print("multiplication table generator!!")
while(True):
  n=int(input("Enter a number:"))
  if(n==0):
    print("thankyou!")
    break
  else:    
    for i in range(1,11):
       print(n,"*",i,"=",n*i) 
  