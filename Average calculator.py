
import pyperclip

print('Willkommen zu duchschnits rechner:')
print('''
[1] From clipbord
[2] Input
''')
bindungszeichen = ''

while True:
    take = input()
    if take == '1':
        text = pyperclip.paste()
        break
    elif take == '2':
        text = ''
        while True:
            new = input()
            if new == '':
                break
            else:
                text += new + '\n'
        break

    else:
        bindungszeichen = take


text = text.replace('\t', ' ')

lines = text.split('\n')

word = []
numbers = []

for i in lines:
    for x,a in enumerate(i):
        if a.isspace() and i[x + 1].isnumeric():
            word.append(i[:x])
            numbers.append([int(x) for x in i[x:].split(' ') if x != ''])
            break

end = dict(zip(word, numbers))

for w, n in end.items():
    print(f'{w.strip()}{bindungszeichen} {sum(n) / len(n)}')

