def deretFaktorial(n):
    faktorial = n
    total = 1
    for _ in range (1, n+1):
        for j in range (1, faktorial+1):
            total = total * j
        print (total, end = " ")
        for k in range (faktorial, 0, -1):
            print(k, end = " ")
        total = 1
        faktorial = faktorial - 1
        print()
            
masukan1 = int(input("Masukkan n: "))
deretFaktorial(masukan1)

