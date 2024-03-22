import random


take = input('automatically (a) or yourself (y)?').upper()

how_many = 4

your_input = []
random_numbers = []
for _ in range(how_many):
    random_numbers.append(random.randint(1, 49))

counter = 0

def input_mine():
    # input ur 6 random numbers from 1 to 49:

    global your_input
    for _ in range(how_many):
            while True:
                try:
                    your_input_num = int(input())
                    if your_input_num in range(1,50):
                        your_input.append(your_input_num)
                        break
                    else:
                        print('in range 1 - 49')
                        continue
                except ValueError:
                    print('input only numbers!')
                    continue




# genarate  6 random numbers from 1 to 49:
                


'''                
if take == 'A':
    all_combinations = list(range(1, 50))
    random.shuffle(all_combinations)

    while True:
        counter += 1
        random_numbers_now = all_combinations[:how_many]

        if random_numbers == random_numbers_now:
            print(f'u got it. {counter} trys')
            print(random_numbers)
            break
        else:
            all_combinations = all_combinations[how_many:]
            continue

'''

if take == 'A':
    random_numbers_now = []
    while True:
        counter += 1
        random_numbers_now = []
        for _ in range(how_many):
            
            random_numbers_now.append(random.randint(1, 49))

        if random_numbers == random_numbers_now:
            print(f'u got it. {counter} trys')
            print(random_numbers)
            break
        else:
            continue
        

elif take == 'Y':
    
    while True:
        counter += 1
        your_input = []
        input_mine()

        if random_numbers == your_input:
            print(f'u got it. {counter} trys')
            print(random_numbers)
            break
        else:
            continue
        



          
