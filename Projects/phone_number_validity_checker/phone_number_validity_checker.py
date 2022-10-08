import phonenumbers
x = input("Enter number here(with the country code): ")
phone_number = phonenumbers.parse(x)
valid = phonenumbers.is_valid_number(phone_number)
possible = phonenumbers.is_possible_number(phone_number)
print(valid)
print(possible) 
