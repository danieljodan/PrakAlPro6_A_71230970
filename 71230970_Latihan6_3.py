def deretKotak (t,l):
    luas = t * l
    for i in range (1,luas+1):
        print(i, end = " ")
        if i % l == 0:
            print()

masukan1 = int(input("Masukkan Tinggi: "))
masukan2 = int(input("Masukkan Lebar: "))  
deretKotak(masukan1,masukan2)