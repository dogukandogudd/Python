sayi=int(input("Kaça kadar sayıların toplamını alacağını beliritiniz: "))
toplam=0
for i in range(1,sayi+1,1):
    toplam+=i
print("Sayıların toplamı: ",str(toplam))