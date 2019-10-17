from collections import Counter


class Team:
    def __init__(self, team):
        self.team = team
        self.points = 0
        self.goal_difference = 0

    def __repr__(self):
        return "{0}: {1} ({2})".format(self.team, self.points, self.goal_difference)


eredivisie = [
    "ADO Den Haag - FC Utrecht: 0 - 3",
    "PSV - AZ: 3 - 2",
    "VVV Venlo - Sparta: 3 - 0",
    "Vitesse - NAC Breda: 4 - 1",
    "Heracles Almelo - Ajax: 2 - 1",
    "PEC Zwolle - Roda JC: 4 - 2",
    "Willem II - Excelsior: 1 - 2",
    "Feyenoord - FC Twente: 2 - 1",
    "FC Groningen - SC Heerenveen: 3 - 3",
    "Roda JC - Vitesse: 1 - 3",
    "FC Twente - VVV Venlo: 1 - 2",
    "AZ - ADO Den Haag: 2 - 0",
    "SC Heerenveen - Heracles Almelo: 1 - 1",
    "Excelsior - Feyenoord: 0 - 1",
    "FC Utrecht - Willem II: 2 - 0",
    "Ajax - FC Groningen: 3 - 1",
    "NAC Breda - PSV: 1 - 4",
    "Sparta - PEC Zwolle: 1 - 1",
    "NAC Breda - Sparta: 2 - 2",
    "Vitesse - AZ: 1 - 2",
    "PEC Zwolle - FC Twente: 2 - 0",
    "ADO Den Haag - SC Heerenveen: 1 - 2",
    "Heracles Almelo - Excelsior: 2 - 2",
    "Feyenoord - Willem II: 5 - 0",
    "VVV Venlo - Ajax: 0 - 2",
    "FC Groningen - FC Utrecht: 2 - 1",
    "PSV - Roda JC: 2 - 0",
    "Heracles Almelo - Feyenoord: 2 - 4",
    "Willem II - ADO Den Haag: 1 - 2",
    "Excelsior - Vitesse: 0 - 3",
    "Ajax - PEC Zwolle: 3 - 0",
    "SC Heerenveen - PSV: 2 - 0",
    "AZ - NAC Breda: 2 - 1",
    "Sparta - FC Twente: 1 - 0",
    "FC Utrecht - Roda JC: 2 - 0",
    "FC Groningen - VVV Venlo: 1 - 1",
    "Sparta - AZ: 0 - 2",
    "Excelsior - SC Heerenveen: 1 - 2",
    "NAC Breda - FC Groningen: 2 - 1",
    "Roda JC - Willem II: 1 - 3",
    "PEC Zwolle - Heracles Almelo: 2 - 1",
    "FC Twente - FC Utrecht: 4 - 0",
    "ADO Den Haag - Ajax: 1 - 1",
    "PSV - Feyenoord: 1 - 0",
    "Vitesse - VVV Venlo: 1 - 1",
    "Willem II - SC Heerenveen: 1 - 2",
    "Heracles Almelo - Roda JC: 2 - 1",
    "Feyenoord - NAC Breda: 0 - 2",
    "ADO Den Haag - Sparta: 1 - 0",
    "FC Utrecht - PSV: 1 - 7",
    "FC Groningen - FC Twente: 1 - 0",
    "VVV Venlo - PEC Zwolle: 1 - 1",
    "Ajax - Vitesse: 1 - 2",
    "AZ - Excelsior: 0 - 2",
    "FC Twente - Heracles Almelo: 2 - 1",
    "NAC Breda - ADO Den Haag: 0 - 1",
    "PEC Zwolle - FC Groningen: 3 - 2",
    "PSV - Willem II: 4 - 0",
    "Excelsior - VVV Venlo: 0 - 2",
    "AZ - Feyenoord: 0 - 4",
    "SC Heerenveen - Ajax: 0 - 4",
    "Vitesse - FC Utrecht: 1 - 1",
    "Sparta - Roda JC: 1 - 2",
    "Ajax - Sparta: 4 - 0",
    "Roda JC - NAC Breda: 1 - 0",
    "FC Utrecht - SC Heerenveen: 3 - 1",
    "Feyenoord - PEC Zwolle: 0 - 0",
    "Heracles Almelo - Vitesse: 1 - 1",
    "FC Groningen - AZ: 1 - 1",
    "VVV Venlo - PSV: 2 - 5",
    "Willem II - FC Twente: 3 - 1",
    "ADO Den Haag - Excelsior: 1 - 2",
    "FC Groningen - Willem II: 0 - 1",
    "NAC Breda - PEC Zwolle: 0 - 2",
    "VVV Venlo - ADO Den Haag: 0 - 2",
    "Excelsior - Sparta: 1 - 1",
    "FC Twente - Roda JC: 3 - 0",
    "PSV - Heracles Almelo: 3 - 0",
    "AZ - FC Utrecht: 3 - 0",
    "Feyenoord - Ajax: 1 - 4",
    "SC Heerenveen - Vitesse: 0 - 4",
    "FC Twente - Excelsior: 1 - 3",
    "Roda JC - Feyenoord: 1 - 1",
    "Heracles Almelo - VVV Venlo: 3 - 0",
    "PEC Zwolle - ADO Den Haag: 2 - 0",
    "Willem II - Ajax: 1 - 3",
    "Vitesse - PSV: 2 - 4",
    "Sparta - FC Groningen: 2 - 1",
    "FC Utrecht - NAC Breda: 2 - 2",
    "SC Heerenveen - AZ: 1 - 2",
    "Sparta - SC Heerenveen: 0 - 0",
    "AZ - Willem II: 3 - 2",
    "Excelsior - Roda JC: 1 - 0",
    "Heracles Almelo - FC Groningen: 2 - 1",
    "VVV Venlo - NAC Breda: 0 - 0",
    "ADO Den Haag - Feyenoord: 2 - 2",
    "Vitesse - PEC Zwolle: 0 - 0",
    "Ajax - FC Utrecht: 1 - 2",
    "PSV - FC Twente: 4 - 3",
    "Feyenoord - VVV Venlo: 1 - 1",
    "FC Twente - SC Heerenveen: 0 - 4",
    "Willem II - Sparta: 2 - 2",
    "NAC Breda - Ajax: 0 - 8",
    "ADO Den Haag - Heracles Almelo: 4 - 1",
    "FC Groningen - Vitesse: 4 - 2",
    "FC Utrecht - Excelsior: 3 - 1",
    "PEC Zwolle - PSV: 0 - 1",
    "Roda JC - AZ: 0 - 1",
    "AZ - FC Twente: 2 - 0",
    "VVV Venlo - Willem II: 3 - 3",
    "FC Groningen - Feyenoord: 0 - 2",
    "Heracles Almelo - NAC Breda: 2 - 1",
    "SC Heerenveen - PEC Zwolle: 1 - 2",
    "Ajax - Roda JC: 5 - 1",
    "Sparta - FC Utrecht: 1 - 3",
    "Excelsior - PSV: 1 - 2",
    "Vitesse - ADO Den Haag: 2 - 0",
    "PEC Zwolle - FC Utrecht: 1 - 1",
    "FC Twente - Ajax: 3 - 3",
    "ADO Den Haag - FC Groningen: 0 - 3",
    "Willem II - Heracles Almelo: 3 - 1",
    "Feyenoord - Vitesse: 1 - 0",
    "VVV Venlo - AZ: 0 - 2",
    "Roda JC - SC Heerenveen: 2 - 1",
    "PSV - Sparta: 1 - 0",
    "NAC Breda - Excelsior: 3 - 1",
    "Willem II - NAC Breda: 1 - 1",
    "SC Heerenveen - VVV Venlo: 2 - 2",
    "Excelsior - PEC Zwolle: 1 - 2",
    "AZ - Heracles Almelo: 5 - 0",
    "FC Twente - ADO Den Haag: 2 - 3",
    "Roda JC - FC Groningen: 2 - 2",
    "Ajax - PSV: 3 - 0",
    "NAC Breda - FC Twente: 1 - 2",
    "PEC Zwolle - AZ: 1 - 1",
    "FC Groningen - PSV: 3 - 3",
    "Vitesse - Willem II: 2 - 2",
    "VVV Venlo - FC Utrecht: 0 - 1",
    "ADO Den Haag - Roda JC: 3 - 2",
    "Feyenoord - SC Heerenveen: 1 - 1",
    "Heracles Almelo - Sparta: 3 - 2",
    "Ajax - Excelsior: 3 - 1",
    "Willem II - PEC Zwolle: 2 - 3",
    "SC Heerenveen - NAC Breda: 1 - 0",
    "PSV - ADO Den Haag: 3 - 0",
    "Roda JC - VVV Venlo: 0 - 1",
    "FC Twente - Vitesse: 1 - 1",
    "Sparta - Feyenoord: 0 - 7",
    "AZ - Ajax: 1 - 2",
    "FC Utrecht - Heracles Almelo: 1 - 1",
    "Excelsior - FC Groningen: 2 - 0",
    "ADO Den Haag - PEC Zwolle: 4 - 0",
    "NAC Breda - FC Utrecht: 3 - 1",
    "PSV - Vitesse: 2 - 1",
    "AZ - SC Heerenveen: 3 - 1",
    "Excelsior - FC Twente: 0 - 0",
    "FC Groningen - Sparta: 4 - 0",
    "VVV Venlo - Heracles Almelo: 3 - 1",
    "Ajax - Willem II: 3 - 1",
    "Feyenoord - Roda JC: 5 - 1",
    "Sparta - Vitesse: 0 - 1",
    "FC Utrecht - AZ: 1 - 1",
    "Roda JC - FC Twente: 1 - 1",
    "ADO Den Haag - VVV Venlo: 1 - 1",
    "PEC Zwolle - NAC Breda: 1 - 0",
    "Vitesse - SC Heerenveen: 1 - 1",
    "Sparta - Excelsior: 2 - 3",
    "Ajax - Feyenoord: 2 - 0",
    "Willem II - FC Groningen: 1 - 1",
    "Heracles Almelo - PSV: 1 - 2",
    "FC Utrecht - Feyenoord: 1 - 1",
    "SC Heerenveen - Sparta: 2 - 1",
    "FC Groningen - Heracles Almelo: 3 - 3",
    "PEC Zwolle - Vitesse: 1 - 2",
    "FC Twente - PSV: 0 - 2",
    "NAC Breda - VVV Venlo: 0 - 1",
    "FC Utrecht - Ajax: 0 - 0",
    "Roda JC - Excelsior: 2 - 1",
    "Feyenoord - ADO Den Haag: 3 - 1",
    "Willem II - AZ: 0 - 2",
    "Vitesse - FC Groningen: 2 - 0",
    "SC Heerenveen - FC Twente: 1 - 0",
    "PSV - PEC Zwolle: 4 - 0",
    "Heracles Almelo - ADO Den Haag: 1 - 1",
    "Excelsior - FC Utrecht: 2 - 2",
    "VVV Venlo - Feyenoord: 1 - 0",
    "Sparta - Willem II: 1 - 0",
    "AZ - Roda JC: 2 - 2",
    "Ajax - NAC Breda: 3 - 1",
    "PEC Zwolle - SC Heerenveen: 3 - 2",
    "PSV - Excelsior: 1 - 0",
    "FC Utrecht - Sparta: 1 - 0",
    "FC Twente - AZ: 0 - 4",
    "Roda JC - Ajax: 2 - 4",
    "NAC Breda - Heracles Almelo: 6 - 1",
    "Willem II - VVV Venlo: 3 - 0",
    "ADO Den Haag - Vitesse: 1 - 0",
    "Feyenoord - FC Groningen: 3 - 0",
    "FC Utrecht - PEC Zwolle: 2 - 1",
    "Heracles Almelo - Willem II: 1 - 0",
    "Sparta - PSV: 1 - 2",
    "AZ - VVV Venlo: 0 - 0",
    "SC Heerenveen - Roda JC: 1 - 1",
    "Ajax - FC Twente: 2 - 1",
    "Excelsior - NAC Breda: 0 - 0",
    "Vitesse - Feyenoord: 3 - 1",
    "FC Groningen - ADO Den Haag: 0 - 0",
    "VVV Venlo - FC Groningen: 1 - 1",
    "Vitesse - Excelsior: 1 - 2",
    "PSV - SC Heerenveen: 2 - 2",
    "NAC Breda - AZ: 1 - 3",
    "ADO Den Haag - Willem II: 2 - 1",
    "Roda JC - FC Utrecht: 1 - 4",
    "FC Twente - Sparta: 1 - 1",
    "Feyenoord - Heracles Almelo: 1 - 0",
    "PEC Zwolle - Ajax: 0 - 1",
    "FC Groningen - NAC Breda: 1 - 1",
    "AZ - Sparta: 2 - 1",
    "Heracles Almelo - PEC Zwolle: 2 - 1",
    "SC Heerenveen - Excelsior: 0 - 1",
    "VVV Venlo - Vitesse: 2 - 2",
    "Ajax - ADO Den Haag: 0 - 0",
    "Willem II - Roda JC: 1 - 0",
    "Feyenoord - PSV: 1 - 3",
    "FC Utrecht - FC Twente: 3 - 1",
    "Roda JC - Heracles Almelo: 0 - 3",
    "Excelsior - AZ: 1 - 2",
    "PSV - FC Utrecht: 3 - 0",
    "NAC Breda - Feyenoord: 2 - 1",
    "SC Heerenveen - Willem II: 2 - 0",
    "PEC Zwolle - VVV Venlo: 1 - 1",
    "Vitesse - Ajax: 3 - 2",
    "Sparta - ADO Den Haag: 2 - 1",
    "FC Twente - FC Groningen: 1 - 1",
    "Heracles Almelo - FC Twente: 2 - 1",
    "ADO Den Haag - NAC Breda: 0 - 2",
    "Willem II - PSV: 5 - 0",
    "VVV Venlo - Excelsior: 2 - 3",
    "Roda JC - Sparta: 0 - 2",
    "FC Groningen - PEC Zwolle: 2 - 0",
    "Ajax - SC Heerenveen: 4 - 1",
    "FC Utrecht - Vitesse: 5 - 1",
    "Feyenoord - AZ: 2 - 1",
    "Excelsior - ADO Den Haag: 1 - 2",
    "FC Twente - Willem II: 2 - 2",
    "Vitesse - Heracles Almelo: 0 - 0",
    "PSV - VVV Venlo: 3 - 0",
    "SC Heerenveen - FC Utrecht: 2 - 2",
    "AZ - FC Groningen: 3 - 2",
    "NAC Breda - Roda JC: 0 - 1",
    "Sparta - Ajax: 2 - 5",
    "PEC Zwolle - Feyenoord: 3 - 4",
    "Vitesse - Roda JC: 0 - 3",
    "PEC Zwolle - Sparta: 2 - 0",
    "PSV - NAC Breda: 5 - 1",
    "ADO Den Haag - AZ: 0 - 3",
    "Willem II - FC Utrecht: 3 - 2",
    "VVV Venlo - FC Twente: 0 - 0",
    "FC Groningen - Ajax: 1 - 2",
    "Heracles Almelo - SC Heerenveen: 1 - 2",
    "Feyenoord - Excelsior: 5 - 0",
    "Excelsior - Willem II: 2 - 1",
    "NAC Breda - Vitesse: 1 - 0",
    "AZ - PSV: 2 - 3",
    "Roda JC - PEC Zwolle: 3 - 2",
    "Sparta - VVV Venlo: 3 - 2",
    "FC Utrecht - ADO Den Haag: 3 - 3",
    "SC Heerenveen - FC Groningen: 1 - 1",
    "FC Twente - Feyenoord: 1 - 3",
    "Ajax - Heracles Almelo: 1 - 0",
    "Heracles Almelo - AZ: 0 - 3",
    "ADO Den Haag - FC Twente: 2 - 1",
    "VVV Venlo - SC Heerenveen: 0 - 2",
    "Vitesse - Sparta: 7 - 0",
    "PEC Zwolle - Excelsior: 1 - 1",
    "NAC Breda - Willem II: 1 - 2",
    "FC Groningen - Roda JC: 2 - 1",
    "Feyenoord - FC Utrecht: 3 - 1",
    "PSV - Ajax: 3 - 0",
    "FC Twente - PEC Zwolle: 2 - 0",
    "SC Heerenveen - ADO Den Haag: 2 - 0",
    "Roda JC - PSV: 2 - 2",
    "AZ - Vitesse: 4 - 3",
    "Excelsior - Heracles Almelo: 2 - 2",
    "Sparta - NAC Breda: 2 - 1",
    "Willem II - Feyenoord: 1 - 5",
    "FC Utrecht - FC Groningen: 1 - 1",
    "Ajax - VVV Venlo: 4 - 1",
    "ADO Den Haag - PSV: 3 - 3",
    "FC Groningen - Excelsior: 4 - 0",
    "VVV Venlo - Roda JC: 1 - 4",
    "Vitesse - FC Twente: 5 - 0",
    "Heracles Almelo - FC Utrecht: 2 - 2",
    "Ajax - AZ: 3 - 0",
    "PEC Zwolle - Willem II: 0 - 1",
    "NAC Breda - SC Heerenveen: 3 - 0",
    "Feyenoord - Sparta: 3 - 1",
    "FC Twente - NAC Breda: 1 - 1",
    "Roda JC - ADO Den Haag: 2 - 3",
    "Excelsior - Ajax: 1 - 2",
    "PSV - FC Groningen: 0 - 0",
    "Willem II - Vitesse: 2 - 2",
    "AZ - PEC Zwolle: 6 - 0",
    "Sparta - Heracles Almelo: 2 - 5",
    "FC Utrecht - VVV Venlo: 1 - 0",
    "SC Heerenveen - Feyenoord: 2 - 3"
]

wedstrijden = dict()

for i in eredivisie:
    team1 = i.split(' - ')[0]
    team2 = i.split(' - ')[1].split(":")[0]

    score = i.split(":")[1].split(" ")
    difference = ((int(score[1]), int(score[3])))


    teams = (team1, team2)

    wedstrijden[teams] = difference


uitslagen = dict()
remind = list()

for key, value in wedstrijden.items():


    t1 = key[0]
    t2 = key[1]

    t1_score = value[0]
    t2_score = value[0]

    t1_points = 0
    t2_points = 0

    if t1_score > t2_score:
        t1_points = 30
    elif t1_score < t2_score:
        t2_score = 30
    else:
        t1_points = 1
        t2_points = 1



    if t1 not in remind:
        uitslagen[t1] = [t1_points, t1_score]
    else:
        test = uitslagen.get(t1)
        uitslagen[t1] = [test[0] + t1_points, test[1] + t1_score]

    if t2 not in remind:
        uitslagen[t2] = [t2_points, t2_score]
    else:
        test = uitslagen.get(t2)
        uitslagen[t2] = [test[0] + t2_points, test[1] + t2_score]

    remind.append(t1)
    remind.append(t2)


print(uitslagen)


list_objects = []

for key, value in uitslagen.items():

    team = Team(key)
    team.points = value[0]
    team.goal_difference = value[1]

    list_objects.append(team)

print ("-----------------------------------------")

print (list_objects)




