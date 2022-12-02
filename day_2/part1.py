import sys

actions = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scisor',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scisor'
}


def score_round(action_pl, action_opp):
    if action_pl == 'rock':
        score = 1
    elif action_pl == 'paper':
        score = 2
    elif action_pl == 'scisor':
        score = 3

    # draw condition
    if action_pl == action_opp:
        score += 3
        return score

    # win conditions
    if action_pl == 'paper' and action_opp == 'rock':
        score += 6
        return score

    if action_pl == 'rock' and action_opp == 'scisor':
        score += 6
        return score

    if action_pl == 'scisor' and action_opp == 'paper':
        score += 6
        return score

    # if reach here, player lost
    return score


total_score = 0


for line in open(sys.argv[1], 'r').readlines():
    opp, pl = line.split(' ')
    action_opp = actions[opp.strip()]
    action_pl = actions[pl.strip()]
    total_score += score_round(action_pl, action_opp)

print(total_score)
