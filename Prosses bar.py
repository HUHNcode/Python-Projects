import time

fortschritt = 0

def Proses_bar(many, interval=1, tic=False):
    icon = '█'
    icon2 = ['[', ']']

    global fortschritt
    
    counter1 = 0
    barL = [icon2[0]]
    while many > counter1:
        counter1 += 1
        barL.append(' ')

    barL.append(icon2[1])

    if tic is False:
        counter2 = 0
        print(''.join(map(str, barL)), end='', flush=True)
        
        while counter2 < many:
            counter2 += 1
            barL[counter2] = icon
            time.sleep(interval)
            print('\r' + ''.join(map(str, barL)), end='', flush=True)

    elif tic is True:
        global fortschritt
        fortschritt += 1
        barL[fortschritt] = icon
        print('\r' + ''.join(map(str, barL)), end='', flush=True)

print('Test')

Proses_bar(50, 0.2)

