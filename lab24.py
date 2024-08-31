# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:47:57 2024

@author: nguyenthikieutrang
"""
a = float(input("nhập số giờ:"))
b = float(input("nhập số phút:"))
c = float(input("nhập số giây:"))
if 0 <= a < 24:
    print("số giờ hợp lệ")
else:
        print("số giờ không hợp lệ")
if 0 <= b < 60:
    print("số phút hợp lệ")
else:
        print("số phút không hợp lệ")
if 0 <= c < 60:
    print("số giây hợp lệ")
else:
    print("số giây không hợp lệ")