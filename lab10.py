# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:58:59 2024

@author: nguyenthikieutrang
"""
so = int(input("nhập 4 số xe:"))
nguyen1 = so // 1000
du1 = so % 1000
nguyen2 = du1 // 100
du2 = du1 % 100
nguyen3 = du2 // 10
du3 = du2 % 10
nguyen4 = du3
tinh = nguyen1 + nguyen2 + nguyen3 +nguyen4
cuoi = tinh%10 + tinh//10
print("số nút 4 chữ số = ", cuoi)