import json
import requests
from Schedule.Student import EnumStudent
import datetime
        
def parseRequest(data):
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

        message = ""
        findCour = False
        for i in data["results"] :
                if(i["start"][:10] == dateToday[:10]) :
                        if((i["start"][11:13] >= time) & (i["start"][11:13] <= timeEnd)) :
                                heureDebut = i["start"][11:16]
                                heureFin = i["end"][11:16]
                                listLigneCour = i["title"].split('\n')
                                ligneCour = listLigneCour[0]
                                salleCour = listLigneCour[3]
                                typeCour = i["type"]
                                message = message + ("Tu as un " + typeCour + " de " + ligneCour + " qui commence à " + 
                                        heureDebut + " et qui se termine à " + heureFin + " dans la (les) " + salleCour)
                                findCour = True
        
        if findCour is False :
                return "Tu n'as pas de cour"
        return(message)

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
        if ("m1 ilsen") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M1_ILSEN.value)
        if ("m2 ilsen") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M2_ILSEN.value)
        if ("m1 sicom") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M1_SICOM.value)
        if ("m2 sicom") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M2_SICON.value)
        if ("m1 ia") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M1_IA.value)
        if ("m2 ia") in text :
                url = urlApiPromotion + str(EnumStudent.Promotion.M2_IA.value)
        if ("m1 sicom classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_SICON_CLA.value)
        if ("m1 ia sicom classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_IA_SICON_CLA.value)
        if ("m1 sicom alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_SICOM_ALT.value)
        if ("m1 ia sicom alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_IA_SICON_ALT.value)
        if ("m2 sicom classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_SICOM_CLA.value)
        if ("m2 ia sicom classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_SICON_CLA.value)
        if ("m2 sicom alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_SICOM_ALT.value)
        if ("m1 ia sicom alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_SICON_ALT.value)
        if ("m1 ilsen alternant") in text :
                print("coucou")
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_SICOM_ALT.value)
                print(url)
        if ("m1 ilsen classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M1_ILSEN_CLA.value)
        if ("m2 ilsen alt") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_ILSEN_ALT.value)
        if ("m2 ia ilsen alternant") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_ILSEN_ALT.value)
        if ("m2 ilsen classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_ILSEN_CLA.value)
        if ("m2 ia ilsen classique") in text :
                url = urlApiGroupe + str(EnumStudent.Groupe.M2_IA_ILSEN_CLA.value)

        try :
                data = requests.get(url).json()
                message = parseRequest(data)
                print(message)
                return(message)
        except Exception :
                return("Désolé, une erreur est survenu :'(")
        
        print("Je n'ai pas compris la demande, tu dois me donner ton année ainsi que ton groupe")
