nilai1 = float(input("Masukkan nilai 1: "))
nilai2 = float(input("Masukkan nilai 2: "))
nilai3 = float(input("Masukkan nilai 3: "))
nilai4 = float(input("Masukkan nilai 4: "))
nilai5 = float(input("Masukkan nilai 5: "))

import math
a = max(nilai1, nilai2, nilai3, nilai4, nilai5)
b = min(nilai1, nilai2, nilai3, nilai4, nilai5)
jangkauan = a-b
print("jangkauan = ", jangkauan)

x = [nilai1, nilai2, nilai3, nilai4, nilai5]
x.sort()
print("x sesudah diurutkan = ", x)

n = nilai1, nilai2, nilai3, nilai4, nilai5
m = sorted(n)
print("n = ", n)
print("m = ", m)