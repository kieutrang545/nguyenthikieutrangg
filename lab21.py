# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:39:09 2024

@author: nguyenthikieutrang
"""
def doc_so(so):
  so_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
  if 0 <= so <= 9:
    return so_chu[so]
  else:
    return "Không đọc được"
so_nhap = int(input("Nhập một số: "))
ket_qua = doc_so(so_nhap)
print(ket_qua)
