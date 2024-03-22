import random

from German5000words import words
Hitt_counter = 0
Leben  = int(input('mir wie vilen lebne spilen?: '))

def random_word():
    global word

    word = random.choice(words)


    global len_word
    len_word = len(word)

random_word()

Word_Lerr = ['_ ' ] * len_word
Word_Liste = list(word)
#print(f'{Word_Liste}         ({len_word})')

print(''.join(Word_Lerr) + f'   //   ({len_word})')

#print(Word_Lerr)




def Auswahl():
    global Hitt_counter
    while Hitt_counter < Leben:


        if '_ ' not in Word_Lerr:
            print('u won!!!')
            break

        
        coice = input('Tacke ur latter: ')
        
        print(coice.upper())
        if coice in Word_Liste or coice.upper() in Word_Liste:
            print('letter ist in der liste')
            for i in range(0, len(Word_Liste)):
                if Word_Liste[i] == coice.lower() or Word_Liste[i] == coice.upper():
                    if Word_Liste[i] == coice.upper():
                        Word_Lerr[i] = coice.upper()

                    elif Word_Liste[i] == coice.lower():
                        Word_Lerr[i] = coice.lower()
                    



            print(''.join(Word_Lerr))

        

        else:
            print('Falsch? you lost one live')
            Hitt_counter += 1


        
        print(f'du hast insgesamt {Hitt_counter} Leben verlorne')


    if Hitt_counter == Leben:
        print('u lost :(')

Auswahl()
print(word)