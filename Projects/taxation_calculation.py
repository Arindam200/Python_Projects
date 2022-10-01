#Parnani Panda
active=True
while active:
    message=input("Hey")
    if message.lower()=="quit":
        active=False
    else:
        name=input("Enter your name:")
        salary=int(input("enter your salary :"))

        if(salary<=250000):
            print("no tax for you")
        elif((salary>2500000) and(salary<=500000)):
            tax=salary/20
            print("your tax slab is 5% and your tax is",tax)
        elif((salary>500000)and (salary<=750000)):
            tax=salary/10
            print("your tax slab is 10% and your tax is ",tax)
        elif((salary>750000)and (salary<=1000000)):
            tax=15*salary/100
            print("your tax slab is 15% and your tax is ",tax)
        else:
            tax=salary/5
            print("your tax slab is 20% and your tax is ",tax)
        
     