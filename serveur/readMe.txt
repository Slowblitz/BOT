Penser à bien changer les ip afin qu'ils puissent communiquer entre eux

Rasa :

-> rasa run actions
-> rasa run -m models --enable-api --cors "*" --debug

Python : (le serveur est dans un environent virtuel python penser à l'activer)

-> export FLASK_APP=serveur.py
-> flask run --host="your ip"