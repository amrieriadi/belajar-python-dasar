import time
number = int(input("Masukan sebuah bilangan: "))
start=time.time()
if number > 0:
    print ("Bilangan Positif")
else:
    if number < 0:
        print ("Bilangan Negatif")
    else:
        print("Bilangan NOL")
stop=time.time()
elap=stop-start
print("Waktu:",str(elap))
print("Selesai") 
