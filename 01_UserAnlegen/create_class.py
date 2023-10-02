import random
from openpyxl import load_workbook

def getClasses(file):
    infos=list()
    wb = load_workbook(file, read_only=True)
    ws = wb[wb.sheetnames[0]]
    for row in ws.iter_rows():
        x = row[0]
        y = x.value
        x1 = row[1]
        y1 = x1.value
        x2 = row[2]
        y2 = x2.value

        if y!=None and y[0].isdigit():
            infos.append([y,y1,y2])
    return infos

def createpasswd(klasse,room,teacher):
    zeichenkette = "!%&(),._-=^#"
    return klasse + "" + random.choice(zeichenkette) + "" + str(room) + "" + random.choice(zeichenkette) + "" + teacher + "" + random.choice(zeichenkette)

def createUsers(infos):
    with open('.\\01_UserAnlegen\\createClasses', 'w') as f:
        f.write("groupadd Lehrer\n")
        f.write("groupadd Seminar\n")
        f.write("groupadd Klasse\n")
        f.write("groupadd cdrom\n")
        f.write("groupadd plugdev\n")
        f.write("groupadd sambashare\n")
        f.write("useradd -d \"/home/lehrer\"-c \"lehrer\" -m -g Lehrer -G cdrom,plugdev,sambashare -s /bin/bash lehrer\n")
        f.write("useradd -d \"/home/seminar\"-c \"seminar\" -m -g Seminar -G cdrom,plugdev,sambashare -s /bin/bash seminar\n")
        for i in infos:
            f.write("useradd /home/klassen/k"+i[0].lower()+" -c \""+i[0]+"\" -m -g Klasse -G cdrom,plugdev,sambashare -s /bin/bash k"+i[0].lower()+"\n")
            f.write("echo \"k"+i[0].lower()+":"+createpasswd(i[0],i[1],i[2])+" | chpasswd\"\n")

createUsers(getClasses(".\\01_UserAnlegen\\Klassenraeume_2023.xlsx"))
