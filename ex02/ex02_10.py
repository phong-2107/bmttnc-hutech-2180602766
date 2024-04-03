def daoNguocChuoi(chuoi):
    return chuoi[::-1]

input_Str = input("moi nhap chuoi: ")
print("chuoi dao nguoc la : ", daoNguocChuoi(input_Str))