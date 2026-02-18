# Simple data output

word = "mathematics"
number_1 = 10
number_2 = 3.5

print("word: " + word)
print('first number: %s' %(number_1))
print('numbers: %s, %.8f ' %(number_1, number_2))
print('first number:' + str(number_1), end=' . ')
print('second number: ' + str(number_2))
print(f'numbers: {number_1} , {number_2:.8f}')
print('numbers: ', number_1, number_2, sep=' *** ')