def cekPrima(angka):
    if angka <= 2:
        return f"Tidak ada angka prima yang lebih rendah dari {angka}"
    else:
        for i in range(angka-1, 1, -1):  
            prima = True
            for j in range(2, i):
                if i % j == 0:
                    prima = False
                    break
            if prima:
                return i
    
masukan1 = int(input("Masukkan sebuah angka: "))
print(cekPrima(masukan1))

