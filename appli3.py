#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Hello, bienvenu dans notre boutique")

from prettytable import PrettyTable




produits = {
            1: {'nom':'Banane', 'prix': 4, 'quantité':0},
            2: {'nom':'Pomme', 'prix': 2,'quantité':0},
            3: {'nom':'Orange', 'prix': 1.5, 'quantité':0},
            4: {'nom':'Poire', 'prix': 3,'quantité':0}
          }




table = PrettyTable(["id",'nom','prix'])

for (key,value) in produits.items():
    table.add_row([key, value['nom'], value['prix'],])

print (table)

n1  = int(input("combien de bananes tu veux? "))
n2  = int(input("combien de pommes tu veux? "))
n3  = int(input("combien de oranges tu veux? "))
n4  = int(input("combien de Poires tu veux? "))
print("et de scoubidou bidou")



total = (n1*4)+(n2*2)+(n3*1.5)+(n4*3)

tva = (total)+((total)*20)/100

table2 = PrettyTable(['nom','prix','quantité'])

table2.add_row([produits[1]['nom'], produits[1]['prix'], n1])
table2.add_row([produits[2]['nom'], produits[2]['prix'], n2])
table2.add_row([produits[3]['nom'], produits[3]['prix'], n3])
table2.add_row([produits[4]['nom'], produits[4]['prix'], n4])
print (table2)
print ("ça fera hors taxes ", total ," €")
print ("et avec la tva " ,tva , " €")
