alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# The logo is the actraction!

def encrypt(plane_text, shift_amount): #this is the funtion for the encryption of the data
    
  cipher_text = ''  
    
  for letter in plane_text:
      
    position = alphabet.index(letter)
  
    new_position = position + shift_amount
  
    if new_position >=25:  # it is the beauty of the code & main logic if we want to encrypt the last alphabet letter it give us INDEX ERROR but this if condtion rectify that issue
        
       new_position = new_position  - 26
      
    new_letter = alphabet[new_position]
      
    cipher_text +=new_letter
      
  print(f'You New encode : {cipher_text}')

def decrypt(cipher_text , shift_amount):
  
  plane_text = ''  
  
  for letter in cipher_text:

    position = alphabet.index(letter)

    new_position = position - shift_amount

    if new_position < 0:#it is the beauty of the code &  2nd main logic if we want to decrypt the starting  alphabet letter it give us same INDEX ERROR but this if condtion rectify that iss

        new_position = new_position + 26 
          
    new_letter = alphabet[new_position]
    
    plane_text +=new_letter
    
  print(f'You New encoded Data : {plane_text}')

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()#this converts everything into lowercase letters

text = input("Type your message:\n").lower() #like direction it also converts everything into lower letters
  
shift = int(input("Type the shift number:\n"))

if direction == 'encode' :

  encrypt(plane_text=text,shift_amount=shift)
  
elif direction == 'decode':
  
  decrypt(cipher_text = text,shift_amount = shift) 
  
  
