# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:37:31 2024

@author: nguyenthikieutrang
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
print("Số lớn nhất là:", max_num)
