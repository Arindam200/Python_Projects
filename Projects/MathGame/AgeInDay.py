#Age in days
#Read an integer value corresponding to a person's age in days and enter it in years, months and days

inputDays = int(input("Enter your age in days: "))

yearInDays = 365;
monthInDays = 30;

yDays = inputDays / yearInDays;
mDays = (inputDays % yearInDays) / monthInDays;
days = ((inputDays % yearInDays) % monthInDays);

print("Year(s): ",int(yDays)) 
print("Month(s)", int(mDays))
print("Day(s)", int(days))

#Output [400Days -->  1Year,  1Month, 5Days]