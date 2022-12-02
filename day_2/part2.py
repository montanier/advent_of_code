import sys

actions = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scisor'
}

result = {
    'X': 'loose',
    'Y': 'draw',
    'Z': 'win'
}


def score_round(action_opp, result):

    # win conditions
    if action_opp == 'rock':
        if result == 'win':
            action_pl = "paper"
            score = 6
        elif result == 'loose':
            action_pl = "scisor"
            score = 0
        else:
            action_pl = "rock"
            score = 3

    if action_opp == 'scisor':
        if result == 'win':
            action_pl = "rock"
            score = 6
        elif result == 'loose':
            action_pl = "paper"
            score = 0
        else:
            action_pl = "scisor"
            score = 3

    if action_opp == 'paper':
        if result == 'win':
            action_pl = "scisor"
            score = 6
        elif result == 'loose':
            action_pl = "rock"
            score = 0
        else:
            action_pl = "paper"
            score = 3

    if action_pl == 'rock':
        score += 1
    elif action_pl == 'paper':
        score += 2
    elif action_pl == 'scisor':
        score += 3

    return score


total_score = 0


for line in open(sys.argv[1], 'r').readlines():
    opp, res = line.split(' ')
    action_opp = actions[opp.strip()]
    res = result[res.strip()]
    total_score += score_round(action_opp, res)

print(total_score)
