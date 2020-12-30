import json
import requests
import EnumPromotion
import datetime

#dateToday = datetime.date.today()
dateToday = "2020-12-16T10:00:23.111111"
time = dateToday[11:13]
timeEnd = ""
if(time >= "12") :
        time = "12"
        timeEnd = "19"
else:
        time = "07"
        timeEnd = "12"
        
def parseRequest(data):
        message = ""
        findCour = False
        for i in data["results"] :
                if(i["start"][:10] == dateToday[:10]) :
                        if((i["start"][11:13] >= time) & (i["start"][11:13] <= timeEnd)) :
                                heureDebut = i["start"][11:16]
                                heureFin = i["end"][11:16]
                                ligneCour = i["title"].split('\n')
                                typeCour = i["type"]
                                message = message + ("Tu as un " + typeCour + " de " + ligneCour[0][10:] + " qui commence à " + 
                                        heureDebut + " et qui se termine à " + heureFin + "\n")
                                findCour = True
        
        if findCour is False :
                return "Tu n'as pas de cour"
        return(message)

urlApiPromotion = "https://edt-api.univ-avignon.fr/app.php/api/events_promotion/"
urlApiGroupe = "https://edt-api.univ-avignon.fr/app.php/api/events_tdoption/"

text = "l2 g1"
text = text.lower()

if ("l1") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.L1.value)
if( "l1 g1" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L1G1.value)
if( "l1 g2" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L1G2.value)
if( "l1 g3" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L1G3.value)
if( "l1 g4" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L1G4.value)
if( "l1 g5" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L1G5.value)
if( "l1 g6" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L1G6.value)
if ("l2") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.L2.value)
if( "l2 g1" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L2G1.value)
if( "l2 g2" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L2G2.value)
if( "l2 g3" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L2G3.value)
if( "l2 g3" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L2G4.value)
if ("l3") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.L3.value)
if( "l3 g1" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3G1.value)
if( "l3 g2" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3G2.value)
if( "l3 g3" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3G3.value)
if( "l3 g4" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3G4.value)
if( "l3 g5" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3G5.value)
if( "l3 e1" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3E1.value)
if( "l3 e2" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3E2.value)
if( "l3 e3" in text ) :
        url = urlApiGroupe + str(EnumPromotion.Groupe.L3E3.value)
if ("m1 ilsen") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.M1_ILSEN.value)
if ("m2 ilsen") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.M2_ILSEN.value)
if ("m1 sicom") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.M1_SICOM.value)
if ("m2 sicom") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.M2_SICON.value)
if ("m1 ia") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.M1_IA.value)
if ("m2 ia") in text :
        url = urlApiPromotion + str(EnumPromotion.Promotion.M2_IA.value)
if ("m1 sicom classique") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M1_SICON_CLA.value)
if ("m1 ia sicom classique") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M1_IA_SICON_CLA.value)
if ("m1 sicom alternant") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M1_SICOM_ALT.value)
if ("m1 ia sicom alternant") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M1_IA_SICON_ALT.value)
if ("m2 sicom classique") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_SICOM_CLA.value)
if ("m2 ia sicom classique") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_IA_SICON_CLA.value)
if ("m2 sicom alternant") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_SICOM_ALT.value)
if ("m1 ia sicom alternant") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_IA_SICON_ALT.value)
if ("m1 ilsen alternant") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_SICOM_ALT.value)
if ("m1 ilsen classique") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M1_ILSEN_CLA.value)
if ("m2 ilsen alternant") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_ILSEN_ALT.value)
if ("m2 ia ilsen alternant") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_IA_ILSEN_ALT.value)
if ("m2 ilsen classique") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_ILSEN_CLA.value)
if ("m2 ia ilsen classique") in text :
        url = urlApiGroupe + str(EnumPromotion.Groupe.M2_IA_ILSEN_CLA.value)

try :
        data = requests.get(url).json()
        print(parseRequest(data))
except Exception :
        print("Désolé, une erreur est survenu :'(")
        print("Je n'ai pas compris la demande, tu dois me donner ton année ainsi que ton groupe")