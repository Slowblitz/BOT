Penser à bien changer les ip afin qu'ils puissent communiquer entre eux

Rasa :

-> rasa run actions
-> rasa run -m models --enable-api --cors "*" --debug

Python : (le serveur est dans un environent virtuel python penser à l'activer)

-> export FLASK_APP=serveur.py
-> flask run --host="your ip"


EXPORT KEY API
export GOOGLE_APPLICATION_CREDENTIALS="/home/vallotjpro/dev/master_ilsen/m2/application_innovation/BOT/google_key_speech.json"