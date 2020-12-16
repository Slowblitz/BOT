
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import json
import datetime
import requests
from rasa_sdk.interfaces import Action
import requests

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

    def run(self, dispatcher, tracker, domain):
        findCour = False
        dateToday = datetime.date.today()
        data = requests.get("https://edt-api.univ-avignon.fr/app.php/api/events_promotion/2-M2EN").json()
        for i in data["results"] :
            if(i["start"][:10] == str(dateToday)):
                heureDebut = i["start"][12:16]
                heureFin = i["end"][12:16]
                ligneCour = i["title"].split('\n')
                typeCour = i["type"]
                message = "Tu as un " + typeCour + " de " + ligneCour[0] + " qui commence à " + \
                          heureDebut + " et qui se termine à " + heureFin
                dispatcher.utter_message(message)
                findCour = True

        if not findCour:
            dispatcher.utter_message(text="Vous n'avez pas de cour")
        return []

class ActionScheduleTomorrow(Action):
    def name(self):
        return 'action_schedule_tomorrow'
    
    def run(self, dispatcher, tracker, domain):
        findCour = False
        dateTomorow = datetime.date.today() + datetime.timedelta(days=1)
        data = requests.get("https://edt-api.univ-avignon.fr/app.php/api/events_promotion/2-M2EN").json()
        if data is not None :
            for i in data["results"] :
                if(i["start"][:10] == str(dateTomorow)):
                        dispatcher.utter_custom_json(i)
                        findCour = True
        
        if not findCour:
            dispatcher.utter_message(text="Vous n'avez pas de cour")
        
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
        print(next(tracker.get_latest_entity_values("jour"),None))
        response = requests.get("https://edt-api.univ-avignon.fr/app.php/api/salles/disponibilite?site=CERI&date=",date.strftime('%Y-%m-%d'))
        data =response.json()# This method is convenient when the API returns JSON
        for response in data["results"] :

            dispatcher.utter_message(response["libelle"].split('=')[0])
        return []
