import random
while True:
    name = input("Please enter your name: ")
    question = input("What is your question: ")
    answer = ()
    random_number = random.randint(1, 12)

    if name == "" and not question == "":
        print("Question:", question)
    if question == "":
        print("Ya gotta ask a damn question dude.")
    if not name == "" and not question == "":
        print(name, "asks:", question) 

    if random_number == 1:
        answer = ("Yes Definitely.")
    elif random_number == 2:
        answer = ("it is decidedly so.")
    elif random_number == 3:
        answer = ("Without a doubt.")
    elif random_number == 4:
        answer = ("Reply hazy, try again.")
    elif random_number == 5:
        answer = ("Ask again later.")
    elif random_number == 6:
        answer = ("Better not tell you now.")
    elif random_number == 7:
        answer = ("My sources say no.")
    elif random_number == 8:
        answer = ("Outlook not so good.")
    elif random_number == 9:
        answer = ("Very doubtful.")
    elif random_number == 10:
        answer = ("Not a chance.")
    elif random_number == 11:
        answer = ("For sure.")
    elif random_number == 12:
        answer = ("You already know the answer bud.")
    else:
        answer = ("Error")


    if question == "":
        print("Try again. This time ask me something.")
    else:
        print("Magic 8-ball's answer:", answer)

    new_question = input("Would you like to ask another question?(y/n)")
    if new_question == "n":
        break