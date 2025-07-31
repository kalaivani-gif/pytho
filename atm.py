print ("select the services you want:")
print("1.withdraw")
print("2.deposit\n3.savings\n4.balance")
service=int(input("pls select:"))
pin=1234
if service==1:
    print('withdraw')
    amount=int(input("Enter a amount:"))
    pin=int(input("Enter a secret pin"))
    if pin==PIN:
        print('collect your amount')
    else:
        print("incorrect pin")
elif service==2:
    print('deposit')
elif service==3:
    print('savings')
elif service==4:
    print('balance')
else:
    print('kindly select the above services')
