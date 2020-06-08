print('Welcome to the Python Calculator')
print('By bestcreatorT')
x = int(input('First number: '))
y = input('Operation(+, -, *, /): ')
z = int(input('Second number: '))
if y == '+':
  print(float(x+z))
elif y == '-':
  print(float(x-z))
elif y == '*':
  print(float(x*z))
elif y == '/':
  print(float(x/z))
else:
  print('Syntax Error')
