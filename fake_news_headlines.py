import random
subjects=[
    "Shahrukh khan",
    "Virat khohli",
    "Nirmila sitharaman",
    "A Mumbai Cat",
    "A Group Of Monyek",
    "Prime Minster Modi Ji",
    "Auto Rickshaw Drived Delhi"
]

actions = [
    "Launches",
    "cancles",
    "dances with",
    "decalres war on",
    "eat",
    "ordered",
    "clerebrates"
]

place_of_things = [
    "at red ford",
    "mumbai local train",
    "plate of samosa",
    "inside praliment",
    "at ganga ghat",
    "during IPL match",
    "india gate"
]

#start the headline genration loop 

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_of_thing = random.choice(place_of_things)

    headline = f'BREAKING NEWs : {subject} {action} {place_of_thing}'
    print('\n' + headline)

    user_input = input("do you want another healding? (YES/NO)").strip().lower()
    if user_input == "no" :
        break

print ("\n THANKS FOR USING THE FAKE NEWS HEADLINE GENRATER HAVE A FUN DAY" )