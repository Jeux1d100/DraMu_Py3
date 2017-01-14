#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import random
import time
import json
from operator import itemgetter

# import avatar
import bestiary
import equipment
import expedition

class Colour:
    BLACK = "\033[98m"
    LGREY = "\033[97m"
    LPURPLE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

class Avatar(object):
    def __init__(self, name):
        self.name = name # Nom de l'ego (avatar du joueur)
        self.maxhealth = 100 # Santé maximum de l'ego
        self.health = 40 # Santé actuelle de l'ego
        self.baseattack = 5 # Attaque de base de l'ego
        self.curweap = "Aucune" # Arme équipée, qui s'ajoute à baseattack
        self.jeto = 50 # total de Jetons, monnaie du DraMu
        self.abo = 0 # total d'abonnés, ressource
        self.matorg = 0 # Total de Matière Organique, ressource
        self.rubujo = 0 # Total de Rubujoj (déchets), ressource
        self.serum = 3 # Total de sérum, potion de soin et autre drogues
        self.buff = 0 # Effet actif sur l'ego
        self.inventory = json.load(open("inventory.txt"))

    # def attack(self):
    #     attack = self.baseattack
    #     if self.curweap == "Aucune":
    #         self.weapdmg += 2
    #     elif self.curweap == "Lii":
    #         self.weapdmg += 10
    #     return attack

    def do_attack():
#        os.system("clear")
        avatar_attack =  ego.baseattack + random.randint(8,12)  # Dégâts de l'ego
        challenger_attack = random.randint(3,5) # Dégâts de l'adversaire

        challenger.health -= avatar_attack
        print ("")
        print ("      Vous infligez " + Colour.GREEN + "%i dégâts " % avatar_attack + Colour.END + "à l'adversaire.")
        #print ("      Vous infligez %i dégâts à l'adversaire !" % avatar_attack)
        if challenger.health < 1:
            win()
        else:
            ego.health -= challenger_attack
            print ("        L'adversaire vous blesse pour " + Colour.RED + "%i dégâts." % challenger_attack + Colour.END)
#            print ("        L'adversaire vous blesse pour %i dégâts !" % challenger_attack)
        if ego.health < 1:
            lose()
        else:
            Avatar.do_attack()

    def do_quit():
#        os.system("clear")
        sys.exit()

def main():
    os.system("clear")
    inventory = {
        'Sword': {'attack': 5, 'defence': 1, 'weight': 15, 'price': 2},
        'Armor': {'attack': 0, 'defence': 10, 'weight': 25, 'price': 5}
        }
    for name, item in inventory.items():
        print ("{0}: {1[attack]} {1[defence]} {1[weight]} {1[price]}".format(name, item))

    print ("Menu")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                        ")
    print (Colour.GREEN + "         DraMu 170110_01                          " + Colour.END)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      n - nouvelle partie                                                  ")
    print ("                                                                           ")
    print ("      q (ou Entrée) - quitter                                              ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    if option =="n":
        avatar_creation_name()
    elif option =="q":
        sys.exit()
    elif option =="aide":
        go_help()
    elif option =="w":
        go_hub()
    elif option =="":
        sys.exit()
    else:
        sys.exit()

def avatar_creation_name():
    os.system("clear")
    print ("Avatar")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print ("      Création de l'avatar.                                            ")
    print ("")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Choisissez un nom -> " + Colour.END)
    while not option :
        option = input(Colour.DARKCYAN + "   Choisissez un nom -> " + Colour.END)
    global ego
    ego = Avatar(option)
    go_hub()
    # AvatarBody.avatar_creation_body()

def go_hub():
    while True:
        os.system("clear")
        # for indice, description in sorted(ego.inventory.items(), key=lambda x: x[0][1][1]):
        #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
        # for indice, description in sorted(ego.inventory.items(), key=lambda x: x[1][1][1]):
        #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
        print ("Antre")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Vous êtes %s, le zum' du jour.                                       " % (ego.name))
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      a - combattre dans l'arène                                           ")
        print ("      b - entrer dans la boutique                                          ")
        print ("      m - développer une mutation                                          ")
        print ("      x - préparer une expédition                                          ")
        print ("      i - voir votre statut et inventaire                                  ")
        print ("      ? - ouvrir une page d'aide                                           ")
        print ("                                                                           ")
        print ("      q (ou Entrée) - quitter DraMu                                                    ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "a":
            select_challenger()
        elif option == "b":
            go_shop()
        elif option == "m":
            go_mutation_prepare()
        elif option == "x":
            go_expedition_prepare()
        elif option == "i":
            go_info()
        elif option == "?":
            go_help()
        elif option == "q": #arrêter le programme et sortir
            sys.exit()
        elif option == "":
            sys.exit()
        else:
            print("      Ce choix n'est pas valide")
            go_hub()

def select_challenger():
    os.system("clear")
    print ("Introduction")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    intro = json.load(open("intro.txt"))
    for i, blabla in sorted(intro.items(), key=lambda x:x[0]):
        print ("{}".format(blabla))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
    global challenger
    challenger = (random.choice(bestiary.BESTIARY))
    # challenger_type = random.randint(1, 99)
    # challenger = bestiary.BESTIARY
    # if challenger_type in range(1, 29):
    #     challenger = bestiary.caninae_active
    # if challenger_type in range(30, 49):
    #     challenger = bestiary.casuariidae_active
    # if challenger_type in range(50, 64):
    #     challenger = bestiary.biours_active
    # if challenger_type in range(65, 89):
    #     challenger = bestiary.crocaillou_active
    # if challenger_type in range(90, 99):
    #     challenger = bestiary.proboscidea_active
    go_arena()

def go_arena():
    os.system("clear")
    print ("Arène")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (" ")
    print ("            %s (%i/%i)   vs   %s (%i/%i)" % (ego.name, ego.health, ego.maxhealth, challenger.name, challenger.health, challenger.maxhealth))
    print (" ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      a (ou Entrée) - attaquer                                                         ")
    print ("      f - fuir et abandonner le combat                                     ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    if option == "a":
        Avatar.do_attack()
    elif option =="":
        Avatar.do_attack()
    elif option == "f":
        Avatar.do_flee()
    else:
        print("      Ce choix n'est pas valide")
        go_arena()

def go_shop():
    os.system("clear")
    print ("Boutique Interface")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("        Échangez vos jetons contre du matériel utilisable !                ")
    print ("                                                                           ")
    print ("        Choisissez simplement l'objet de votre choix,                      ")
    print ("        votre compte sera débité automatiquement.                          ")
    print ("                                                                           ")
    print ("        Veuillez sélectionner la catégorie désirée.                        ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("      | o - Offense | d - Défense | s - Sérum |                            ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour retourner à l'antre" + Colour.END)
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END)
    if option == "o":
        go_shop_off()
    elif option =="d":
        go_shop_def()
    elif option == "s":
        go_shop_serum()
    elif option =="":
        go_hub()
    else:
        print("      Ce choix n'est pas valide")
        go_arena()

def go_shop_off():
    os.system("clear")
    print ("Catégorie : Offensif")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Objet | Prix en jetons JTS | Description               Jetons disponibles : %i   " % ego.jeto)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("         ~ ~ ~ Armes ~ ~ ~                                                 ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    shop_off = json.load(open("shop_off.txt"))
    for indice, description in sorted(shop_off.items(), key=lambda x: x[1][1]):
        print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour retourner à l'interface boutique" + Colour.END)
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END)
    if option == "":
        go_shop()
    elif option in shop_off:
        if ego.jeto >= shop_off[option][0]:
            ego.jeto -= shop_off[option]
            print ("      Vous achetez l'objet %s." % option)
            ego.serum += 1
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
            go_shop()
        else:
            print ("      Vous n'avez pas assez de jetons.")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
            go_shop()
    else:
        print ("      Cet objet n'existe pas !")
        option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
        go_shop()
    return go_shop

def go_shop_def():
    os.system("clear")
    print ("Catégorie : Défensif")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Objet | Prix en jetons JTS | Description               Jetons disponibles : %i   " % ego.jeto)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("         ~ ~ ~ Armures ~ ~ ~                                                 ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    shop_def = json.load(open("shop_def.txt"))
    for indice, description in sorted(shop_def.items(), key=lambda x: x[1][1]):
        print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour retourner à l'interface boutique" + Colour.END)
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END)
    if option == "":
        go_shop()

def go_shop_serum():
    os.system("clear")
    print ("Catégorie : Sérum")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Objet | Prix en jetons JTS | Description               Jetons disponibles : %i   " % ego.jeto)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    print ("          ~ ~ ~ Sérum ~ ~ ~                                                ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    shop_serum = json.load(open("shop_serum.txt"))
    for indice, description in sorted(shop_serum.items(), key=lambda x: x[1][1]):
        print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour retourner à l'interface boutique" + Colour.END)
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END)
    if option == "":
        go_shop()
    elif option in shop_serum:
        if ego.jeto >= shop_serum[option][1]:
            ego.jeto -= shop_serum[option][1]
            print ("      Vous achetez l'objet " + Colour.GREEN + "{} ".format(description[0]) + Colour.END + "pour " + Colour.RED + "{} jetons".format(description[1]) + Colour.END + ".")
            ego.serum += 1
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
            go_shop()
        else:
            print ("      Vous n'avez pas assez de jetons.")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
            go_shop()
    else:
        print ("      Cet objet n'existe pas !")
        option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
        go_shop()
    return go_shop

def go_mutation_prepare():
    print ("Mutation !")
    time.sleep(2)
    pass

def go_help():
    os.system("clear")
    print ("Aide")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("        Vocabulaire et termes employés                                     ")
    print ("                                                                           ")
    print ("        Zum', rubujo... sont des mots en langue espéranto (http://esperanto-france.org/)     ")
    print ("        Zumo = bourdonnement, utilisé au ici au sens de ""buzz sur internet""  ")
    print ("        Rubujo = dêchet, rebu, poubelle. Utilisé pour nommer une ressource, des bidules de récupération...")
    print ("                                                                           ")
    print ("                                                                           ")
    print ("                                                                           ")
    print ("                                                                           ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    go_hub()


def do_serum():
    if ego.serum > 0 :
        ego.serum -= 1
        if ego.health > ego.maxhealth :
            ego.health == ego.maxhealth
            go_info()
        else :
            ego.health += 50
            print ("      Vous injectez le sérum et constatez un effet " + Colour.GREEN + "positif " + Colour.END + "sur votre organisme.")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
            go_info()
    else :
        print ("      Vous n'en avez pas. Vous pouvez échanger vos jetons à la boutique contre du sérum.")
        option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
        go_info()
#    return go_info()


def go_expedition_prepare():
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    expedition.ExpeditionPrepare.expedition_prepare()

def go_info():
    os.system("clear")
    print ("Info")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("            %s (%i/%i), effects actifs : %s                                " % (ego.name, ego.health, ego.maxhealth, ego.buff))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Arme Actuelle : %s (+%i DGT)                                         " % (ego.curweap, ego.baseattack))
    print ("      Jetons : %i   |   Abonnés : %i   |   Matorg : %i   |   Rubujo : %i   " % (ego.jeto, ego.abo, ego.matorg, ego.rubujo))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      s - injecter un sérum (reste %s)                                     " % (ego.serum))
    print ("      t (ou Entrée) - retourner à l'antre                                  ")
    print ("")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    if option == "s":
        do_serum()
    elif option == "t":
        go_hub()
    elif option =="":
        go_hub()
    else:
        print("Ce choix n'est pas valide")
        go_info()

def win():
#    os.system("clear")
    ego.abo += challenger.abogain
    ego.jeto += challenger.jetogain
    ego.matorg += (challenger.matorg/2)
    print ("                                                                           ")
    print ("Victoire")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("            %s (%i/%i)   vs   %s (%i/%i)" % (ego.name, ego.health, ego.maxhealth, challenger.name, challenger.health, challenger.maxhealth))
    print ("                                                                           ")
    print ("      Vous avez vaincu votre adversaire %s.                                " % challenger.name)
    print ("      Vous avez %s nouveaux abonnés.                                       " % challenger.abogain)
    print ("      Votre récompense pour ce combat est de %i jetons.                    " % challenger.jetogain)
    print ("      Vous assimilez %i matorg.                                            " % (challenger.matorg/2))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    challenger.health = challenger.maxhealth
    ego.buff += 2
    if ego.buff > 1 :
        ego.health += (ego.buff)
        if ego.health > ego.maxhealth :
            ego.health = ego.maxhealth
    go_hub()

def lose():
    #os.system("clear")
    if ego.abo < 1 :
        ego.abo -= challenger.abogain/2
    else :
        ego.abo == 0
    if ego.jeto < 1 :
        ego.jeto += challenger.jetogain
    else :
        ego.jeto = 0
    if ego.matorg < 1 :
        ego.matorg -= challenger.matorg
    else :
        ego.matorg = 0
    ego.buff -= 3
    if ego.buff < 1 :
        ego.health += ego.buff
        if ego.health < 1 :
            option = input(Colour.DARKCYAN + "   P A R T I E   T E R M I N É E..." + Colour.END)
            sys.exit()
        else :
            print ("                                                                           ")
            print ("Défaite")
            print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("                                                                           ")
            print ("            %s (%i/%i)   vs   %s (%i/%i)" % (ego.name, ego.health, ego.maxhealth, challenger.name, challenger.health, challenger.maxhealth))
            print ("                                                                           ")
            print ("      Vous tombez face à votre adversaire. Vous perdez %i abonnés !        " % challenger.abogain)
            print ("      Votre compensation pour participer à ce combat est de %i jetons.     " % challenger.jetogain)
            print ("      Vos blessures vous font perdre %i matorg.                            " % challenger.matorg)
            print ("                                                                           ")
            print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("                                                                           ")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
            challenger.health = challenger.maxhealth
            go_hub()

class AvatarBody(object):

    def avatar_creation_body():
        os.system("clear")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("      Choisissez maintenant les éléments composants votre corps.       ")
        print ("      Vous pouvez choisir plusieurs fois le même élément.              ")
        print ("      Séparez vos choix par des espaces;                               ")
        print ("      Exemple, votre choix -> corne dent dent                          ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("      Vous allez choisir 3 outils, 2 sens et 1 enveloppe.              ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
        AvatarBody.tool_choice()

    def tool_choice():
        os.system("clear")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("      Choisissez trois outils :                         ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("   -> corne griffe queue dent ventouse dard main pince crochet        ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        tool_list = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).split()
        if len(tool_list) == 3:
            tool1, tool2, tool3 = tool_list
            for tool in tool_list:
                if tool not in ("corne", "griffe", "queue", "dent", "ventouse", "dard", "main", "pince", "crochet"):
                    print ("   Au moins un de vos choix n'est pas valide. Veuillez recommencer.")
                    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
                    os.system("clear")
                    AvatarBody.tool_choice()
            else:
                AvatarBody.sens_choice()
        else :
            print ("   Au moins un de vos choix n'est pas valide. Veuillez recommencer.")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
            os.system("clear")
            AvatarBody.tool_choice()

    def sens_choice():
        os.system("clear")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("      Choisissez deux organes sensoriels :                             ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("   -> vue ouïe toucher odorat goût sonar thermos radios magnos         ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        sens_list = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).split()
        if len(sens_list) == 2:
            sens1, sens2 = sens_list
            for sens in sens_list:
                if sens not in ("vue", "ouïe", "toucher", "odorat", "goût", "sonar", "thermos", "radios", "magnos"):
                    print ("   Au moins un de vos choix n'est pas valide. Veuillez recommencer.")
                    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
                    os.system("clear")
                    AvatarBody.skin_choice()
            else:
                AvatarBody.skin_choice()
        else:
            print ("   Au moins un de vos choix n'est pas valide. Veuillez recommencer.")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
            os.system("clear")
            AvatarBody.sens_choice()

    def skin_choice():
        os.system("clear")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("      Choisissez une enveloppe, matière qui recouvre votre corps :     ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("   -> peau poils plumes écailles cuir fourrure plaques cheveux tissu   ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        skin_list = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).split()
        if len(skin_list) == 1:
            skin1 = skin_list
            for skin in skin_list:
                if skin not in ("peau", "poils", "plumes", "écailles", "cuir", "fourrure", "plaques", "cheveux", "tissu"):
                    print ("   Au moins un de vos choix n'est pas valide. Veuillez recommencer.")
                    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
                    os.system("clear")
                    AvatarBody.skin_choice()
            else:
                AvatarBody.body_resume()
        else:
            print ("   Au moins un de vos choix n'est pas valide. Veuillez recommencer.")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
            os.system("clear")
            AvatarBody.skin_choice()

    def body_resume():
        os.system("clear")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        print ("      La création de votre ego est terminée.                           ")
        print ("                                                                       ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                       ")
        # print ("%s, la nature vous a doté des éléments suivants :" % (ego.name))
        # print ("- trois outils ou accessoires : %s, %s, %s." % (tool1, tool2, tool3))
        # print ("- deux organes de sens : %s, %s, %s." % (sens1, sens2))
        # print ("- Votre corps est recouvert de : %s." % (skin1))
        # option=input("")
        option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
        go_hub()

if __name__ == '__main__':
	main()
