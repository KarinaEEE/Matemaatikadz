#Kodutoo matemaatika

import random


raskus=int(input("Palun valige raskusaste (1, 2, 3): "))
küsimuste_arv=int(input("Palun valige küsimuste arv: "))
küsimused=[]
õiged_vastused=0

for _ in range(küsimuste_arv):
    tehe=random.choice(['+', '-', '*', '/', '**'])
    if raskus==1:
        arv1=random.randint(1, 10)
        arv2=random.randint(1, 10)
    elif raskus==2:
        arv1=random.randint(10, 100)
        arv2=random.randint(10, 100)
    elif raskus==3:
        arv1=random.randint(100, 1000)
        arv2=random.randint(100, 1000)
    
    if tehe=='+':
        küsimus=f"{arv1} + {arv2}"
        vastus=arv1 + arv2
    elif tehe=='-':
        küsimus=f"{arv1} - {arv2}"
        vastus=arv1 - arv2
    elif tehe=='*':
        küsimus=f"{arv1} * {arv2}"
        vastus=arv1 * arv2
    elif tehe=='/':
        küsimus=f"{arv1} / {arv2}"
        vastus=arv1 / arv2
    elif tehe=='**':
        küsimus=f"{arv1} ** {arv2}"
        vastus=arv1 ** arv2

    kasutaja_vastus=float(input(f"{küsimus} = "))
    if kasutaja_vastus==vastus:
        print("Õige!")
        õiged_vastused += 1
    else:
        print("Vale vastus!")

tulemus=(õiged_vastused / küsimuste_arv) * 100
print(f"Teie tulemus: {tulemus}%")
if tulemus<60:
    print("Hinne 2")
elif tulemus<75:
    print("Hinne 3")
elif tulemus<90:
    print("Hinne 4")
elif tulemus>90:
    print("Hinne 5")

