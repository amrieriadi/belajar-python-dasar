import matplotlib.pyplot as plt

# Data
x=[1, 2, 3, 4, 5]
y=[2, 4, 6, 8, 10]

# Membuat grafik garis
plt.plot(x,y)

# Menambahkan label sumbu dan judul
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Grafik Garis')

# Menampilkan grafik
plt.show()
