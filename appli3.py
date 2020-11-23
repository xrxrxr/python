#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Hello, bienvenu dans notre boutique")





produits = {
    1:{"id": "1", "nom": "banane", "prix": "4", "quantité": "", "prixHT": ""},
    2:{"id": "2", "nom": "pommme", "prix": "2", "quantité": "", "prixHT": ""},
    3:{"id": "3", "nom": "orange", "prix": "1.5", "quantité": "", "prixHT": ""},
    4:{"id": "4", "nom": "poire", "prix": "3", "quantité": "", "prixHT": ""},
}



for item in produits:

    print (produits(item, headers=["banane", "pommme", "orange", "poire"]))
     #print(format('id', str,'nom','poire', str , "quantité" , "prixHT" , str),
