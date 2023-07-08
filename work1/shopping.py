paid = int(input("Nhap so tien da chi: "))
if paid < 75:
    print(paid)
elif paid >= 75 and paid < 100:
    print(paid - 15)
elif paid >= 100 and paid < 150:
    print(paid - 25)
elif paid >= 150:
    print(paid - 50)