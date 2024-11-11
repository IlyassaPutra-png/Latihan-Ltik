'''
Nama: Ilyassa Putra
NIM: 2602741
Kelas: 1-RPL
menambahkan fitur.py
'''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 0:
        return[0]
    elif n == 2:
        return[0,1]

    deret_awal = [0,1]
    for i in range(2, n):
        deret_akhir = deret_awal [-1] + deret_awal [-2]
        deret_awal.append(deret_akhir)
    return deret_awal

N = int(input("Masukan panjang deret fibonacci: "))

print(f"Deret fibonacci sebanyak {N} angka: {fibonacci(N)}")
