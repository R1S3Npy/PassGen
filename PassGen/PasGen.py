import os,time,random,csv

PassW = []
maiuscole = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscole = "abcdefghijklmnopqrstuvwxyz"
numeri = "0123456789"
simboli = "!@#$%^&*()-_=+[]{};:,.<>?/"

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

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def Gen():
    while True:
        clear()
        print("====[GENERATOR]=====\n")
        lenght = int(input("Lunghezza (Consiglio da 8 in su!): "))

        if lenght < 4:
            print("Errore: la password deve avere almeno 4 caratteri")
            input("\n\nHit Enter to go back...")
            return

        print("Generazione in corso...\n")
        time.sleep(2)

        password = [
            random.choice(maiuscole),
            random.choice(minuscole),
            random.choice(numeri),
            random.choice(simboli)
        ]

        tutti = maiuscole + minuscole + numeri + simboli
        for i in range(lenght - 4):
            password.append(random.choice(tutti))

        random.shuffle(password)
        gen = "".join(password)
        print(gen)

        scelta = input("\nTi piace? (S = sì, R = rigenera, N = esci)\n> ")

        if scelta.lower() == "s":
            service = input("\nNome servizio: ")
            PassW.append([gen, service])
            print(f"Salvata: {gen} -> {service}\n")

            with open("PassGen.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([gen, service])

            input("\n\nHit Enter to go back...")
            break

        elif scelta.lower() == "n":
            break
        elif scelta.lower() == "r":
            continue

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



