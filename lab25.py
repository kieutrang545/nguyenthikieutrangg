# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:13:05 2024

@author: Administrator
"""

def doi_chu_cai(chu_cai):
  if chu_cai.islower():
    return chu_cai.upper()
  else:
    return chu_cai.lower()
chu_cai = input("Nhập một chữ cái: ")
if len(chu_cai) != 1 or not chu_cai.isalpha():
  print("Vui lòng nhập đúng một chữ cái.")
else:
  chu_cai_moi = doi_chu_cai(chu_cai)
  print("Chữ cái sau khi chuyển đổi:", chu_cai_moi)