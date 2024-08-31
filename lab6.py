# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:21:49 2024

@author: nguyenthikieutrang
"""
a = int(input("nhập số năm sinh của bạn:"))
if a <= 2024:
    so_tuoi = 2024 - a
    print("số tuổi của bạn là: ", so_tuoi)
else:
    print("số năm sinh của bạn không đúng")