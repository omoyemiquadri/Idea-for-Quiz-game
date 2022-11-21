import pyfiglet as fg

label = fg.figlet_format("QUIZ")
print(f"{label} \n\t\t QUIZ GAME APPLICATION.")


class Quiz:
    def __init__(self):
        playing = input("Do you want to play game? ")

        if playing != "yes".lower():
            quit()
        print("Okay! Let's play game")
    def ans(self):
        score = 0
        answer = input("What do CPU stand for? ")
        if answer.lower() == "central processing units":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        answer_2 = input("What do RAM stand for? ")
        if answer_2.lower() == "random access memory":
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        print("You got " + str(score) + " questions correct!")
        print("You got " + str((score / 4) * 100) +"%.")
        quit()

game = Quiz()
game.ans()