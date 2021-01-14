## sad path 1
* greet
  - utter_yo

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## schedule
* ask_schedule
  - action_schedule

* ask_schedule_tomorow
  - action_schedule_tomorrow

## teacher
* greet
  - utter_greet
* ask_teacher
  - utter_name_teacher
* give_name
  - action_teacher
  - utter_goodbye

## free_class_room

* greet
    - utter_greet
* salle_libre
    - action_free_class_room
    - utter_did_that_help
* deny
  - utter_goodbye

## free_class_room_tomorrow

* salle_libre_demain{"jour":"demain"}
    -  action_free_class_room_tomorrow
    - utter_did_that_help

## New Story

* WhereIs{"salle":"salle 2"}
    - action_GpsClassRoom
* WhereIs{"salle":"salle 3"}
    - action_GpsClassRoom
* WhereIs{"salle":"salle 1"}
    - action_GpsClassRoom
* WhereIs
    - utter_goodbye
* WhereIs
    - utter_goodbye

## New Story

* WhereIs{"salle":"salle 3"}
    - action_GpsClassRoom
    - utter_goodbye

## New Story

* ask_salle_schedule{"salle":"s1"}
    - slot{"salle":"s1"}
    - slot{"salle":"s1"}
    - action_GpsClassRoom
* ask_schedule{"year":"L3","promotion":"G2"}
    - slot{"promotion":"G2"}
    - slot{"year":"L3"}
    - action_schedule

## New Story

* ask_formation_schedule
    - utter_ask_formation_schedule
* ask_schedule{"year":"M2","promotion":"ingénierie logiciel"}
    - slot{"promotion":"ingénierie logiciel"}
    - slot{"year":"M2"}
    - action_schedule

## New Story

* ask_formation_schedule
    - utter_ask_formation_schedule
* ask_schedule{"year":"M2","promotion":"ingénierie logiciel","regime":"alternant"}
    - slot{"promotion":"ingénierie logiciel"}
    - slot{"regime":"alternant"}
    - slot{"year":"M2"}
    - action_schedule

## New Story

* salle_libre_demain
    - action_free_class_room_tomorrow

## New Story

* salle_libre_demain
    - action_free_class_room_tomorrow
