import json
import requests
import EnumTeacher
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
                                message = message + ("Il a un " + typeCour + " de " + ligneCour[0][10:] + " qui commence à " + 
                                        heureDebut + " et qui se termine à " + heureFin + "\n")
                                findCour = True
        
        if findCour is False :
                return "Le prof n'a pas cour aujourd'hui"
        return(message)

urlApiTeacher = "https://edt-api.univ-avignon.fr/app.php/api/events_enseignant/"




text = "mickael rouvier"
text = text.lower()

if ("jabaian bassam") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_BASSAM.value)
if ("fabrice lefevre") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_LEFEVRE.value)
if ("mickael rouvier") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_BASSAM.value)
if ("phillipe gilles") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_GILLES.value)
if ("sophie nabitz") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_NABITZ.value)
if ("corinne fredouille") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_FREDOUILLE.value)
if ("richard dufour") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_DUFOUR.value)
if ("juan manuel torres moreno") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_TORRES.value)
if ("driss matrouf") in text :
        url = urlApiTeacher + str(EnumTeacher.Teacher.TEACHER_MATROUF.value)
        
try :
        data = requests.get(url).json()
        print(parseRequest(data))
except Exception :
        print("Désolé, une erreur est survenu :'(")
        print("Je n'ai pas compris la demande, tu dois me donner un nom de pofesseur du CERI")