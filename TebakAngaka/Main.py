import random

def random_angka(x):
    data = random.randint(0, x)
    a = 0 
    while a != data:
        a = int(input("Masukan angka: "))
        if a < data:
            print("Angka kurang besar")
        elif a > data:
            print("Angka kebesaran")

    print("Tebakan benar")
            
        
random_angka(100)        