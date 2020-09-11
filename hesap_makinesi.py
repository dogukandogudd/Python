islem=input("İşlemi sayısını giriniz (1+,2-,3*,4/): ")
sayi1=int(input("İlk sayıyı giriniz : "))
sayi2=int(input("İkinici sayıyı giriniz :"))
if islem =="1":
    sonuc= int(sayi1)+int(sayi2)
    print("Sonuç : ",str(sonuc))
elif islem =="2":
    sonuc= int(sayi1)-int(sayi2)
    print("Sonuç : ",str(sonuc))
elif islem =="4":
    sonuc= int(sayi1)*int(sayi2)
    print("Sonuç : ",str(sonuc))
elif islem =="5":
    sonuc= int(sayi1)/int(sayi2)
    print("Sonuç : ",str(sonuc))   