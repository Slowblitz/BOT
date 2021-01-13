import json
import requests
from enum import Enum
import datetime

class Salle(Enum) :
        SALLE_ADA = "Direct a gauche deuxieme amphi"
        SALLE_BLAISE = "Direct a gauche premier amphi"
        SALLE_CISCO = "Premier etage au fond a droite"
        SALLE_ELEC = "Premier etage au fond a gauche"
        SALLE_RES = "Premier etage au fond a droite"
        SALLE_ROB = "Premier etage 4 em salle  a droite"
        SALLE_S1 = "Rez de chaussé premiere a droite"
        SALLE_S2 = "Rez de chaussé deuxieme a droite"
        SALLE_S3 = "Rez de chaussé troisieme a droite"
        SALLE_S4 = "Rez de chaussé quatriéme a droite"
        SALLE_S5 = "Rez de chaussé premiere a gauche"
        SALLE_S6 = "Rez de chaussé premiere a gauche"
        SALLE_S7 = "Rez de chaussé premiere a gauche"
        SALLE_S8 = "Rez de chaussé premiere a droite"
        SALLE_STAT1 = "premiere etage premiere a  droite"
        SALLE_STAT2 = "premiere etage deuxieme a  droite"
        SALLE_STAT3 = "premiere etage troiseme a  droite"
        SALLE_STAT4 = "premiere etage premiere a  gauche"
        SALLE_STAT5 = "premiere etage deuxieme a  gauche"
        SALLE_STAT6 = "premiere etage quatrieme a  droite"
        SALLE_STAT7 = "premiere etage cinquieme a  droite"
        SALLE_STAT8 = "premiere etage salle windobe"
        SALLE_STAT9 = "premiere etage salle windobe"
def WhereIsClassRoom(text):

        if("amphi blaise") in text :
                where = str(Salle.SALLE_BLAISE.value)
        if("amphi ada") in text :
                where = str(Salle.SALLE_ADA.value)
        if("amphitheatre blaise") in text :
                where = str(Salle.SALLE_BLAISE.value)
        if("amphitheatre ada") in text :
                where = str(Salle.SALLE_ADA.value)
        if("salle cisco") in text :
                where = str(Salle.SALLE_CISCO.value)
        if("salle elec") in text :
                where = str(Salle.SALLE_ELEC.value)
        if("salle reseau") in text :
                where = str(Salle.SALLE_RES.value)
        if("salle robot") in text :
                where = str(Salle.SALLE_ROB.value)
        if("salle 1") in text :
                where = str(Salle.SALLE_S1.value)
        if("salle 2") in text :
                where = str(Salle.SALLE_S2.value)
        if("salle 3") in text :
                where = str(Salle.SALLE_S3.value)
        if("salle 4") in text :
                where = str(Salle.SALLE_S4.value)
        if("salle 5") in text :
                where = str(Salle.SALLE_S5.value)
        if("salle 6") in text :
                where = str(Salle.SALLE_S6.value)
        if("salle 7") in text :
                where = str(Salle.SALLE_S7.value)
        if("salle 8") in text :
                where = str(Salle.SALLE_S8.value)
        if("stat 1") in text :
                where = str(Salle.SALLE_STAT1.value)
        if("stat 2") in text :
                where = str(Salle.SALLE_STAT2.value)
        if("stat 4") in text :
                where = str(Salle.SALLE_STAT4.value)
        if("stat 5") in text :
                where = str(Salle.SALLE_STAT5.value)
        if("stat 6") in text :
                where = str(Salle.SALLE_STAT6.value)
        if("stat 7") in text :
                where = str(Salle.SALLE_STAT7.value)
        if("stat 8") in text :
                where = str(Salle.SALLE_STAT8.value)
        if("stat 9") in text :
                where = str(Salle.SALLE_STAT9.value)
                
        try :
                return(where)
        except Exception :
                print("Désolé, une erreur est survenu :'(")
                print("Je n'ai pas compris la demande, tu dois me donner ton année ainsi que ton groupe")