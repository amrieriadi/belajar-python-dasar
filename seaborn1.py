import seaborn as sns
import matplotlib.pyplot as plt

#Data
categories = ['Category A', 'Category B', 'Category C']
values=[25, 40, 30]

#Plotting bar chart dengan seaborn
sns.barplot(x=categories, y=values)

#Menambahkan label

plt.xlabel('Kategori')
plt.ylabel('Nilai')
plt.title('Contoh Grafik Bar dengan Seaborn')

#Menampilkan grafik
plt.show()

#Tambahkan perintah ini untuk menjaga tampilan grafis
plt.pause(0.001)
plt.show(block=True)
