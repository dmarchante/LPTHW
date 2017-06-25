print "I like fruit, so I brought you two boxes of a variety of fruits. Box one has tropical fruits and box two has regular fruits, choose one."

box = raw_input("> ")

if box == "1":
    print "You chose the tropical box. Would you like to eat a mango or an orange?"

    trop_fruit = raw_input("> ")

    if trop_fruit == "mango":
        print "That is my favorite fruit enjoy!"
    elif trop_fruit == "orange" or trop_fruit == "pineapple":
        print "I like that fruit too, enjoy!"
    else:
        print "We dont have that fruit in this box. Sorry."

elif box == "2":
    print "You chose the regular fruit box. Would you like to eat an apple or a peach?"

    reg_fruit = raw_input("> ")

    if reg_fruit == "apple":
        print "I am not a fan of apples, but enjoy!"
    else:
        print "I guess its peach or nothing. Enjoy!"

else:
    print "I guess you dont like fruits."
