num = float(input("Nhap 1 so bat ky: "))
if num%2 == 0 and num == int(num) and num >= 0:
    print("La so chan")
elif num%2 != 0 and num == int(num) and num >= 0:
    print("La so le")
else:
    print("Khong phai so tu nhien")