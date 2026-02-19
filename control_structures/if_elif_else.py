# Basic if-elif-else control

x = int(input("Type a number (x: integer): "))
y = int(input("Type another number (y: integer): "))
if x < 1:
    print('x is less than 1')
else:
    print('x is greater than or equal to 1')

if y > 3:
    print('y is greater than 3.')
elif y==3:
    print('y is equal to 3.')
else:
    print('y is less than 3. ')