import math

def luas(jari: int | float) -> float:
    '''
    luas lingkaran pi x r x r

    jari: nilai dari jari jari lingkaran
    '''
    return math.pi * jari**2



def keliling(jari: int | float) -> float:
    '''
    keliling lingkaran 2 x pi x r

    jari: nilai dari jari jari lingkaran
    '''
    return math.pi * jari * 2




jari = float(input("Inpo jari jari: "))
             
print(f"Inpo luas didapat: {luas(jari=jari)}")

print(f"Inpo keliling didapat: {keliling(jari=jari)}")

