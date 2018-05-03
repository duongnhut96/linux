import os
n = int(input("Nhap So Phan Tu Trong Day : "))
a = []
for i in range(0,n):
    print("Nhap phan tu thu",i)
    Nhap = int(input())
    a.append(Nhap)
print("Day Vua Nhap La :",a)
print("-------------------------------")
print("So Chan Trong Day la :")
for chan in a:
    if(chan % 2 == 0):

        print(chan)
x=a.sort()
print("Sap xep day  =",x)
#ghi file
file = open("LuTru.txt","w")
file.write(str(a))