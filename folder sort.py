import os
import shutil
os.chdir(r'/home/timon/Dokumente/Code laufzeit umgebung/02')
ordner = ['Images', 'Videos', 'Else']
bildendungen = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff']
videoendungen = ['.mp4', '.avi', '.mkv', '.wmv', '.mov', '.flv', '.mpeg', '.mpg']


for i in ordner:
    if os.path.exists(os.getcwd() + '/' + i):
        continue
    else:
        os.mkdir(i)


fiels = os.listdir(os.getcwd())
[fiels.remove(x) for x in ordner]
for i in fiels:
    if i[i.rfind('.'):] in bildendungen:
        shutil.move(os.getcwd() + '/' + i, os.getcwd() + '/' + ordner[0])
    elif i[i.rfind('.'):] in videoendungen:
        shutil.move(os.getcwd() + '/' + i, os.getcwd() + '/' + ordner[1])
    else:
        shutil.move(os.getcwd() + '/' + i, os.getcwd() + '/' + ordner[2])