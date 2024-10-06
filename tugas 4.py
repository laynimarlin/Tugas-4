def multiply_numbers(a,b):
    return a*b

# Input bilangan
bilangan_1 = [[2, 3, 1],
              [3, 5, 2],
              [4, 2, 3]]

bilangan_2 = [[5, 3, 1],
              [2, 1, 4],
              [3, 2, 1]]

# Hasil perkalian
hasil = [[multiply_numbers(bilangan_1[i][j], bilangan_2[i][j]) for j in range(3)]for i in range(3)]

# Menampilkan hasil
for row in hasil:
    print(row)