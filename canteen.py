
name=input("Enter your college name:")
print("🍕🥞🍔🍟🍰🍩🥚🥘🍝"*2,name,"Canteen","🍕🥞🍔🍟🍰🍩🥚🥘🍝"*2)
food_items={40:["idly","dosa","vada","poori"],
60:["manchurai","noodles","fried rice"],30:["icecream","kulfi"],
20:["maaza","puply","sprite"],
120:["chicken biryani","chicken 65"],80:"meals"}
prices_list = []
for k in food_items.keys():
    prices_list.append(k)
prices_list.sort()
while(True):
    print("Enter P: prices\t M: Menu\t F: food-items\t B: Budget ")
    option = input("ENTER YOUR OPTION: ")
    if option=='P':
        print("Prices : ")
        for k in food_items.keys():
            print(k,end=" ")
    elif option=='M':
        print("Menu : ")
        for i in prices_list:
            print("MRP: ",i," Items: ",food_items[i])
    elif option=="F":
        print("Food items available: ")
        for v in food_items.values():
            print(v)
    elif option=="B":
        budget = int(input("Enter your budget: "))
        for i in prices_list:
            if i<=budget:
                print("MRP : ",i," items :",food_items[i])
    else:
        print("Thank YOU!!!")
        break