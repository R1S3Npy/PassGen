import os,time,secrets,csv

PassW = []
Char = [
    'q','1','A','w','2','B','e','3','C','r','4','D','t','5','E','y','6','F','u','7','G','i','8','H','o','9','I','p','0','J','a','!','K','s','@','L','d','#','M','f','$','N','g','%','O','h','^','P','j','&','Q','k','*','R','l','-','S','z','_','T','x','=','U','c','+','V','v','<','W','b','>','X','n','?','Y','m','Z'
]

if not os.path.exists("PassGen.csv") or os.path.getsize("PassGen.csv") == 0:
    with open("PassGen.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Password", "Service"])

with open("PassGen.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row:
            PassW.append(row)


def Gen():
    print("====[GENERATOR]=====\n")
    lenght = int(input("Lunghezza (Consiglio da 8 in su!): "))
    print("Generazione in corso...\n")
    time.sleep(2)

    gen = ""
    for i in range(lenght):
        charStr = secrets.choice(Char)
        gen += charStr
    print(gen)


    service = input("\nNome servizio: ")
    generate = [gen,service]

    PassW.append(generate)
    
    with open("PassGen.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(generate)
    
    input("\n\nHit Enter to go back...")

def View():
    print("====[VIEW]=====\n")
    for row in PassW:
        print(f"{row[0]:<10} | {row[1]:>10}")
    input("\n\nHit Enter to go back...")

while True:
    os.system("clear")
    print("Benvenuto nel PassGen!\n")
    task = input("1.Genera Password\n2.Visualizza passwords\n3.Exit\n\n> ")
    os.system("clear")
    if task == "1":
        Gen()

    elif task == "2":
        View()

    elif task == "3":
        verify = input("Are you sure? Y/N\n> ")
        if verify == "Y" or verify == "y":
            break




