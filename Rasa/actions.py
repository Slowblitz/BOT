
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

urlApi = 'https://edt-api.univ-avignon.fr/app.php/api/enseignants'

class ActionTeacher(Action):
    def name(self):
        return 'action_teacher'

    def run(self, dispatcher, tracker, domain):
        response = requests.get(urlApi)
        datasTeacher = response.json()
        print(datasTeacher)
        dispatcher.utter_custom_json(datasTeacher)
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
        for response in data["results"] :
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
        for response in data["results"] :

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
