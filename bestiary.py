#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
# from avatar import Creature

class Caninae(object):
    def __init__(self, name):
        self.name = name
        self.description = ("Un chien sauvage, affaibli par la faim et la maladie.")
        self.maxhealth = 20
        self.health = self.maxhealth
        self.matorg = 70 # organic material
        self.baseattack = 4
        self.jetogain = 5 # tokens given to player when defeated
        self.aboneed = 0 # number of followers needed to spawn
        self.abogain = 5 # followers given to player when defeated
caninae_active = Caninae("Caninae")

class Casuariidae(object):
    def __init__(self, name):
        self.name = name
        self.description = ("Cet imposant oiseau ne sait peut-être pas voler, mais son bec et ses longues pattes griffues sont mortels.")
        self.maxhealth = 50
        self.health = self.maxhealth
        self.matorg = 70
        self.baseattack = 10
        self.jetogain = 15
        self.aboneed = 6
        self.abogain = 10
casuariidae_active = Casuariidae("Casuariidae")

class BiOurs(object):
    def __init__(self, name):
        self.name = name
        self.description = ("Cet ours...")
        self.maxhealth = 70
        self.health = self.maxhealth
        self.matorg = 70
        self.baseattack = 15
        self.jetogain = 30
        self.aboneed = 20
        self.abogain = 35
biours_active = BiOurs("BiOurs")

class Crocaillou(object):
    def __init__(self, name):
        self.name = name
        self.description = ("Vu de loin, on dirait bien un rocher, et pourtant, il bouge.")
        self.maxhealth = 100
        self.health = self.maxhealth
        self.matorg = 100
        self.baseattack = 20
        self.jetogain = 50
        self.aboneed = 70
        self.abogain = 60
crocaillou_active = Crocaillou("Crocaillou")

class Proboscidea(object):
    def __init__(self, name):
        self.name = name
        self.description = ("Un animal énorme, aussi gras que musclé, avec deux formidables trompes sur la face.")
        self.maxhealth = 150
        self.health = self.maxhealth
        self.matorg = 150
        self.baseattack = 30
        self.jetogain = 75
        self.aboneed = 300
        self.abogain = 100
proboscidea_active = Proboscidea("Proboscidea")

# BESTIARY = (Caninae, Casuariidae, BiOurs, Crocaillou, Proboscidea)
BESTIARY = (caninae_active, casuariidae_active, biours_active, crocaillou_active, proboscidea_active)

# num_to_select = 2 # set the number to select here.
# list_of_random_items = random.sample(BESTIARY, num_to_select)
# first_random_item = list_of_random_items[0]
# second_random_item = list_of_random_items[1]



# def choix_bestiary():
#     global adversaire
#     # for i in bestiary.BESTIARY:
#     #     print ("oui !")
#     adversaire_type = random.randint(1, 99)
#     if adversaire_type in range(1, 29):
#         adversaire = bestiary.lutin_active
#     if adversaire_type in range(30, 49):
#         adversaire = bestiary.gobelin_active
#     if adversaire_type in range(50, 64):
#         adversaire = bestiary.orc_active
#     if adversaire_type in range(65, 89):
#         adversaire = bestiary.ogre_active
#     if adversaire_type in range(90, 99):
#         adversaire = bestiary.troll_active
#     ui_attaq()
