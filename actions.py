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
        dispatcher.utter_custom_json(datasTeacher)
        return []

class ActionSchedule(Action):
    def name(self):
        return 'action_schedule'

    def run(self, dispatcher, tracker, domain):
        dataToday = datetime.date.today()
        data = requests.get("https://edt-api.univ-avignon.fr/app.php/api/events_promotion/2-M2EN").json()
        dataToday = datetime.date.today()
        data = requests.get("https://edt-api.univ-avignon.fr/app.php/api/events_promotion/2-M2EN").json()
        for i in data["results"] :
                if(i["start"][:10] == str(dataToday)):
                    dispatcher.utter_custom_json(i)
        return []