w = float(input("Nhap can nang: "))
h = float(input("Nhap chieu cao: "))
bmi = w/(h**2)
if bmi < 16:
    print("Gay cap do III")
elif bmi >= 16 and bmi < 17:
    print("Gay cap do II")
elif bmi >= 17 and bmi < 18.5:
    print("Gay cap do I")
elif bmi >= 18.5 and bmi < 25: 
    print("Binh thuong")
elif bmi >= 25 and bmi < 30:
    print("Thua can")
elif bmi >= 30 and bmi < 35:
    print("Beo phi cap do I")
elif bmi >= 35 and bmi < 40:
    print("Beo phi cap do II")
elif bmi >= 40:
    print("Beo phi cap do III")