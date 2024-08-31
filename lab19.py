# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:29:47 2024

@author: nguyenthikieutrang
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))
min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d
print("Số nhỏ nhất là:", min_num)
