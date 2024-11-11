'''
Nama: Ilyassa Putra
NIM: 2402741
Kelas: 1C-RPL
'''

print("Mulai")
a = int(input("jam: "))
b = int(input("Menit: "))
c = int(input("Detik: "))

print("Selesai")
d = int(input("jam: "))
e = int(input("Menit: "))
f = int(input("Detik: "))

g = d - a

if e < b:
    e += 60
    d -= 1
h = e - b

if f < c:
    f += 60
    e -= 1
i = f - c

print("Hitung hasil:")
print(f"{g} jam - {h} Menit - {i} Detik")