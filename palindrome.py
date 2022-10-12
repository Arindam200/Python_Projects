n = input()
n = int(n)
copy_n=n
result = 0
 
while(n!=0):
    digit = n%10
    result = result*10 + digit
    n=int(n/10)
 
print("Result is: ", result)
if(result==copy_n):
    print("Palindrome!")
else:
    print("Not a Palindrome!")