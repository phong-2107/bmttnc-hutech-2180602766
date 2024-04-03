time = float(input("Nhap so gio lam trong tuan: "))
money = float(input("Nhap thu lao moi gio lam: "))

gio_chuan = 44
gio_vuot_chuan = max(0, time - gio_chuan);
thuc_linh = gio_chuan * money + gio_vuot_chuan * money * 1.5
print(f"so tien thuc linh : {thuc_linh}")