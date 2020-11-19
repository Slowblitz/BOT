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

class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return ['hello world']
class ActionYo(Action):
    def name(self):
        return 'action_yo'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Example yo")
        return []


class ActionCiao(Action):
    def name(self):
        return 'action_ciao'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("ciao")
        return []

class EmploiDuTemp(Action):
    def name(self):
        return 'action_emploi_du_temps'

    def run(self, dispatcher, tracker, domain):
        dataToday = datetime.date.today()
        data = requests.get("https://edt-api.univ-avignon.fr/app.php/api/events_promotion/2-M2EN").json()
        dataToday = datetime.date.today()
        data = requests.get("https://edt-api.univ-avignon.fr/app.php/api/events_promotion/2-M2EN").json()
        for i in data["results"] :
                if(i["start"][:10] == str(dataToday)):
                    dispatcher.utter_custom_json(i)
        return []