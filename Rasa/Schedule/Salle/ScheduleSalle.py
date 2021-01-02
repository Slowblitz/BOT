import json
import requests
import EnumSalle
import datetime

if __name__ == "__main__" :
        #dateToday = datetime.date.today()
        dateToday = "2020-12-16T13:00:23.111111"
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
                                        message = message + ("La salle à un  " + typeCour + " de " + ligneCour[0][10:] + " qui commence à " + 
                                                heureDebut + " et qui se termine à " + heureFin + "\n")
                                        findCour = True
                
                if findCour is False :
                        return "Tu n'as pas de cour"
                return(message)

        urlApiSalle = "https://edt-api.univ-avignon.fr/app.php/api/events_salle/"

        text = "salle 1"
        text = text.lower()

        if("ampi blaise") in text :
                url = urlApiSalle + str(EnumSalle.Salle.CERI_BLAISE.value)
        if("ampi ada") in text :
                url = urlApiSalle + str(EnumSalle.Salle.CERI_ADA.value)
        if("salle cisco") in text :
                url = urlApiSalle + str(EnumSalle.Salle.CERI_CISCO.value)
        if("salle elec") in text :
                url = urlApiSalle + str(EnumSalle.Salle.CERI_ELEC.value)
        if("salle res") in text :
                url = urlApiSalle + str(EnumSalle.Salle.CERI_RES.value)
        if("salle rob") in text :
                url = urlApiSalle + str(EnumSalle.Salle.CERI_ROB.value)
        if("salle 1") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S1.value)
        if("salle 2") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S2.value)
        if("salle 3") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S3.value)
        if("salle 4") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S4.value)
        if("salle 5") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S5.value)
        if("salle 6") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S6.value)
        if("salle 7") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S7.value)
        if("salle 8") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_S8.value)
        if("stat 1") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT1.value)
        if("stat 2") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT2.value)
        if("stat 4") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT4.value)
        if("stat 5") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT5.value)
        if("stat 6") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT6.value)
        if("stat 7") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT7.value)
        if("stat 8") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT8.value)
        if("stat 9") in text :
                url = urlApiSalle + str(EnumSalle.Salle.SALLE_STAT9.value)
                
        try :
                data = requests.get(url).json()
                print(parseRequest(data))
        except Exception :
                print("Désolé, une erreur est survenu :'(")
                print("Je n'ai pas compris la demande, tu dois me donner ton année ainsi que ton groupe")