import os
from HCN import HCNhat
n = int(input("Nhap So Luong HCN ban muon : "))
a = []
for i in range(0,n):
    print("-------------------------------------------------")
    print("Nhap Thong Tin HCN Thu :",i+1)
    ten = input("Nhap ten HCN :")
    dai = int(input("Nhap Chieu Dai HCN :"))
    rong = int(input("Nhap Chieu Rong HCN :"))
    HCN = HCNhat(ten,dai,rong)
    a.append(HCN)
for iteam in a:
    print("-------------------------------------------------")
    print("Thong Tin HCN :", iteam.getTen())
    CV = iteam.getCV()
    DT = iteam.getDT()
    print(iteam.ToString())
    print("Chu Vi =",CV)
    print("Dien Tich =", DT)
DT_MAX = a[0].getDT()
for item in a:
    print("-------------------------------------------------")
    if(iteam.getDT()>DT_MAX):
        print( "HCN lon nhat la :", iteam.getTen())
        break
file = open("LuuHCN.txt", "w")
for file1 in a:
    file.write("-------------------------------------\n")
    file.write(file1.ToString()+"\n")
    file.write("Dien Tich " +str(file1.getDT())+"\n")
    print("\n")
    file.write("Chu Vi   " +str(file1.getCV())+"\n")