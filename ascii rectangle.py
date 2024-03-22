import pyperclip
dimensions = [20, 20]
output = ''
print('██' * dimensions[0])
output += '█' * dimensions[0] + '\n'
for _ in range(dimensions[1] - 2):
    print('█' + (' ' * (dimensions[0] * 2 - 2)) + '█')
    output += '█' + (' ' * (dimensions[0] - 2)) + '█' + '\n'

print('██' * dimensions[0])
output += '█' * dimensions[0]
pyperclip.copy(output)
