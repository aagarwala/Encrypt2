#Anirudh Agarwala
#Encrypts all ASCII values from 32-126 by shifting them by give amount from user
#First asks the user to input the string, then shift the amount by a given value
#If the shifting causes the new ASCII value to go out of range, it wraps around starting at value 32


userstring= raw_input('Please enter a string: ')

shiftAmount=int(raw_input('Enter a number between 1 and 94: '))

#while the input is invalid
while(shiftAmount < 1 or shiftAmount > 94):
    #display error message
    print 'Shift amount must be between 1 and 94'
    #ask for a number between 1 and 25
    shiftAmount=raw_input('Enter a number between 1 and 94: ')

    #the input is valid
    shiftAmount=int(shiftAmount)#convert to a number

cipherText=""
for char in userstring: #for each character in userstring
    charNum=ord(char)#get the character's ascii value
    newcharPOS=charNum + shiftAmount #shift the character over by shift amount
    if(newcharPOS > 126): #if number goes out of ASCII range of lowercase alphabet subtracts 26 to wrap around the alphabet
       newcharPOS -= 95
    shiftedchar=chr(newcharPOS)#convert back into a character
    cipherText += shiftedchar
#endfor
print cipherText
