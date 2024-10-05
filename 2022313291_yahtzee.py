# Yahtzee game
import random
import os

# information about player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = {
            "aces": 0,
            "twos": 0,
            "threes": 0,
            "fours": 0,
            "fives": 0,
            "sixes": 0,
            "chance": 0,
            "three_of_a_kind": 0,
            "four_of_a_kind": 0,
            "full_house": 0,
            "small_straight": 0,
            "large_straight": 0,
            "yahtzee": 0
        }

# Handling the roll of the dice include reroll
def roll(player):
    # NOTE: add the changes that happen when rerolling
    global current_dice
    current_dice = [random.randint(1, 6) for _ in range(5)]
    reroll_count = 0

    clear()
    # show the current score
    printScoreExpected(player)

    # Showing the dice
    print("----Your roll: ")
    for i in range(5):
        print("Die",i+1, ": ",current_dice[i], end="\n")
    print("----")

    is_reroll = input("Do you want to reroll? (y/n): ")
    is_reroll.lower().strip()

    while is_reroll not in ("y", "yes", "n", "no"):
        is_reroll = input("(You've mistyped) Do you want to reroll? (y/n): ")
        is_reroll.lower().strip()

    if is_reroll in ("y", "yes"):
        # TODO: check everything
        while reroll_count < 2:
            # Show for the reroll
            if reroll_count != 0:
                clear()
                # show the current score
                printScoreExpected(player)
                print(replace_index)

                print("----Your second roll: ")
                for i in range(5):
                    print("Die",i+1, ": ",current_dice[i], end="\n")
                print("----")
                is_reroll = input("Do you want to reroll? (y/n) default is 'y': ")
                is_reroll = is_reroll.lower().strip()

                if is_reroll == "n" or is_reroll == "no":
                    break

            replace_index = input("Enter the index of the dice you want to keep: (separated by space) :")

            # turn the index into a list
            replace_index = replace_index.split(" ")
            replace_index = [int(i) for i in replace_index]

            # Check if the values are valid (in range)
            for i in replace_index:
                if i < 1 or i > 5:
                    print("Invalid index")

            # Choose the inverse of the replace_index
            replace_index = [i for i in range(1, 6) if i not in replace_index]

            # Replace the die that user wants
            for i in replace_index:
                current_dice[i - 1] = random.randint(1, 6)

            reroll_count += 1

        clear()
        # show the current score
        printScoreExpected(player)
        print(replace_index)

        print(player.name + "---- latest roll: ")
        for i in range(5):
            print("Die",i+1, ": ",current_dice[i], end="\n")
        print("----")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printScoreCurrent(player):
    # NOTE: if score that are not recorded, - shown
    print("\n")
    print("------Current Score: ")
    print("Player: " + player.name)
    print("1. Aces: ", player.score["aces"])
    print("2. Twos: ", player.score["twos"])
    print("3. Threes: ", player.score["threes"])
    print("4. Fours: ", player.score["fours"])
    print("5. Fives: ", player.score["fives"])
    print("6. Sixes: ", player.score["sixes"])
    print("7. Chance: ", player.score["chance"])
    print("8. Three of a Kind: ", player.score["three_of_a_kind"])
    print("9. Four of a Kind: ", player.score["four_of_a_kind"])
    print("10. Full House: ", player.score["full_house"])
    print("11. Small Straight: ", player.score["small_straight"])
    print("12. Large Straight: ", player.score["large_straight"])
    print("13. Yahtzee: ", player.score["yahtzee"])
    print("\n")

def chooseScore(player):
    #NOTE: only choose one, can only choose the unrecorded yet
    clear()
    printScoreExpected(player)
    print(player.name + "---- latest roll: ")
    for i in range(5):
        print("Die",i+1, ": ",current_dice[i], end="\n")
    print("----")

    choose_score = int(input("Based on the score above, give number of the score you want to record: "))

    # change the value of the player score based on the choose_score input
    match choose_score:
        case 1:
            player.score["aces"] = scoreUpper(1)
        case 2:
            player.score["twos"] = scoreUpper(2)
        case 3:
            player.score["threes"] = scoreUpper(3)
        case 4:
            player.score["fours"] = scoreUpper(4)
        case 5:
            player.score["fives"] = scoreUpper(5)
        case 6:
            player.score["sixes"] = scoreUpper(6)
        case 7:
            player.score["chance"] = sum(current_dice)
        case 8:
            player.score["three_of_a_kind"] = scoreOfAKind(3)
        case 9:
            player.score["four_of_a_kind"] = scoreOfAKind(4)
        case 10:
            player.score["full_house"] = scoreFullHouse()
        case 11:
            player.score["small_straight"] = scoreStraight("small")
        case 12:
            player.score["large_straight"] = scoreStraight("large")


# score (UPPER)
def scoreUpper(num):
    count = 0
    for i in range(5):
        if current_dice[i] == num:
            count += 1
    return count * num

# score (LOWER)
def scoreFullHouse():
    # TODO: make a constant marks
    for num in current_dice:
        if current_dice.count(num) == 3:
            for num in current_dice:
                if current_dice.count(num) == 2:
                    return 25
    return 0

def scoreOfAKind(numOfAKind):
    for num in current_dice:
        if current_dice.count(num) == numOfAKind:
            # Yahtzee!
            if numOfAKind == 5:
                return 50
            return num * numOfAKind
    return 0

def scoreStraight(size):
    sorted_dice = list(set(current_dice))
    # NOTE: ada problem dekat large, kene settlekan
    if size == "large":
        if [1,2,3,4,5] == sorted_dice or [2,3,4,5,6] == sorted_dice:
            return 40
    else: # small
        if all(x in sorted_dice for x in [1,2,3,4]) or all(x in sorted_dice for x in [2,3,4,5]) or all(x in sorted_dice for x in [3,4,5,6]):
            return 30
    return 0

def printScoreExpected(player):
    # NOTE: add, like 2 columns (up: can choose, down: already choose) - But need to settle first - problem
    print(" Yahtzee Expected score: \n")
    if (player.score["aces"] == 0):
        print("1. Aces: ", scoreUpper(1))

    if (player.score["twos"] == 0):
        print("2. Twos: ", scoreUpper(2))

    if (player.score["threes"] == 0):
        print("3. Threes: ", scoreUpper(3))

    if (player.score["fours"] == 0):
        print("4. Fours: ", scoreUpper(4))

    if (player.score["fives"] == 0):
        print("5. Fives: ", scoreUpper(5))

    if (player.score["sixes"] == 0):
        print("6. Sixes: ", scoreUpper(6))

    if (player.score["chance"] == 0):
        print("7. Chance: ", sum(current_dice))

    if (player.score["three_of_a_kind"] == 0):
        print("8. Three of a Kind: ", scoreOfAKind(3))

    if (player.score["four_of_a_kind"] == 0):
        print("9. Four of a Kind: ", scoreOfAKind(4))

    if (player.score["full_house"] == 0):
        print("10. Full House: ", scoreFullHouse())

    if (player.score["small_straight"] == 0):
        print("11. Small Straight: ", scoreStraight("small"))

    if (player.score["large_straight"] == 0):
        print("12. Large Straight: ", scoreStraight("large"))

    if (player.score["yahtzee"] == 0):
        print("13. Yahtzee: ", scoreOfAKind(5))

def Yahtzee():
    clear()
    print("Let's play Yahtzee!\n")

    players = []

    # Create 2 players
    for i in range(2):
        name = input("Enter player " + str(i + 1) + " name: ")
        players.append(Player(name))

    clear()
    for turn in range(13):
        for player in players:
            print("Player " + player.name + "'s turn " + str(turn + 1) + " started\n")
            # to avoid user's turn burn
            while True:
                print("Options:\n 1. Roll\n 2. Score")
                choice = int(input("Enter your choice:"))

                match(choice):
                    case 1:
                        roll(player)
                        chooseScore(player)
                        clear()
                        break
                    case 2:
                        #TODO: but score "-", maybe make 2 group something like that
                        printScoreCurrent(player)
                    case _:
                        print("Invalid choice\n")

    print("WINNER!!!")
    player1_final_score = sum(players[0].score.values())
    player2_final_score = sum(players[1].score.values())

    print("Total Score of ", players[0].name ,": ", player1_final_score)
    print("Total Score of ", players[1].name ,": ", player2_final_score)

    if (player1_final_score > player2_final_score):
        print(players[0].name, " wins!")
    else:
        print(players[1].name, " wins!")

    
if __name__ == "__main__":
    try:
        Yahtzee()
    except KeyboardInterrupt:
        print("\nExiting the game!")
