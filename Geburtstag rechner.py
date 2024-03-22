from datetime import datetime


def take():
    global User_T
    print('DD MM YYYY')
    #User_T = input('input ur date')
    User_T = '01 0 2024'


def to_day():
    AA = datetime.now()
    global heute
    heute =  AA.strftime('%d %m %Y')

def calc_age():
    pass



take()
to_day()

# print(f'you was born: {User_T}')
# print(f'Today is the: {to_day()}')

years = int(heute[6:10]) - int(User_T[6:10])

month = 0


print(years)
print(month)
print()
