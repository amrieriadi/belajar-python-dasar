Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/aammr/OneDrive/Documents/python/pertemuan 5 1.py
Enter a value: 
def pesan():
    print("hallo")

print("OK")
OK
pesan()
hallo
print(pesan())
hallo
None
print("We start here.")
We start here.
message()
Enter a value: 
print("We end here.")
We end here.
def message():
    print("Entera value: ")

    
pesan2()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    pesan2()
NameError: name 'pesan2' is not defined. Did you mean: 'pesan'?
def pesan2()
SyntaxError: expected ':'
def pesan2():
    print("hallo")

    
def pesan2()
SyntaxError: expected ':'
def pesan():
    print("hallo")

    
pesan()
hallo
pesan=10
pesan()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    pesan()
TypeError: 'int' object is not callable
def pesan2():
    print("hallo")

    
pesan2()
hallo
def pesan():
    print("hallo")

    
pesan()
hallo
def pesan(Nama):
    print("hallo")

    
pesan("Amri")
hallo
def pesan(Nama):
    print("hallo" + Nama)

    
pesan("Amri")
halloAmri
def pesan(Nama):
    print("hallo" + str(Nama))

    
pesan(10)
hallo10
def pesan(Nama):
    print("hallo" , Nama)

    
pesan(10)
hallo 10
pesan(100)
hallo 100
def pesan(Nama):
    print("hallo " , Nama)

    
pesan(10)
hallo  10
def TampilAngka(Nomor):
    print("Angka yang dimasukan: ",Nomor)

    
TampilAngka(int(input("Masukan angka:")))
Masukan angka:50
Angka yang dimasukan:  50
print(TampilAngka(int(input("Masukan angka:"))))
Masukan angka:60
Angka yang dimasukan:  60
None
x=int(input("Masukan Angka:"))
Masukan Angka:33
TampilkanAngka(x)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    TampilkanAngka(x)
NameError: name 'TampilkanAngka' is not defined. Did you mean: 'TampilAngka'?
TampilAngka(x)
Angka yang dimasukan:  33

= RESTART: C:/Users/aammr/OneDrive/Documents/python/pertemuan 5 2.py
Traceback (most recent call last):
  File "C:/Users/aammr/OneDrive/Documents/python/pertemuan 5 2.py", line 4, in <module>
    TampilAngka(x)
NameError: name 'x' is not defined
def TampilAngka(Nomo=1):
    print("Angka yang dimasukan:",Nomor)

    
TampilAngka()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    TampilAngka()
  File "<pyshell#54>", line 2, in TampilAngka
    print("Angka yang dimasukan:",Nomor)
NameError: name 'Nomor' is not defined. Did you mean: 'Nomo'?
def TampilAngka(Nomor=1):
    print("Angka yang dimasukan:",Nomor)

    
TampilAngka()
Angka yang dimasukan: 1

= RESTART: C:/Users/aammr/OneDrive/Documents/python/pertemuan 5 2.py
Masukan Angka:5
Angka yang dimasukan:  5
def Perkenalan(Nama, Usia=18):
    print("nama Saya:",Nama,"Usia:",Usia))
    
SyntaxError: unmatched ')'
def Perkenalan(Nama, Usia=18):
    print("nama Saya:",Nama,"Usia:",Usia)

    
Perkenalan("Amri")
nama Saya: Amri Usia: 18
Perkenalan("Amri",19)
nama Saya: Amri Usia: 19
def Perkenalan(Nama, Usia):
    print("nama Saya:",Nama,"Usia:",Usia)

    
Perkenalan("Amri")
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    Perkenalan("Amri")
TypeError: Perkenalan() missing 1 required positional argument: 'Usia'
Perkenalan("Amri","19")
nama Saya: Amri Usia: 19




















def Perkenalan(Nama,Usia):
    print("nama Saya:",Nama,"Usia:",Usia)

    
Perkenalan(Usia=17, Nama="Amri")
nama Saya: Amri Usia: 17
def Perkenalan(Nama,Usia,Alamat):
    print("nama Saya:",Nama,"Usia:",Usia,"Tinggal di:",Alamat)

    
Perkenalan(Usia=17, Alamat="Bandunf",Nama="Amri")
nama Saya: Amri Usia: 17 Tinggal di: Bandunf
Perkenalan(Usia=17, Alamat="Bandunf",Nama="Amri")
nama Saya: Amri Usia: 17 Tinggal di: Bandunf
def sum(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)

    
sum(a,b,c)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    sum(a,b,c)
NameError: name 'a' is not defined
sum(1,2,3)
1 + 2 + 3 = 6



Perkenalan("Agus",20,"Bali")
nama Saya: Agus Usia: 20 Tinggal di: Bali
print(Perkenalan("Agus",20,"Bali"))
nama Saya: Agus Usia: 20 Tinggal di: Bali
None
def nilai(a,b)
SyntaxError: expected ':'
def nilai(a,b):
    x=a+b
    return x

print(nilai(10,15))
25
nilai(10,15)
25
nilaiakhir=nilai(10,15)
print(nilaiakhir)
25
def test():
    x=10
    print(x)

    
test()
10
x=20
print(x)
20
test()
10
print(x)
20
def test():
    z=10
    print(z)

    
test()
10
print(z)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
z=100
def test():
    z=10
    print(z)

    
print(z)
100
test()
10
print(z)
100
z=212
def test():
    print(z)

    
print(z)
212
test()
212
z=212
def test():
    global z
    z=1000
    print(z)

    
print(z)
212
test()
1000
print(z)
1000
def angka1():
    x1=10
    print(x1)

    
def angka2():
    x2=100
    print(x2)

    
print(angka1)
<function angka1 at 0x0000022459F9C360>
angka1()
10
angka2()
100
def angka2():
    x1=100
    print(x1)

    
angka1()
10
def angka2():
    global x1
    x1=100
    print(x1)

    
angka1()
10
>>> printx1()
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    printx1()
NameError: name 'printx1' is not defined. Did you mean: 'print'?
>>> angka2()
100
>>> print(x1)
100
>>> angka()
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    angka()
NameError: name 'angka' is not defined. Did you mean: 'angka1'?
>>> angka1()
10
>>> print(x1)
100
>>> myTuple = (1,10,100,1000)
>>> print(mtTuple[0])
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    print(mtTuple[0])
NameError: name 'mtTuple' is not defined. Did you mean: 'myTuple'?
>>> print(myTuple[0])
1
>>> mylist=[1,2,3.5,"Hallo", True)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> mylist=[1,2,3.5,"Hallo", True]
>>> print(mylist)
[1, 2, 3.5, 'Hallo', True]
