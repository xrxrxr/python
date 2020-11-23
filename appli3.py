#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Hello, bienvenu dans notre boutique")





produits = {
    1:{"id": "1", "nom": "Poire", "prix": "4", "Quantité": "", "prixHT": ""},
    2:{"id": "2", "nom": "Poire", "prix": "2", "Quantité": "", "prixHT": ""},
    3:{"id": "3", "nom": "Poire", "prix": "1.5", "Quantité": "", "prixHT": ""},
    4:{"id": "4", "nom": "Poire", "prix": "3", "Quantité": "", "prixHT": ""},
}



for item in list:
    print(":",item[0]," "*(9-len(item[0])),":",
    item[1]," "*(13-len(item[1])),":",
    item[2]," "*(4-len(str(item[2])),":")
