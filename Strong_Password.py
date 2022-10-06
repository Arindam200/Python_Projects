import string , random as rd

print('******************* :) ------Make Your Deivces Free From The Hackers & The Unauthorized Persons------ (:*********************')


no_low_char=int(input('Enter The No.Of Lower_Characters You Want In Your Password       :  '))

no_upper_char=int(input('Enter The No.Of Upper_Characters You Want In Your Password     :  '))

no_special_char=int(input('Enter The No.Of Special_Charecters You Want In Your Password :  '))

lower_case=[]

upper_case=[]

special_case=['~','`','!','@','#','$','%','^','&','*','.','/','|','_','+','-','=',':',';',',','?']

password_list=[]

password=''

for letter in string.ascii_lowercase:      #By Using This For Loop We Can Access All LowerCase Alphabets  
    lower_case.append(letter)

for letter in string.ascii_uppercase:      #By Using This For Loop We Can Access All UpperCase Alphabets 
   upper_case.append(letter)

for i in range(0,no_low_char):
    temp1=rd.choice(lower_case)
    password += temp1
    lower_case.remove(temp1)               #This Line Is The Beauty Of The Code It Resists The Repetion Of The Chacaters

for i in range(0,no_upper_char):
    temp2=rd.choice(upper_case)
    password += temp2
    upper_case.remove(temp2)               #This Line Is The Beauty Of The Code It Resists The Repetion Of The Chacaters

for i in range(0,no_special_char):
    temp3=rd.choice(special_case)
    password += temp3
    special_case.remove(temp3)             #This Line Is The Beauty Of The Code It Resists The Repetion Of The Chacaters  

password_list=list(password)               #We Cannot Shuffle The String That's Why We Are Converting This To List Data Structure

rd.shuffle(password_list)

sample=''

for letters in password_list:

    sample+=letters 

print(f'Now You Have Such A Strong Password Password In The Universe <3 :  {sample}')
    
