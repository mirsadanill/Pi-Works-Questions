sayi=input("Bir sayı girin: ")
toplam=0
for rakam in sayi:
  toplam += int(rakam)
 
print("sayının rakamları toplamı:",toplam)

if (int(sayi)%int(toplam))==0 :
    print("Tam bölünebilir") 
else:
    print("Tam bölünemez")
    
    
    
