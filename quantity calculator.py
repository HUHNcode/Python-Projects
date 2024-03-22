import random

# quantity calculator
trennzeichen = ' '
text = '''
22 76 47 26 27 82 79 29 2 16 100 80 19 1 34 58 45 67 2 36 25 13 15 73 12 81 2 63 73 81 37 50 72 74 12 23 21 25 13 79 3.3 4 6 6 2 17 38 62 95 71 8
'''

text = ''.join([str(random.randint(0, 1000)) + ' ' for _ in range(random.randint(1, 100000))])


text = text.replace('\n', '')
text = text.split(trennzeichen)
Numbers = []
Floats = []



for i in text:
    if i.isnumeric():
        Numbers.append(int(i))
    elif '.' in i:
        Numbers.append(float(i))

def analysis():
    my_dic = {}
    for i in Numbers:
        if Numbers.count(i) >= 2:
            my_dic[i] = Numbers.count(i)
    my_dic = dict(sorted(my_dic.items(), key=lambda item: item[0], ))
    print(my_dic)
    for k,v in my_dic.items():
        print(f'Die {k} kommt {v} mal for')




def print_quantity(list):
    for i in list:
        print(f'{i} ', end='')

def add():
    return sum(Numbers)

def multiply():
    y = 1
    for i in Numbers:
        y *= i
    return y

def average():
    return add() / len(Numbers)



print(f'Adirt ist das: {add()}')
print(f'Multiplizirt ist das: {multiply()}')
print(f'Der Duchschnit ist: {average()}')
print('--------------------\nANALYSE:')
# analysis()
# Numbers.sort()
# print_quantity(Numbers)