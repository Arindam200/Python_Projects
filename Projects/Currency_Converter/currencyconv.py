with open('currency.txt') as f:
    lines=f.readlines()

currencyDic={}
for line in lines:
    parsed=line.split("\t")
    currencyDic[parsed[0]]=parsed[1]

amount=int(input("Enter amount in INR:\n"))
print("Enter the name of currency you want to convert this amount to? Available options are:\n")
[print(item) for item in currencyDic.keys()]
currency = input("Please enter one of these values:\n")
print(f'{amount} INR is equal to {amount * float(currencyDic[currency])} {currency}')
