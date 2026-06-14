total=0.0
#enter kwh used
kwh=int(input("Enter the KW hours used:"))
if (kwh<=1000):
    total=kwh*0.07633
else:
    total = 1000 * 0.07633
    kwh-=1000
    total=total+(kwh*0.09259)

print("Amount owed is $",total)