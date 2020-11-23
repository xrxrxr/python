#!/usr/bin/python
# -*- coding: utf-8 -*-

print("Hello, on calcule la tva")
n  = int(input("entre le prix hors taxes:"))
quant  = int(input("entre une quantité:"))

if n != "0":
        print (" erreur entre une valeur superieur a 0")
else:
        if quant != "0":
                print (" erreur entre une valeur superieur a 0")
        else:
            print ("prix sans tva" , (n)*(quant))
tva = (n*quant)*1.2

print ( "prix avec la tva" , (tva))
tva > 200
(tva) / 5
