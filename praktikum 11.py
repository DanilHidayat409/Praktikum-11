# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:57:27 2021
@author: Muhammad Danil Hidayat
@NIM : 065002100032
"""

data=int(input("masukan angka yang di cari"))
list1=[10,30,20,25,200,100,40,35,5]
def bubblesort(data):
    for i in range (len(data)-1,0,-1):
        for j in range (0,len(data)-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1]=data[j+1],data[j]
bubblesort(list1)
print("sesudah di sorting", list1)

def binary_search(data, num_find):
    start = 0
    end = len(list1) - 1
    mid = (start + end)//2
    found = False
    position = -1
    while start <= end:
        if list1[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > list1[mid]:
            start = mid + 1
            mid = (start + end)//2
        else:
            end = mid - 1
            mid = (start + end)//2
    return (found, position-1)   
num=data
found = binary_search(data, num)
if found[0]:
    print('Nomor %d ditemukan di posisi %d'%(num, found[1]+2))
else:
    print('Nomor %d tidak ditemukan'%num)
    
    
                    