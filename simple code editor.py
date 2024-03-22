counter = 0
code = ''
while True:
    counter += 1
    x = input(f'{counter} |')
    if x == '':
        break
    else:
        code += x + '\n'
try:
    exec(code)
except:
    pass