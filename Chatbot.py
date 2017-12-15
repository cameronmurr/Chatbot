#Chatbot

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup", "yee", "uh huh"]:
            return True
        elif answer in ["n", "no", "nope", "nah", "nuh uh"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Major key",
                 "Yuhhhhhhh",
                 "Das swag",
                 "Gucci",
                 "Fo shizzle"
                 "Preach"]

    return random.choice(responses)


def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister"]
    teacher_words = ["cooper", "school", "subject"]
    math_words = ["number", "math"]
    teacher_responses = ["I hear Mr. Cooper's class is litty.", "School is dank"]


    
    if has_keyword(statement, family_words):
        response = "Fam is the most important."
    elif has_keyword(statement, teacher_words):
        response = random.choice(teacher_responses)
    elif has_keyword (statement, math_words):
        response = "2 plus 2 is 4 minus 1 is three; Quick Maths."
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("██████╗  █████╗  ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗██████╗  ██████╗ ████████╗")
    print("██╔══██╗██╔══██╗██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔═══██╗╚══██╔══╝")
    print("██║  ██║███████║██║   ██║██║   ██║███████║██╔██╗ ██║██████╔╝██║   ██║   ██║   ")
    print("██║  ██║██╔══██║██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║██╔══██╗██║   ██║   ██║   ")
    print("██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║██████╔╝╚██████╔╝   ██║   ")
    print(" ═════╝ ╚═╝  ╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝    ╚═╝  ")
    print("Yo what's the word. I'm Daquanbot.")
    print("What's ya name homie?")
    name=input()
    print("Wassup " + name)

    while talking:
        statement = input(name + ": ")
        statement = statement.lower()

        if (statement == "goodbye" or
           statement == "bye" or
           statement == "deuces" or
           statement == "adios"):
            talking = False
        else:
            response = get_response(statement)
            print("Daquanbot: " + response)

    print("Dueces big dawg")

start()

playing = True

while playing:
    play()
    playing = confirm("Wanna chat again?")

end()
