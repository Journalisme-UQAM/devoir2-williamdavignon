# coding: utf-8

import csv, json
import requests

fichier = "lobby_inst.csv"

entetes = {
    "User-agent":"William dAvignon requete envoye dans le cadre dun cours de journalisme.",
    "From":"william.davignon@gmail.com"
}


# "http://jhroy.ca/uqam/lobby.json"
# truc qu'on cherche'

# code de l'organisation lobbyiste
# nom de l'organisation lobbyiste en français
# nom de l'organisation lobbyiste en anglais
# date à laquelle la communication a eu lieu
# sujet principal
# sujet autre
# l'institution visée (optionnel)
url = "http://jhroy.ca/uqam/lobby.json"
lobby = requests.get(url,headers=entetes)
ls = lobby.json()
n = 0
x = 1
for cas in ls["registre"]:
    if "limat" in str(cas):
        code = ls["registre"][n][0]["client_org_corp_num"]
        orgF = ls["registre"][n][0]["fr_client_org_corp_nm"]
        orgA = ls["registre"][n][0]["en_client_org_corp_nm"]
        date= ls["registre"][n][0]["date_comm"]
        sujetP = list()
        sujetA = list()
        inst = list()
        insnb = 0
        suj = 0
        for obj in list(ls["registre"][n][1]):
            sujetP.append(ls["registre"][n][1][suj]["objet"])
            sujetA.append(ls["registre"][n][1][suj]["objet_autre"])
            suj += 1
        for ins in list(ls["registre"][n][2]):
            inst.append(ls["registre"][n][2][insnb]["institution"])
            insnb += 1

        # print(code, orgF, orgA, date, sujetP, sujetA)             <-- test    
        x += 1
        skits = list()
        skits.append(code)
        skits.append(orgF)
        skits.append(orgA)
        skits.append(date)
        skits.append(sujetP)
        skits.append(sujetA)
        skits.append(inst)

        dead = open(fichier, "a")
        obies = csv.writer(dead)
        obies.writerow(skits)
    n += 1
# print (n, x)                      <--- tout    des tests

# testEffa = ls["registre"][500]
# print(testEffa)
