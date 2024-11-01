
X = [1, 5, 5, 7, 6, 7, 9, 2, 0, 5, 4, 6, 7, 2, 7, 8, 2, 4, 6, 2]

y1 = int(input("Masukkan nilai y1 (0-10): "))

if y1 in X and y1 % 2 == 0:
    indices = [i for i, value in enumerate(X) if value == y1]
    print("Indeks y1 (genap) ditemukan di:", indices)
else:
    print("Tidak ada hasil atau y1 bukan bilangan genap.")
