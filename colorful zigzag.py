import time
import numpy
from termcolor import colored
rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta'] * 5000

try:
    print(colored(' ', 'red'))
except:
    print('you nead to install termcolor. pip install termcolor')
numpy.abs(-1)
bakwards = False
counter = 0
colorswich = 0
while True:
    time.sleep(0.05)
    if bakwards:
        counter -= 1
    else:
        counter += 1

    if counter > 20:
        bakwards = True
        colorswich += 1
    elif counter == 0:
        bakwards = False
    
    
    print('     ' * 18 + (' ' * counter * 4 + colored('██████     █     ██████',rainbow_colors[colorswich])))


