# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:45:33 2024

@author: nguyenthikieutrang
"""
print("============ MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================")
lua_chon = int(input("Moi nhap lua chon:"))
print("==============================")
if lua_chon == 1:
    print("Hu tieu")
elif lua_chon == 2:
    print("Chao long")
elif lua_chon == 3:
    print("Banh canh")
elif lua_chon == 4:
    print("Bun rieu")
elif lua_chon == 5:
    print("Pho bo")
else:
    print("lua chon khong co trong Menu")