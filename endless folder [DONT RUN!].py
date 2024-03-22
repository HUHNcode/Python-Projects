import os
import string


os.chdir(r'/media/timon/Daten/Code laufzeit umgebung/01')
og_dir = os.getcwd()
# if not os.path.exists('folder1'):
#     os.mkdir('folder1')

alphabet_list = list(string.ascii_uppercase)
def creat(new_path=os.getcwd()):
    #os.chdir(new_path)
    for i in alphabet_list:
        os.mkdir(i)
counter = 0
def make():
    for i in alphabet_list:
        x = os.getcwd()
        os.chdir(os.getcwd() + '/' + i)
        creat()
        os.chdir(x)

creat()
for i in alphabet_list:
    
    os.chdir(og_dir + '/' + i)
    sec_dir = os.getcwd()
    creat()

    make()
    for i in alphabet_list:
        os.chdir(os.getcwd() + '/' + i)
        make()

    
    os.chdir(og_dir)




'''
def creat(new_path=os.getcwd()):
    #os.chdir(new_path)
    for i in alphabet_list:
        os.mkdir(i)
creat()
main_dir = os.getcwd()

for i in alphabet_list:
    os.chdir(main_dir + f'/{i}')
    creat()
    
'''