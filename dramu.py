#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import random
import time
import json

# import avatar
import bestiary
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

        self.baseattack = 5 # Attaque de base de l'ego
        self.curweap = "Aucune" # Arme équipée, qui s'ajoute à baseattack

        self.jeto = 50 # total de Jetons, monnaie du DraMu
        self.abo = 100 # total d'abonnés, ressource
        self.safeabo = 1
        self.matorg = 50 # actuelle Matière Organique, ressource vitale
        self.maxmatorg = 100
        
        self.nerf = 0 # Cerveau (Action + Agilité)
        self.fluide = 0 # Cœur (Puissance + Résistance)
        self.chimie = 0 # Glande (Pouvoir + Cohésion)
        self.gaz = 0 # Poumon (Endurance + Résérve)

        self.rubujo = 0 # Total de Rubujoj (déchets), ressource
        self.serum = 3 # Total de sérum, potion de soin et autre drogues
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
        ego_attack =  ego.baseattack + random.randint(9,16)  # Dégâts de l'ego
        challenger_attack = challenger.baseattack + random.randint(1,8) # Dégâts de l'adversaire

        while ego.matorg > 0 :
            challenger.health -= ego_attack
            print ("")
            print ("      Vous infligez " + Colour.GREEN + "{} dégâts ".format(ego_attack) + Colour.END + "à l'adversaire.")
            if challenger.health < 1:
                win()
            else:
                ego.matorg -= challenger_attack
                print ("        L'adversaire vous blesse pour " + Colour.RED + "{} dégâts.".format(challenger_attack) + Colour.END)
        
            if ego.matorg < 1:
                lose()
            else :
                Avatar.do_attack()

    def do_quit():
#        os.system("clear")
        sys.exit()

def main():
    os.system("clear")
    print ("Menu")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                        ")
    print (Colour.YELLOW + "    DraMu 1701_01 | Développé par Tchey | http://jeux1d100.net" + Colour.END)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      n - nouvelle partie                                                  ")
    print ("                                                                           ")
    print ("      q - quitter                                              ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour commencer une nouvelle partie" + Colour.END)
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
        avatar_creation_name()
    else:
        main()

def avatar_creation_name():
    os.system("clear")
    print ("Avatar")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print ("      Création de l'avatar.                                            ")
    print ("")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    print (Colour.DARKCYAN + "   Touche Entrée pour le nom par défaut : Vakog" + Colour.END)
    option = input(Colour.DARKCYAN + "   Choisissez un nom -> " + Colour.END)
    while not option :
        option = "Vakog"
    global ego
    ego = Avatar(option)
    go_hub()
    # AvatarBody.avatar_creation_body()

def go_hub():
    while True:
        os.system("clear")
        taxe = 20
        # for indice, description in sorted(ego.inventory.items(), key=lambda x: x[0][1][1]):
        #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
        # for indice, description in sorted(ego.inventory.items(), key=lambda x: x[1][1][1]):
        #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
        print ("Antre")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Vous êtes {}, le zum' du jour, et vous avez {}/{} matorg.             ".format(ego.name, ego.matorg, ego.maxmatorg))
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Jetons : {}   |   Abonnés : {}   |   Rubujo : {}                     ".format(ego.jeto, ego.abo, ego.rubujo))
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      a - combattre dans l'arène " + Colour.LPURPLE + "(activité soumise à la taxe universelle d'organisation : " + Colour.END + Colour.RED + "{} JTS".format(taxe) + Colour.END + ")")
        print ("      b - entrer dans la boutique " + Colour.LPURPLE + "(matériel certifié conforme aux réglementations en vigueur)" + Colour.END)
        print ("      m - développer une mutation " + Colour.LPURPLE + "(science expérimentale, résultats non garantis)" + Colour.END)
        print ("      x - préparer une expédition " + Colour.LPURPLE + "(la responsabilité du système ne saurait être engagée)" + Colour.END)
        print ("      i - consulter l'inventaire " + Colour.LPURPLE + "(synchronisation aux serveurs sous réserve)" + Colour.END)
        print ("      ? - ouvrir une page d'aide " + Colour.LPURPLE + "(sources anonymes, informations non contractuelles)" + Colour.END)
        print ("                                                                           ")
        print ("      q - quitter DraMu " + Colour.LPURPLE + "(assistance psychomédicale à la charge de l'utilisateur)" + Colour.END)
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Touche Entrée pour combattre dans l'arène" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()

        if option == "":
            if ego.jeto > taxe :
                ego.jeto -= taxe
                select_challenger()
            else :
                option = input(Colour.DARKCYAN + "   Vous ne pouvez pas vous acquitter de la taxe universelle d'organisation. " + Colour.END).lower()
                go_hub()
        elif option == "a":
            if ego.jeto > taxe :
                ego.jeto -= taxe
                select_challenger()
            else :
                option = input(Colour.DARKCYAN + "   Vous ne pouvez pas vous acquitter de la taxe universelle d'organisation. " + Colour.END).lower()
                go_hub()
        elif option == "b":
            go_shop()
        elif option == "m":
            go_mutation_prepare()
        elif option == "x":
            go_expedition_prepare()
        elif option == "i":
            go_hub()
        elif option == "?":
            go_help()
        elif option == "q": #arrêter le programme et sortir
            sys.exit()
        else:
            print("      Ce choix n'est pas valide")
            go_hub()

def select_challenger():
    os.system("clear")
    print ("Introduction")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Vous payez la taxe universelle d'organisation, d'un montant de " + Colour.RED + "20 JTS" + Colour.END + ".")
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
    print ("            {} ({}/{})   vs   {} ({}/{})                    ".format(ego.name, ego.matorg, ego.maxmatorg, challenger.name, challenger.health, challenger.maxhealth))
    print (" ")
    print ("    {}                                                              ".format(challenger.description))
    print (" ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      a - attaquer                                                         ")
    print ("      f - fuir et abandonner le combat                                     ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour attaquer" + Colour.END)
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
    # os.system("clear")
    # print ("Catégorie : Offensif")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                           ")
    # print ("      Objet | Prix en jetons JTS | Description               Jetons disponibles : {}           ".format(ego.jeto))
    # print ("                                                                           ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("         ~ ~ ~ Armes ~ ~ ~                                                 ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                           ")
    # shop_off = json.load(open("shop_off.txt"))
    # for indice, description in sorted(shop_off.items(), key=lambda x: x[1][1]):
    #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
    # print ("                                                                           ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                           ")
    # print (Colour.DARKCYAN + "   Touche Entrée pour retourner à l'interface boutique" + Colour.END)
    # option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END)
    # if option == "":
    #     go_shop()
    # elif option in shop_off:
    #     if ego.jeto >= shop_off[option][0]:
    #         ego.jeto -= shop_off[option]
    #         print ("      Vous achetez l'objet {}.".format(option)
    #         ego.serum += 1
    #         option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    #         go_shop()
    #     else:
    #         print ("      Vous n'avez pas assez de jetons.")
    #         option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    #         go_shop()
    # else:
    #     print ("      Cet objet n'existe pas !")
    #     option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    #     go_shop()
    # return go_shop
    pass

def go_shop_def():
    os.system("clear")
    # shop_def = json.load(open("shop_def.txt"))
    # for name, item in shop_def():
    #     print ("{0} - {1[id]} : {1[name]}   JTS {1[price]} x{1[quantity]} ({1[description]})".format(name, item))
    print ("Catégorie : Défensif")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Objet | Prix en jetons JTS | Description               Jetons disponibles : {}           ".format(ego.jeto))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("         ~ ~ ~ Armures ~ ~ ~                                                 ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    # shop_def = json.load(open("shop_def.txt"))
    # for indice, description in sorted(shop_def.items(), key=lambda x: x[1][1]):
    #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
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
    print ("      Objet | Prix en jetons JTS | Description               Jetons disponibles : {}           ".format(ego.jeto))
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
            ego.inventory[option] = 1
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
    print (Colour.YELLOW + "      Vocabulaire et termes employés                       " + Colour.END)
    print ("                                                                           ")
    print ("        Zum', rubujo... sont des mots en langue espéranto (http://esperanto-france.org/)     ")
    print ("        Zumo = bourdonnement, utilisé au ici au sens de ""buzz sur internet""  ")
    print ("        Rubujo = dêchet, rebu, poubelle. Utilisé pour nommer une ressource, des bidules de récupération...")
    print ("                                                                           ")
    print (Colour.YELLOW + "      Règles du jeu                                        " + Colour.END)
    print ("                                                                           ")
    print ("        Combattez dans l'arène pour gagner des abonnés et des jetons.      ")
    print ("        A chaque victoire, vous assimilez la matorg de l'adversaire,       ")
    print ("        ce qui permet de régénérer. A chaque défaite, vous en perdez.      ")
    print ("                                                                           ")
    print ("        Si vous n'avez plus de matorg, mais que vous êtes populaire,       ")
    print ("        certains abonnés se sacrifient pour vous permettre de vivre.       ")
    print ("                                                                           ")
    print ("        Si vous n'avez ni matorg, ni abonnés, c'est la fin du zum',        ")
    print ("        il est temps de laisser la place à un nouveau mutant.              ")
    print ("                                                                           ")
    print ("        Jetons, rubujoj, mutations... feront l'objet de prochaines         ")
    print ("        mises à jour.                                                      ")
    print ("                                                                           ")
    print ("                                                       - en construction - ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    go_hub()


def do_serum():
    if ego.serum > 0 :
        ego.serum -= 1
        if ego.matorg > ego.maxmatorg :
            ego.matorg == ego.maxmatorg
            go_info()
        else :
            ego.matorg += 50
            print ("      Vous injectez le sérum et constatez un effet " + Colour.GREEN + "positif " + Colour.END + "sur votre organisme.")
            option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
            go_info()
    else :
        print ("      Vous n'en avez pas. Vous pouvez échanger vos jetons à la boutique contre du sérum.")
        option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
        go_info()


def go_expedition_prepare():
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    expedition.ExpeditionPrepare.expedition_prepare()

def go_info():
    os.system("clear")
    # print ("Info")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                           ")
    # print ("            {} ({}/{} MatOrg)                                                     ".format(ego.name, ego.matorg, ego.maxmatorg))
    # print ("                                                                           ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                           ")
    # print ("      Arme Actuelle : {} (+{} DGT)                                         ".format(ego.curweap, ego.baseattack))
    # print ("      Jetons : {}   |   Abonnés : {}   |   Rubujo : {}                     ".format(ego.jeto, ego.abo, ego.rubujo))
    # print ("                                                                           ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                           ")
    # print ("      s - injecter un sérum (reste {})                                     ".format(ego.serum))
    # print ("      t (ou Entrée) - retourner à l'antre                                  ")
    # print ("                                                                           ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                           ")
    # option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    # if option == "s":
    #     do_serum()
    # elif option == "t":
    #     go_hub()
    # elif option =="":
    #     go_hub()
    # else:
    #     print("Ce choix n'est pas valide")
    #     go_info()
    pass

def win():
#    os.system("clear")
    ego.abo += challenger.abogain
    ego.jeto += challenger.jetogain
    if ego.matorg < ego.maxmatorg :
        ego.matorg += challenger.matorg
    if ego.matorg > ego.maxmatorg :
        ego.matorg = ego.maxmatorg
    print ("                                                                           ")
    print (Colour.GREEN + "  ! Victoire !   ! Victoire !   ! Victoire !   ! Victoire !   ! Victoire !" + Colour.END)
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("            {} ({}/{})   vs   {} ({}/{})                                   ".format(ego.name, ego.matorg, ego.maxmatorg, challenger.name, challenger.health, challenger.maxhealth))
    print ("                                                                           ")
    print ("      Vous avez vaincu votre adversaire {}.                                ".format(challenger.name))
    print ("      Vous avez de " + Colour.GREEN + "nouveaux abonnés : {}".format(challenger.abogain) + Colour.END + ".")
    print ("      Votre récompense pour ce combat est de " + Colour.GREEN + "{} jetons".format(challenger.jetogain) + Colour.END + ".")
    print ("      Vous assimilez " + Colour.GREEN + "{} matorg".format(challenger.matorg) + Colour.END + ".")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    challenger.health = challenger.maxhealth 
    go_hub()

def lose():
    #os.system("clear")
    # if ego.matorg < 1 :
    #     print ("    - Vous êtes détruit, il ne reste rien de vous. F I N -   ")
    #     sys.exit()   
    if ego.abo > int(challenger.abogain/20) :
        ego.abo -= int(challenger.abogain/20)
    else :
        ego.abo = 1
    ego.safeabo = 1 + int(ego.abo /10)
    ego.matorg = ego.safeabo
    ego.jeto += int(challenger.jetogain/4)
    print ("                                                                           ")
    print (Colour.RED + "  ! Défaite !   ! Défaite !   ! Défaite !   ! Défaite !   ! Défaite !" + Colour.END)
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("            {} ({}/{})   vs   {} ({}/{})                        ".format(ego.name, ego.matorg, ego.maxmatorg, challenger.name, challenger.health, challenger.maxhealth))
    print ("                                                                           ")
    print ("      L'adversaire vous domine. Vous perdez des " + Colour.RED + "abonnés potentiels : -{}".format(int(challenger.abogain/20)) + Colour.END + ".")
    print ("      Votre compensation pour participer à ce combat est de " + Colour.GREEN + "{} jetons".format(int(challenger.jetogain/4)) + Colour.END + ".")
    print ("      Quelques-uns de vos plus fervents abonnés se sacrifient,")
    print ("      vous permettant de repartir avec " + Colour.GREEN + "{} matorg".format(ego.safeabo) + Colour.END + ".")
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
        print ("   -> corne griffe queue dent ventouse dard main pince crochet         ")
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
        # print ("{}, la nature vous a doté des éléments suivants :".format(ego.name))
        # print ("- trois outils ou accessoires : {}, {}, {}.".format(tool1, tool2, tool3))
        # print ("- deux organes de sens : {}, {}, {}.".format(sens1, sens2))
        # print ("- Votre corps est recouvert de : {}.".format(skin1))
        # option=input("")
        option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END).lower()
        go_hub()

if __name__ == '__main__':
	main()
