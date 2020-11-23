#!/usr/bin/python
# -*- coding: utf-8 -*-

print("Hello, on calcule la tva")
n  = int(input("entre le prix hors taxes:"))
quant  = int(input("entre une quantité:"))

#if n == "0":
#        print (" erreur entre une valeur superieur a 0")
#if quant == "0":
#    print (" erreur entre une valeur superieur a 0")
#    quit()
# else:

print ("prix sans tva" , (n)*(quant))
tva = (n*quant)*1.2

print ( "prix avec la tva" , (tva))

if (tva) > 200:
    rem= (tva)/5

    print("remise de 5%", (rem))
    print(" total avec la remise de 5%", (tva)-(rem))
