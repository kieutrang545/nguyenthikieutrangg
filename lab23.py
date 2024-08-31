# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:12:16 2024

@author: nguyenthikieutrang
"""
print("giải phương trình bậc hai")
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
D=b*b-4*a*c
if D==0:
    nghiem_kep = -b/(2*a)
    print("PT có nghiệm kép x1 = x2 =", nghiem_kep)
if D>0:
    hai_nghiem = (-b+D**0.5)/(2*a),"và x2=",(-b-D**0.5)/(2*a)
    print("PT có hai nghiệm x1=", hai_nghiem)
if D<0:
    print("PT vô nghiệm")
