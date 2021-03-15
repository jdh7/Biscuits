from main import Die, Biscuits
import time


def welcome():
    print("\n")
    print("###########################")
    print("Biscuits, the dice game!  #")
    print("###########################")
    print("\n")


def play_game():
    a = Biscuits()
    while a.game_over == False:
        time.sleep(1)
        x = str(input("Begin by typing roll! "))
        if x == "roll" or "Roll" or "ROLL":
            a.roll()
            a.draw_board()
            a.pick_up(
                list(
                    map(
                        str,
                        input("Which dice would you like to pick up? e.g: 1d6, 4d6:  ")
                        .strip()
                        .split(", "),
                    )
                )
            )
            print(f"current score is {a.score}")
        else:
            if x == "q" or "quit":
                exit(0)

    if a.game_over == True:
        print(f"Turn over! You scored {a.score} points!")
        exit(0)


if __name__ == "__main__":
    welcome()
    if str(input("Start new game? yes/no: ")) == "no":
        exit(0)
    else:
        players = int(input("How many players? "))

    for i in range(0, players):
        play_game()

    if str(input("Play again?")) == "yes":
        play_game()
