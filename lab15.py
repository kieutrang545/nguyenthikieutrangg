# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:35:32 2024

@author: nguyenthikieutrang
"""
a = float(input("nhap so a:"))
b = float(input("nhap so b:"))
A = ((a + b) / (a**(1/3) + b**(1/3)) - (a*b)**(1/3)) / (a**(1/3) - b**(1/3))**2
print("gia tri cua bieu thuc la: ", A)