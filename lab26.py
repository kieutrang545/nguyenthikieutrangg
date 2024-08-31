# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:50:12 2024

@author: nguyenthikieutrang
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
temp = 0
if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print("Thứ tự tăng dần: ", a, b, c)
N = int(input("Nhập số nguyên N: "))
chuso = [int(x) for x in str(N)]
chuso.sort()
N_moi = int("".join(map(str, chuso)))
print("Số có các chữ số theo thứ tự tăng dần: ", N_moi)
