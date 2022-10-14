# Convert Seconds
#Read an integer value that corresponds to a value in seconds then Convert them value to hours, minutes, and seconds
T=int(input("Enter values in seconds: "))


HH=round(T/(3600))
MM=((T%(3600))/60)
SS=(T%(60*60))%60

x="%02d:%02d:%02d"%(HH,MM,SS)
print(x)
