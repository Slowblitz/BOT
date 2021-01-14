
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import json
from datetime import datetime,timedelta
import requests
from typing import Any, Text, Dict, List
from rasa_sdk.interfaces import Action, Tracker
import requests
from Schedule.Student.ScheduleStudent import ask_schedule_student
from ClassRoom.where.whereIsClassRoom import WhereIsClassRoom

urlApiEnseignant = 'https://edt-api.univ-avignon.fr/app.php/api/enseignants'
urlApiEventEnseignant = 'https://edt-api.univ-avignon.fr/app.php/api/events_enseignant/'

class ActionTeacher(Action):
    def name(self):
        return 'action_teacher'

    def run(self, dispatcher, tracker, domain):
        nameTeacher = tracker.latest_message["entities"][0]['value']
        response = requests.get(urlApiEnseignant)
        datasTeacher = response.json()
        dateToday = datetime.today()
        dateToday = dateToday.strftime('%Y-%m-%d')
        dispoMessage = ''
        findIndispo = False
        nbTeacher = 0
        for response in datasTeacher["results"]:
            if response["letter"] == nameTeacher[0]:
                for teacherObject in response["names"]:
                    if nameTeacher in teacherObject["name"]:
                        nbTeacher += 1
                        if(nbTeacher > 1):
                            dispatcher.utter_message(
                                'Plusieurs personnes ont le même nom, redemandez la disponibilité avec le prénom')
                            return []
                        responseDispo = requests.get(urlApiEventEnseignant + teacherObject["uapvHarpege"])
                        dispoTeacher = responseDispo.json()
                        if len(dispoTeacher["results"]) > 0:
                            dispoMessage = 'Monsieur ' + nameTeacher + ' n\'est pas dispo de '
                            for cours in dispoTeacher["results"]:
                                if(cours["start"][:10] == str(dateToday)):
                                    if(cours["type"] != "Annulation"):
                                        findIndispo = True
                                        heureDebut = str(int(cours["start"][11:13]) + 1) + cours["start"][13:16]
                                        heureFin = str(int(cours["end"][11:13]) + 1) + cours["end"][13:16]
                                        dispoMessage += heureDebut + ' à ' + heureFin + ', '
                            dispoMessage += ' aujourd\'hui'
                        if not findIndispo:
                            dispoMessage = nameTeacher + ' est disponible aujourd\'hui'
        dispatcher.utter_message(dispoMessage)
        return []

class ActionSchedule(Action):
    def name(self):
        return 'action_schedule'

    def run(self, dispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if(tracker.get_slot("year") == "L3" or tracker.get_slot("year") == "L2" or tracker.get_slot("year") == "L1"):
            texte = tracker.get_slot("year"),  " ", tracker.get_slot("promotion")
        else :
            texte = tracker.get_slot("year"), " ", tracker.get_slot("promotion"), " ", tracker.get_slot("regime")
        texte = "".join(texte)

        dispatcher.utter_message(ask_schedule_student(texte))
        return []

class ActionScheduleTomorrow(Action):
    def name(self):
        return 'action_schedule_tomorrow'
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message()
        return []
class ActionFreeClassRoom(Action):
    def name(self):
        return 'action_free_class_room'

    def run(self, dispatcher, tracker, domain):
        date = datetime.today().strftime('%Y-%m-%d')
        response = requests.get("https://edt-api.univ-avignon.fr/app.php/api/salles/disponibilite?site=CERI&date=",date)
        data =response.json()# This method is convenient when the API returns JSON
        for response in data["results"][:5] :
            dispatcher.utter_message(response["libelle"].split('=')[0])
        return []

class ActionFreeClassRoomTomorrow(Action):
    def name(self):
        return 'action_free_class_room_tomorrow'

    def run(self, dispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date =datetime.now() + timedelta(days=1)
        tmp = tracker.latest_message.get("jour")
        print(tmp)
        response = requests.get("https://edt-api.univ-avignon.fr/app.php/api/salles/disponibilite?site=CERI&date=",date.strftime('%Y-%m-%d'))
        data =response.json()# This method is convenient when the API returns JSON
        for response in data["results"][:5] :

            dispatcher.utter_message(response["libelle"].split('=')[0])
        return []


class ActionGpsClassRoom(Action):
    def name(self):
        return 'action_GpsClassRoom'

    def run(self, dispatcher, tracker:Tracker, domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        salle = tracker.latest_message["entities"]
        numsalle=(salle[0]['value']).lower()
        dispatcher.utter_message(WhereIsClassRoom(numsalle))
        return []
