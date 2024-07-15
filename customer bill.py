list=['tea','coffee','chocolate coffee','rosemilk','horlicks']
print(list)
userinput=input("enter order:")
print(userinput)
if userinput in list:
    print("Your order is placed")
else:
    print("Sorry sir that item is not in the list,you can order other items")
while(True):
    if userinput in list:
        pass
    print("Sir do you order anything")
    break
userinput1=input("enter order:")
print(userinput1)
if userinput1 in list:
    print("Your order is placed")
else:
    print("Sorry sir that item is not in the list,you can order other items")
while(True):
    if userinput1 in list:
        pass
    print("Sir do you order anything")
    break
customer=input("Reply:")
print(customer)
print("Ok sir,Thank you")
dict={'tea':15,'coffee':20,'chocolate coffee':70,'rosemilk':50,'horlicks':25}
print(dict)
list=userinput+userinput1
print("list of order:",list)


