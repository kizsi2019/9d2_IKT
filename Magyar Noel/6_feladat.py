import random 

i = 0
szamlalo = 0
while i < 20:
    szam = random.randint(1,12)
    if szam % 3 == 0:
        print(szam)
        szamlalo = szamlalo + 1
    i = i + 1
print("A lefutott program", szamlalo, "-szor talált 3-al osztható számot!")