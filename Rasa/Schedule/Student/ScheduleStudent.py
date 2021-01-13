import json
import requests
from Schedule.Student import EnumStudent
from datetime import datetime,timedelta


def parseRequest(data):
        dateToday = datetime.today().strftime('%Y-%m-%d')
        time = dateToday[11:13]
        timeEnd = ""
        if (time >= "12"):
                time = "12"
                timeEnd = "19"
        else:
                time = "07"
                timeEnd = "12"

        message = ""
        findCour = False
        for i in data["results"]:
                if (i["start"][:10] == dateToday[:10]):
                        if ((i["start"][11:13] >= time) & (i["start"][11:13] <= timeEnd)):
                                heureDebut = i["start"][11] + str((int(i["start"][12])) + 1) + i["start"][13:16]
                                heureFin = i["end"][11] + str((int(i["end"][12])) + 1) + i["end"][13:16]
                                typeCour = i["type"]
                                listLigneCour = i["title"].split('\n')
                                ligneCour = listLigneCour[0]
                                for i in listLigneCour:
                                        if ("Salle" in i):
                                                salleCour = i
                                message = message + ("Tu as un " + typeCour + " en " + ligneCour + " qui commence à " +
                                                     heureDebut + " et qui se termine à " + heureFin + " dans la (les) " + salleCour + "\n")
                                findCour = True

        if findCour is False:
                return "Tu n'as pas de cour"
        return (message)

def ask_schedule_student(text) :
        urlApiPromotion = "https://edt-api.univ-avignon.fr/app.php/api/events_promotion/"
        urlApiGroupe = "https://edt-api.univ-avignon.fr/app.php/api/events_tdoption/"

        text = text.lower()
        print(text)
        if ("l1") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.L1.value)
        if( "l1 g1" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L1G1.value)
        if( "l1 g2" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L1G2.value)
        if( "l1 g3" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L1G3.value)
        if( "l1 g4" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L1G4.value)
        if( "l1 g5" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L1G5.value)
        if( "l1 g6" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L1G6.value)
        if ("l2") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.L2.value)
        if( "l2 g1" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L2G1.value)
        if( "l2 g2" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L2G2.value)
        if( "l2 g3" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L2G3.value)
        if( "l2 g3" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L2G4.value)
        if ("l3") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.L3.value)
        if( "l3 g1" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3G1.value)
        if( "l3 g2" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3G2.value)
        if( "l3 g3" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3G3.value)
        if( "l3 g4" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3G4.value)
        if( "l3 g5" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3G5.value)
        if( "l3 e1" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3E1.value)
        if( "l3 e2" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3E2.value)
        if( "l3 e3" in text ) :
                url = urlApiGroupe + str(EnumStudent.Groupe.L3E3.value)
        if ("m1 ingénierie logiciel") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M1_ILSEN.value)
        if ("m2 ingénierie logiciel") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M2_ILSEN.value)
        if ("m1 réseau") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M1_SICOM.value)
        if ("m2 réseau") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M2_SICON.value)
        if ("m1 intelligence artificielle") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M1_IA.value)
        if ("m2 intelligence artificielle") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M2_IA.value)
        if ("m1 réseau classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_SICON_CLA.value)
        if ("m1 intelligence artificielle réseau classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_IA_SICON_CLA.value)
        if ("m1 réseau alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_SICOM_ALT.value)
        if ("m1 intelligence artificielle réseau alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_IA_SICON_ALT.value)
        if ("m2 réseau classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_SICOM_CLA.value)
        if ("m2 intelligence artificielle réseau classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_SICON_CLA.value)
        if ("m2 réseau alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_SICOM_ALT.value)
        if ("m1 intelligence artificielle réseau alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_SICON_ALT.value)
        if ("m1 ingénierie logiciel alternant") in text :
                print("coucou")
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_SICOM_ALT.value)
                print(url)
        if ("m1 ingénierie logiciel classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_ILSEN_CLA.value)
        if ("m2 ingénierie logiciel alt") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_ILSEN_ALT.value)
        if ("m2 intelligence artificielle ingénierie logiciel alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_ILSEN_ALT.value)
        if ("m2 ingénierie logiciel classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_ILSEN_CLA.value)
        if ("m2 intelligence artificielle ingénierie logiciel classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_ILSEN_CLA.value)
        data = requests.get(url).json()
        message = parseRequest(data)
        print(message)
        try :
                data = requests.get(url).json()
                message = parseRequest(data)
                print(message)
                return(message)
        except Exception :
                return("Désolé, une erreur est survenu :'(")
        
        print("Je n'ai pas compris la demande, tu dois me donner ton année ainsi que ton groupe")
