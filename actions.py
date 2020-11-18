# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

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

