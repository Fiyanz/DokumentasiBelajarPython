import math
import matplotlib.pyplot as plt
import numpy as np

# Mendefinisikan variabel a dan b di luar fungsi
a = 0  # Batas bawah integrasi (alas silinder)
b = 10  # Batas atas integrasi (puncak silinder)

def volume_silinder(r, h, n):
  """
  Menghitung volume silinder dengan integral Riemann.

  Args:
    r: Jari-jari silinder.
    h: Tinggi silinder.
    n: Jumlah langkah untuk integrasi numerik.

  Returns:
    Volume silinder.
  """

  def f(x):
    return math.pi * r**2  # Fungsi luas penampang silinder

  # Menghitung integral Riemann menggunakan metode trapesium
  volume = 0
  for i in range(1, n):
    volume += (b - a) / 2 * (f(a) + f(b))

  return volume

# Menentukan nilai jari-jari dan tinggi
r = 5
h = 10

# Menentukan jumlah langkah untuk integrasi numerik
n = 100

# Menghitung volume silinder
volume = volume_silinder(r, h, n)

# Menentukan sumbu x dan y
x = np.linspace(a, b, n)  # Membagi interval [a, b] menjadi n langkah
y = np.vectorize(f(x))  # Menghitung f(x) untuk semua elemen di x

# Memvisualisasikan volume silinder
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("Luas Penampang Silinder")
plt.title("Volume Silinder")
plt.show()

# Menampilkan hasil volume
print("Volume silinder:", volume)
