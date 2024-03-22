import random
import time
user_p = 0
computer_p = 0
matchfield = ['_'] * 120

def prind_fild():
    print(f'''

| {matchfield[100]} | {matchfield[101]} | {matchfield[102]} | {matchfield[103]} | {matchfield[104]} | {matchfield[105]} | {matchfield[106]} | {matchfield[107]} | {matchfield[108]} |╣╬╠|
| {matchfield[99]} | {matchfield[98]} | {matchfield[97]} | {matchfield[96]} | {matchfield[95]} | {matchfield[94]} |▒{matchfield[93]}▒| {matchfield[92]} | {matchfield[91]} | {matchfield[90]} |
| {matchfield[80]} | {matchfield[81]} |▒{matchfield[82]}▒| {matchfield[83]} | {matchfield[84]} | {matchfield[85]} | {matchfield[86]} | {matchfield[87]} |▼{matchfield[88]}▼| {matchfield[89]} |
| {matchfield[79]} |▒{matchfield[78]}▒| {matchfield[77]} | {matchfield[76]} | {matchfield[75]} | {matchfield[74]} | {matchfield[73]} |▒{matchfield[72]}▒|▼{matchfield[71]}▼| {matchfield[70]} |
| {matchfield[60]} | {matchfield[61]} | {matchfield[62]} | {matchfield[63]} | {matchfield[64]} | {matchfield[65]} | {matchfield[66]} | {matchfield[67]} |▼{matchfield[68]}▼| {matchfield[69]} |
| {matchfield[59]} | {matchfield[58]} |▼{matchfield[57]}▼| {matchfield[56]} |▒{matchfield[55]}▒| {matchfield[54]} | {matchfield[53]} | {matchfield[52]} | {matchfield[51]} | {matchfield[50]} |
| {matchfield[40]} | {matchfield[41]} |▼{matchfield[42]}▼| {matchfield[43]} | {matchfield[44]} |▒{matchfield[45]}▒| {matchfield[46]} | {matchfield[47]} | {matchfield[48]} | {matchfield[49]} |
|▒{matchfield[39]}▒| {matchfield[38]} | {matchfield[37]} | {matchfield[36]} | {matchfield[35]} | {matchfield[34]} | {matchfield[33]} | {matchfield[32]} | {matchfield[31]} | {matchfield[30]} |
| {matchfield[20]} | {matchfield[21]} | {matchfield[22]} | {matchfield[23]} | {matchfield[24]} | {matchfield[25]} |▼{matchfield[26]}▼| {matchfield[27]} | {matchfield[28]} |▒{matchfield[29]}▒|	
| {matchfield[19]} |▒{matchfield[18]}▒| {matchfield[17]} | {matchfield[16]} |▒{matchfield[15]}▒| {matchfield[14]} |▼{matchfield[13]}▼| {matchfield[12]} | {matchfield[11]} | {matchfield[10]} |
| {matchfield[0]} | {matchfield[1]} | {matchfield[2]} |▒{matchfield[3]}▒| {matchfield[4]} | {matchfield[5]} | {matchfield[6]} | {matchfield[7]} |▒{matchfield[8]}▒| {matchfield[9]} |


''')

def check_snakes():
    global user_p
    global computer_p

    if matchfield[26] != '_':
        matchfield[13] = matchfield[26]
        if matchfield[26] == "\033[93m{}\033[0m".format("■"):
            user_p = 13 - 1
        else:
            computer_p = 13 - 1
        matchfield[26] = '_'
        
    elif matchfield[57] != '_':
        matchfield[42] = matchfield[57]
        if matchfield[57] == "\033[93m{}\033[0m".format("■"):
            user_p = 42 - 1
        else:
            computer_p = 42 - 1
        matchfield[57] = '_'

    elif matchfield[88] != '_' or matchfield[71] != '_':
        if matchfield[88] != '_':
            matchfield[68] = matchfield[88]

            if matchfield[68] == "\033[93m{}\033[0m".format("■"):
                user_p = 68 - 1

            else:
                computer_p = 68 - 1
            
            matchfield[88] = '_'
        
        else:
            matchfield[68] = matchfield[71]
            if matchfield[71] == "\033[93m{}\033[0m".format("■"):
                user_p = 68 - 1

            else:
                computer_p = 68 - 1
            matchfield[71] = '_'
    else:
        pass

def check_ladder():
    global user_p
    global computer_p

# 18 : 39
# 45 : 55
# 78 : 82
# 72 : 93


    if matchfield[3] != '_':
        matchfield[15] = matchfield[3]
        if matchfield[3] == "\033[93m{}\033[0m".format("■"):
            user_p = 15 - 1
        else:
            computer_p = 15 - 1
        matchfield[3] = '_'
        
    elif matchfield[8] != '_':
        matchfield[29] = matchfield[8]
        if matchfield[8] == "\033[93m{}\033[0m".format("■"):
            user_p = 29 - 1
        else:
            computer_p = 29 - 1
        matchfield[8] = '_'

    elif matchfield[18] != '_':
        matchfield[39] = matchfield[18]
        if matchfield[18] == "\033[93m{}\033[0m".format("■"):
            user_p = 39 - 1
        else:
            computer_p = 39 - 1
        matchfield[18] = '_'


    elif matchfield[45] != '_':
        matchfield[55] = matchfield[45]
        if matchfield[45] == "\033[93m{}\033[0m".format("■"):
            user_p = 55 - 1
        else:
            computer_p = 55 - 1
        matchfield[45] = '_'

    elif matchfield[78] != '_':
        matchfield[82] = matchfield[78]
        if matchfield[78] == "\033[93m{}\033[0m".format("■"):
            user_p = 82 - 1
        else:
            computer_p = 82 - 1
        matchfield[78] = '_'

    elif matchfield[72] != '_':
        matchfield[93] = matchfield[72]
        if matchfield[72] == "\033[93m{}\033[0m".format("■"):
            user_p = 93 - 1
        else:
            computer_p = 93 - 1
        matchfield[72] = '_'

    
    else:
        pass

def check_win():
    if "\033[93m{}\033[0m".format("■") in list(matchfield[109:119]):
        print('Yelow has won')
        return True

    elif "\033[94m{}\033[0m".format("■") in list(matchfield[109:119]):
        print('blue has wone')
        return True

def delx():
    matchfield[13] = '_'
    matchfield[42] = '_'
    matchfield[68] = '_'

def würfel():
    print()
    for _ in range(0,45):
        time.sleep(0.0001)       ####
        x = random.randint(1,6)
        print(f'\r [{x}]', end='', flush=True)
    time.sleep(0.0)             ####
    return x

# ☻    ■   ▼


print('''

Welcom to snakes and ladders:

Game:
    If you land in a ▒_▒ box, you will be teleported to the nearest one ahead.

    If you land in a ▼_▼ box, you will be teleported to the nearest one below.
      
have fun!
''')



while True:
    


    prind_fild()
    
    matchfield[user_p - 1] = '_'
    
    user_p += würfel()
    if matchfield[user_p - 1] == '_':
        pass

    else:
        user_p += 1
    matchfield[user_p - 1] = "\033[93m{}\033[0m".format("■")
    input()
    check_snakes()
    check_ladder()
    if check_win():
        break
    prind_fild()
    
    matchfield[computer_p - 1] = '_'
    
    computer_p += würfel()
    if matchfield[computer_p - 1] == '_':
        pass
        
    else:
        computer_p += 1

    matchfield[computer_p - 1] = "\033[94m{}\033[0m".format("■")
    input()
    check_snakes()
    check_ladder()
    if check_win():
        break
    prind_fild()
    
    


input()