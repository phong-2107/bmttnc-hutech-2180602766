def chiaHetCho5(soNP):
    soTP = int (soNP, 2)
    if soTP % 5 == 0:
        return True
    else:
        return False
    
chuoiNhiPhan = input("nhap chuoi nhi phan :")
soNhiPhanList = chuoiNhiPhan.split(',')
soChiaHet5 = [so for so in soNhiPhanList if chiaHetCho5(so)]
if len(soChiaHet5) > 0:
    ketqua  = ','.join(soChiaHet5)
    print("cac so chia het 5 la : ", ketqua)
else:
    print("khong co so nao chia het cho 5 trong chuoi")