import random
import json
'''
0 -> 2  0-> 4
1 -> 3  1-> 0
2 -> 4  2-> 1
3 -> 0  3-> 2
4 -> 1  4-> 3
''' 
dateipfad = "C:/Users/Lukas/Documents/5.KLasse/SWP Python- Rubner/Github/SWP_Rubner5/Stats.txt"

def read():
    with open(dateipfad, 'r') as datei:
        stats = json.loads(datei.read())
    return stats

def write(stats):
    with open(dateipfad, 'w') as datei:
        json.dump(stats, datei)

def printstats():
    with open(dateipfad, 'r') as datei:
        stats = json.loads(datei.read())
        print(stats) 

def startespiel():
    benutzerEingabe = int(input("Eingabe(Spock=0/Echse=1/Stein=2/Papier=3/Schere=4: "))
    computerEingabe = random.randint(1,4)
    
    stats = read()
    if(benutzerEingabe + 2)%5 == computerEingabe or (benutzerEingabe-1)%5 == computerEingabe:
        print("Gewonnen :)")
        stats['SpielerGewonnen'] += 1
    else:
        print("Verloren :(")
        stats['ComputerGewonnnen'] += 1

    stats[str(benutzerEingabe)] += 1
    write(stats)

def Statistik():
    printstats()

def menu():
    eingabe = input("Wählen sie: 'Spiel' oder 'Stat': ")
    
    if(eingabe.lower().strip() == "spiel"):
        while True:
         startespiel()
    elif(eingabe.lower().strip() == "stat"):
       Statistik()
    else:
        print("Keine gültige Eingabe")


if __name__ == "__main__":
    menu()
    

