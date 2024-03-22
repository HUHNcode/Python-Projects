
Datei_Name = 'Tutorial_15.txt'


Notizen_r = open(Datei_Name, 'r')
Notizen_r.seek(0)
Notizen_r_lines = Notizen_r.readlines()

counter = len(Notizen_r_lines)


def delet_node(delet_index):
    Notizen_r_lines.remove(Notizen_r_lines[delet_index - 1])

def new_node(new_Notiz):
    new_Notiz = new_Notiz + '\n'
    Notizen_r_lines.append(new_Notiz)

def change_node(cange_index):
    Notizen_r_lines[cange_index - 1] = input() + '\n'
    pass
    
def print_nodes():
    zäler = 0
    for i in Notizen_r_lines:
        zäler += 1
        print(f'[{zäler}] {i}' + '\r', end='', flush=True)


while True:
    print_nodes()
    print()
    print('IF: Neue Notiz (Press Enter)  IF: Notiz Löschen (Press x)')
    print('IF: Notiz Endern (Press c) IF: Notizen Speichern (s)')
  
    take = input()
    if take == '':
        new_node(input())
    elif take == 'x'.upper() or take == 'x':
        delet_node(int(input('delet numer: ')))
    elif take == 'c'.upper() or take == 'c':
        change_node(int(input('welche: ')))
    else:
        break

    print('----------------------------')


Notizen_w = open(Datei_Name, 'w')
Notizen_w.writelines(Notizen_r_lines)
Notizen_w.close()
