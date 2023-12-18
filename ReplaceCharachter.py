str=input('Enter the character: ')
curr_char=input('enter the current character')
new_char=input('enter the new character')
if(new_char==''):
    print('you have entered an empty string')
else:
    print('the new string is---',str.replace(curr_char,new_char))    