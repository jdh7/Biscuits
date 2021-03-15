import time
from main import Die, Biscuits
from datetime import datetime


def autoplay(episodes):
    start = datetime.now()
    total = 0
    high = 0
    low = 10
    for i in range(0, episodes):
        a = Biscuits()

        while a.game_over == False:
            current_board = a.roll()
            board = []
            for k in current_board:
                if k[2] != "Picked up":
                    # [dice score, dice sides, roll, name]
                    board.append([k[0].sides - k[2], k[0].sides, k[2], k[1]])

            board = sorted(board, key=lambda x: x[0], reverse=False)

            # a.pick_up(greedy(board))
            # a.pick_up(scared_of_d12(board))
            a.pick_up(turn_thresholding(board))
            # print(a.draw_board())
            # time.sleep(1)

        if a.game_over == True and episodes < 30:
            print(f"Episode {i} over, score: {a.score}")
        elif a.game_over == True and i % 50_000 == 0:
            if total != 0:
                print(f"Episode {i} over, average score: {(total)/(i+1)}")

        if a.score > high:
            high = a.score
        if a.score < low:
            low = a.score

        total += a.score

    end = datetime.now()
    runtime = end - start
    print(f"ran {episodes} times in {runtime} seconds, average score: {total/episodes}")
    print(f"the highest score was: {high}, the lowest score was: {low}")


"""
ALGO-RHYTHMS
"""

# expected return from this strategy is 9.667026666666666 (tested over 300k runs)
def greedy(current_rolls):
    pickup = []
    for i in current_rolls:
        if i[0] == 0:
            pickup.append(i[3])
    if len(pickup) == 0:
        pickup.append(current_rolls[0][3])
    return pickup


# Expected score with thresholds: d12: 2; d10: 1 == 8.87
# Expected score with larger or single die thresholds: 9.29 - 10.24
def scared_of_d12(current_rolls):
    D12THRESHOLD = 2
    D10THRESHOLD = 1
    pickup = []
    for i in current_rolls:
        if i[0] == 0:
            pickup.append(i[3])
        if "d12" not in pickup and i[3] == "d12" and i[0] <= D12THRESHOLD:
            pickup.append(i[3])
        if "d10" not in pickup and i[3] == "d10" and i[0] <= D10THRESHOLD:
            pickup.append(i[3])
    if len(pickup) == 0 and ("d12" or "d10") not in pickup:
        pickup.append(current_rolls[0][3])

    return pickup


# Expected score with 10 remaining dice thresholding: 8.72
# Expected score with 6  remaining dice thresholding: 8.72
# ES with 7 remaining dice == 8.6997
# ES with 8 remaining dice == 8.6912
def turn_thresholding(current_rolls):
    D12THRESHOLD = 2
    D10THRESHOLD = 1
    # 15 dice in the game
    REMAININGDICE = 8
    pickup = []
    for i in current_rolls:
        if i[0] == 0:
            pickup.append(i[3])
        if "d12" not in pickup and i[3] == "d12" and i[0] <= D12THRESHOLD:
            if len(current_rolls) - len(pickup) < REMAININGDICE:
                pickup.append(i[3])
        if "d10" not in pickup and i[3] == "d10" and i[0] <= D10THRESHOLD:
            if len(current_rolls) - len(pickup) < REMAININGDICE:
                pickup.append(i[3])
    if len(pickup) == 0 and ("d12" or "d10") not in pickup:
        pickup.append(current_rolls[0][3])

    return pickup
