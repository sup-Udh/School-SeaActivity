veggies={"tomato":100,"potato":200,"onion":300,"carrot":400,"cabbage":500}
askForVeggis = int(input("enter the number of items you want to buy:"))
bill=0
for i in range(askForVeggis):
    item = input("enter the item you want to buy:")
    if item in veggies:
        bill+=veggies[item]    
    else:
        print(f'{item} is not available')
if bill>2000:print(f'Total Ammount : {bill*0.9}')
elif bill>1500:print(f'Total Ammount : {bill*0.92}')
elif bill>1000:print(f'Total Ammount : {bill*0.95}')
else:print(f'Total Ammount : {bill}')