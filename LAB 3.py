# lewis muthomi
# 1250 01
# Thu sep 8 2022
# lab 3


# This program will let you raise any integer to any integer power


# User greeting
print('Welcome to integer and exponent program')
print('Remember to use whole numbers only.')
print()

   
# Take user input.
base = input ('Please enter the base number : ')
power = int(input ('What is power of ' + base  + ': '))
print()


# Convert string input to float.
base = int(base)
answer = base ** power


# Display and format results.
print(base, 'to the power of', power , 'is',format(answer, ',.0f'))
print()

 
# exits message
print('Thank you for using the power calculator.')
print('Have a nice day!')

