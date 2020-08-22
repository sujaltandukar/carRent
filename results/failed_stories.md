## happy path 1
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: affirm: amazing -->
    - utter_happy   <!-- predicted: utter_affirm -->


## happy path 2
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: affirm: amazing -->
    - utter_happy   <!-- predicted: utter_affirm -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: affirm: not good -->
    - utter_cheer_up   <!-- predicted: utter_affirm -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_affirm -->


## sad path 2
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: affirm: not good -->
    - utter_cheer_up   <!-- predicted: utter_affirm -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: affirm: not really -->
    - utter_goodbye   <!-- predicted: utter_affirm -->


## sad path 3
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: affirm: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_affirm -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: price_list_400: no -->
    - utter_goodbye   <!-- predicted: utter_price_list_400 -->


## bot challenge
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: utter_bot_challenge -->


