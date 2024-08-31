# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:15:55 2024

@author: nguyenthikieutrang
"""
a = int(input("nhập giờ:"))
b = int(input("nhập phút:"))
c = int(input("nhập giây:"))
Tong_so_giay = ( c + (b * 60) + (a * 3600))
print("Tổng số giây là: ", Tong_so_giay)