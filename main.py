# 1-FIBONACCI KETMA-KETLIGI
n = int(input("N ni kiriting: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 2-TUB SONLAR (1 dan N gacha)
n = int(input("N ni kiriting: "))

print("Tub sonlar:")

for son in range(2, n + 1):
    tub = True
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")

# 3-RO‘YXATNI SARALASH (sortsiz)
sonlar = list(map(int, input("Sonlarni kiriting (bo‘sh joy bilan): ").split()))

n = len(sonlar)

for i in range(n):
    for j in range(i + 1, n):
        if sonlar[i] > sonlar[j]:
            sonlar[i], sonlar[j] = sonlar[j], sonlar[i]

print("Saralangan ro'yxat:", sonlar)

# 4-ENG KO‘P UCHRAYDIGAN ELEMENT
sonlar = list(map(int, input("Sonlarni kiriting: ").split()))

eng_kop = sonlar[0]
maks_sanoq = 0

for son in sonlar:
    sanoq = 0
    for x in sonlar:
        if x == son:
            sanoq += 1
    if sanoq > maks_sanoq:
        maks_sanoq = sanoq
        eng_kop = son

print("Eng ko‘p uchraydigan element:", eng_kop)

# 5-SO‘ZLARNI SANASH
jumla = input("Jumla kiriting: ")

sozlar = jumla.split()
print("So'zlar soni:", len(sozlar))
