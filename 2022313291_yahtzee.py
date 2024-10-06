# Yahtzee game
import random
import os
from time import sleep

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
        self.unrecorded = []
        # by default, all scores are unrecorded
        for key in self.score:
            self.unrecorded.append(key)

        # after player choose the score, it will be recorded
        self.recorded = []

# Handling the roll of the dice include reroll
def roll(player):
    global current_dice
    current_dice = [random.randint(1, 6) for _ in range(5)]
    reroll_count = 0

    clear()
    print(" => ROLL 1")
    # show the current score
    printScoreExpected(player)
    printDice(player)

    is_reroll = input("   Reroll? (y/n) -> ")
    is_reroll.lower().strip()

    # Check if mistyped
    while is_reroll not in ("y", "yes", "n", "no"):
        is_reroll = input("   (You've mistyped) Reroll? (y/n) -> ")
        is_reroll.lower().strip()

    if is_reroll in ("y", "yes"):
        while reroll_count < 2:
            # Show for the reroll
            if reroll_count != 0:
                clear()
                print(" => REROLL 2")
                # show the current score
                printScoreExpected(player)
                printDice(player)

                is_reroll = input("   Reroll? (y/n) default is 'y' -> ")
                is_reroll = is_reroll.lower().strip()

                if is_reroll == "n" or is_reroll == "no":
                    break

            print("\n")
            replace_index = input("   Index of dice to *KEEP* (separated by space) -> ")

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
        printDice(player)

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to check if score is recorded or not
def checkScoreCurrent(player, score_category):
    # check if score is not recorded
    for i in player.unrecorded:
        if i == score_category:
            return "- "

    return fitTable(player.score[score_category])

# Function to fit the table (if 1-9, then add a space)
def fitTable(value):
    if value < 10:
        return str(value) + " "
    else:
        return str(value)

# Function to print the current score (recorded)
def printScoreCurrent(player):
    clear()
    print("   +-------------------------------")
    print("      ", player.name ,"current Score")
    print("   +----+------------------+------+")
    print("   | 1  | Aces             | ", checkScoreCurrent(player, "aces"), " |" )
    print("   | 2  | Twos             | ", checkScoreCurrent(player, "twos"), " |" )
    print("   | 3  | Threes           | ", checkScoreCurrent(player, "threes"),   " |" )
    print("   | 4  | Fours            | ", checkScoreCurrent(player, "fours"),  " |" )
    print("   | 5  | Fives            | ", checkScoreCurrent(player, "fives"),  " |" )
    print("   | 6  | Sixes            | ", checkScoreCurrent(player, "sixes"),  " |" )
    print("   | 7  | Chance           | ", checkScoreCurrent(player, "chance"), " |" )
    print("   | 8  | Three of a Kind  | ", checkScoreCurrent(player, "three_of_a_kind"), " |" )
    print("   | 9  | Four of a Kind   | ", checkScoreCurrent(player, "four_of_a_kind"), " |" )
    print("   | 10 | Full House       | ", checkScoreCurrent(player, "full_house"), " |" )
    print("   | 11 | Small Straight   | ", checkScoreCurrent(player, "small_straight"), " |" )
    print("   | 12 | Large Straight   | ", checkScoreCurrent(player, "large_straight"), " |" )
    print("   | 13 | Yahtzee          | ", checkScoreCurrent(player, "yahtzee"), " |" )
    print("   +----+------------------+------+")

# Function to connect the calculation and print the score (unrecorded)
def checkScoreExpected(player, score_index):
    score_index += 1
    match (score_index):
        case 1:
            return ("   | 1  | Aces             | " + str(calculateScore("aces")) + "   |")
        case 2:
            return ("   | 2  | Twos             | " + str(calculateScore("twos")) + "   |")
        case 3:
            return ("   | 3  | Threes           | " + str(calculateScore("threes")) + "   |")
        case 4:
            return ("   | 4  | Fours            | " + str(calculateScore("fours")) + "   |")
        case 5:
            return ("   | 5  | Fives            | " + str(calculateScore("fives")) + "   |")
        case 6:
            return ("   | 6  | Sixes            | " + str(calculateScore("sixes")) + "   |")
        case 7:
            return ("   | 7  | Chance           | " + str(calculateScore("chance")) + "   |")
        case 8:
            return ("   | 8  | Three of a Kind  | " + str(calculateScore("three_of_a_kind")) + "   |")
        case 9:
            return ("   | 9  | Four of a Kind   | " + str(calculateScore("four_of_a_kind")) + "   |")
        case 10:
            return ("   | 10 | Full House       | " + str(calculateScore("full_house")) + "   |")
        case 11:
            return ("   | 11 | Small Straight   | " + str(calculateScore("small_straight")) + "   |")
        case 12:
            return ("   | 12 | Large Straight   | " + str(calculateScore("large_straight")) + "   |")
        case 13:
            return ("   | 13 | Yahtzee          | " + str(calculateScore("yahtzee")) + "   |")

# Function to print the expected score (recorded)
def printScoreExpected(player):
    clear()
    print("   +-------------------------------")
    print("      ", player.name ,"Expected Score")
    print("   +----+------------------+------+")

    score_keys = list(player.score.keys())
    unrecorded_keys = player.unrecorded

    for score_key in score_keys:
        if score_key in unrecorded_keys:
            print(checkScoreExpected(player, score_keys.index(score_key)))

    print("   +----+------------------+------+")

# Function to print the dice values
def printDice(player):
    print("   +-------+------------------+")
    for i in range(5):
        print("   | Die",i+1, "|        ",current_dice[i], end="        |\n")
    print("   +-------+------------------+")

# Function to chosee score category to record
def chooseScore(player):
    printScoreExpected(player)
    printDice(player)

    while True:
        try:
            choose_score = int(input("   Give the *INDEX* of the score category to record -> "))

            # change the value of the player score based on the choose_score input
            match choose_score:
                case 1:
                    player.score["aces"] = scoreUpper(1)
                    player.unrecorded.remove("aces")
                    player.recorded.append("aces")
                    break
                case 2:
                    player.score["twos"] = scoreUpper(2)
                    player.unrecorded.remove("twos")
                    player.recorded.append("twos")
                    break
                case 3:
                    player.score["threes"] = scoreUpper(3)
                    player.unrecorded.remove("threes")
                    player.recorded.append("three")
                    break
                case 4:
                    player.score["fours"] = scoreUpper(4)
                    player.unrecorded.remove("fours")
                    player.recorded.append("fours")
                    break
                case 5:
                    player.score["fives"] = scoreUpper(5)
                    player.unrecorded.remove("fives")
                    player.recorded.append("fives")
                    break
                case 6:
                    player.score["sixes"] = scoreUpper(6)
                    player.unrecorded.remove("sixes")
                    player.recorded.append("sixes")
                    break
                case 7:
                    player.score["chance"] = sum(current_dice)
                    player.unrecorded.remove("chance")
                    player.recorded.append("chance")
                    break
                case 8:
                    player.score["three_of_a_kind"] = scoreOfAKind(3)
                    player.unrecorded.remove("three_of_a_kind")
                    player.recorded.append("three_of_a_kind")
                    break
                case 9:
                    player.score["four_of_a_kind"] = scoreOfAKind(4)
                    player.unrecorded.remove("four_of_a_kind")
                    player.recorded.append("four_of_a_kind")
                    break
                case 10:
                    player.score["full_house"] = scoreFullHouse()
                    player.unrecorded.remove("full_house")
                    player.recorded.append("full_house")
                    break
                case 11:
                    player.score["small_straight"] = scoreStraight("small")
                    player.unrecorded.remove("small_straight")
                    player.recorded.append("small_straight")
                    break
                case 12:
                    player.score["large_straight"] = scoreStraight("large")
                    player.unrecorded.remove("large_straight")
                    player.recorded.append("large_straight")
                    break
                case 13:
                    player.score["yahtzee"] = scoreOfAKind(5)
                    player.unrecorded.remove("yahtzee")
                    player.recorded.append("yahtzee")
                    break
        except ValueError:
            print("   (Error) Invalid input!")

# Function to manage all the score calculations
def calculateScore(score_category):
    match (score_category):
        case "aces":
            return fitTable(scoreUpper(1))
        case "twos":
            return fitTable(scoreUpper(2))
        case "threes":
            return fitTable(scoreUpper(3))
        case "fours":
            return fitTable(scoreUpper(4))
        case "fives":
            return fitTable(scoreUpper(5))
        case "sixes":
            return fitTable(scoreUpper(6))
        case "chance":
            return fitTable(sum(current_dice))
        case "three_of_a_kind":
            return fitTable(scoreOfAKind(3))
        case "four_of_a_kind":
            return fitTable(scoreOfAKind(4))
        case "full_house":
            return fitTable(scoreFullHouse())
        case "small_straight":
            return fitTable(scoreStraight("small"))
        case "large_straight":
            return fitTable(scoreStraight("large"))
        case "yahtzee":
            return fitTable(scoreOfAKind(5))

# Function for score (UPPER): aces, twos, threes, fours, fives, sixes
def scoreUpper(num):
    count = 0
    for i in range(5):
        if current_dice[i] == num:
            count += 1
    return count * num

# Function to calculate score of full house
def scoreFullHouse():
    for num in current_dice:
        if current_dice.count(num) == 3:
            for num in current_dice:
                if current_dice.count(num) == 2:
                    return 25
    return 0

# Function to calculate score_of_a_kind: three_of_a_kind, four_of_a_kind, yahtzee
def scoreOfAKind(numOfAKind):
    for num in current_dice:
        if current_dice.count(num) == numOfAKind:
            # Yahtzee!
            if numOfAKind == 5:
                return 50
            return num * numOfAKind
    return 0

# Function to calculate straight score: small_straight, large_straight
def scoreStraight(size):
    sorted_dice = list(set(current_dice))
    if size == "large":
        if [1,2,3,4,5] == sorted_dice or [2,3,4,5,6] == sorted_dice:
            return 40
    else: # small
        if all(x in sorted_dice for x in [1,2,3,4]) or all(x in sorted_dice for x in [2,3,4,5]) or all(x in sorted_dice for x in [3,4,5,6]):
            return 30
    return 0

# Function to start the game
def Yahtzee():
    clear()
    yahtzee_logo = '''
 __  __    ______    __  __    ______   ______    ______     ______    
/\ \_\ \  /\  __ \  /\ \_\ \  /\__  _\ /\___  \  /\  ___\  /\  ___\   
\ \____ \ \ \  __ \ \ \  __ \ \/_/\ \/ \/_/  /__ \ \  __\  \ \  __\   
 \/\_____\ \ \_\ \_\ \ \_\ \_\   \ \_\   /\_____\ \ \_____\ \ \_____\ 
  \/_____/  \/_/\/_/  \/_/\/_/    \/_/   \/_____/  \/_____/  \/_____/ 
                      "Project Assignment 2"
        '''

    print(yahtzee_logo)
    players = []

    # Create 2 players
    for i in range(2):
        name = input("\tPlayer " + str(i + 1) + " name -> ")
        players.append(Player(name))

    clear()
    
    # Start
    for turn in range(13):
       for player in players:
           print("( TURN:", str(turn + 1), ")", player.name)

           # to avoid user's turn burn after choose result
           while True:
               print('''
    +-----------------------+
           Options
    +---+-------------------+
    | 1 | Roll              |
    +---+-------------------+
    | 2 | Score             |
    +---+-------------------+
                     ''')
               while True:
                   try:
                       choice = int(input("    Your choice -> "))
                       break
                   except ValueError:
                       print("   (Error) Invalid choice\n")

               # Handling roll, score options
               match(choice):
                   case 1:
                       roll(player)
                       chooseScore(player)
                       clear()
                       break
                   case 2:
                       printScoreCurrent(player)
                   case _:
                       print("Invalid choice\n")
    
    winner_banner = '''
    :::       ::: ::::::::::: ::::    ::: ::::    ::: :::::::::: :::::::::  
    :+:       :+:     :+:     :+:+:   :+: :+:+:   :+: :+:        :+:    :+: 
    +:+       +:+     +:+     :+:+:+  +:+ :+:+:+  +:+ +:+        +:+    +:+ 
    +#+  +:+  +#+     +#+     +#+ +:+ +#+ +#+ +:+ +#+ +#++:++#   +#++:++#:  
    +#+ +#+#+ +#+     +#+     +#+  +#+#+# +#+  +#+#+# +#+        +#+    +#+ 
     #+#+# #+#+#      #+#     #+#   #+#+# #+#   #+#+# #+#        #+#    #+# 
      ###   ###   ########### ###    #### ###    #### ########## ###    ### '''

    draw_banner = '''
                :::::::::  :::::::::      :::     :::       ::: 
                :+:    :+: :+:    :+:   :+: :+:   :+:       :+: 
                +:+    +:+ +:+    +:+  +:+   +:+  +:+       +:+ 
                +#+    +:+ +#++:++#:  +#++:++#++: +#+  +:+  +#+ 
                +#+    +#+ +#+    +#+ +#+     +#+ +#+ +#+#+ +#+ 
                #+#    #+# #+#    #+# #+#     #+#  #+#+# #+#+#  
                #########  ###    ### ###     ###   ###   ###   '''

    player1_final_score = sum(players[0].score.values())
    player2_final_score = sum(players[1].score.values())

    print("   Counting total scores for both of you...")
    # Simple gimmic to make like true counting
    sleep(1)

    print("   --------------RESULT--------------\n")
    print("   Total Score for ", players[0].name ," => ", player1_final_score, "\n")
    print("               (VS)\n ")
    print("   Total Score for ", players[1].name ," => ", player1_final_score, "\n")
    print("   ----------------------------------")
    sleep(1)
    print("   Therefore,")

    # Check player score
    if (player1_final_score > player2_final_score):
        print(winner_banner)
        print("\n                             --- ", players[0].name, "  ---")
    elif (player1_final_score < player2_final_score):
        print(winner_banner)
        print("\n                             --- ", players[1].name, "  ---")
    else:
        print(draw_banner)

    print("\n\n")

if __name__ == "__main__":
    try:
        Yahtzee()
    except KeyboardInterrupt:
        print("\n   Exiting the game...")
