#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Equipment :
    def armors():
        armors =   {"tissu":{"PRO":2, "ENC":3, "JTS":20},
                    "cuir":{"PRO":4, "ENC":6, "JTS":40},
                    "carbone":{"PRO":8, "ENC":9, "JTS":80},
                    "plastacier":{"PRO":16, "ENC":12, "JTS":160}}

    # armures =   {"tissu":[2, 3, 20],
    #             "cuir":[4, 6, 40],
    #             "carbone":[8, 9, 80],
    #             "plastacier":[16, 12, 160]}

    weapons = {
        "Poignard antique" : 10,
        "Dague en plastacier" : 28,
        "Epée en chitine" : 25,
        "Fleuret de duel" : 70,
        "Epée monofilament" : 99
        }

    serum = {
        "Vivik" : 25,
        "Mortak" : 10
        }
    #
    # ship = (("NAME", "Albatross"),
    #         ("HP", 50),
    #         ("BLASTERS",13),
    #         ("THRUSTERS",18),
    #         ("PRICE",250))
    # ship = collections.OrderedDict(ship)

melee = {
    "Epée Large" : [40, 2],
    "Dague" : [10],
    "Poignard antique" : [2, 5, 20, 10]
    # "Dague en plastacier" 5, 25, 35, 18,
    # "Epée en chitine" : 8, 40, 15, 25,
    # "Fleuret de duel" : 10, 60, 50, 70,
    # "Epée monofilament" : 15, 80, 90, 99
    }
