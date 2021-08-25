import random
from statistics import mean


def just_round_wins(speed: int, n_combats: int = 100, combat_rounds: int = 3):
    '''number of rounds you win if you roll for each round
    :returns int: number of winning rounds'''

    # changing to two  for proper range further
    if combat_rounds == 1:
        combat_rounds = 2
    round_wins = 0
    for combat in range(n_combats - 1):
        for _ in range(combat_rounds - 1):
            if speed >= random.randint(0, 99):
                round_wins += 1

    return round_wins


def full_combat_wins(speed: int, n_combats: int = 100,
                     combat_rounds: int = 3):
    '''number of rounds you win if you roll once per combat
    :returns int: number of winning rounds'''
    full_combat_wins = 0
    for combat in range(n_combats - 1):
        if speed >= random.randint(0, 99):
            full_combat_wins += 1

    return full_combat_wins * combat_rounds


speed = 36
combat_rounds = 3
just_rounds = []
full_combats = []
number_of_combats = 100

# creating lists with data.
for _ in range(number_of_combats - 1):
    just_rounds.append(just_round_wins(speed, combat_rounds=combat_rounds,
                                       n_combats=number_of_combats))
    full_combats.append(full_combat_wins(speed, combat_rounds=
    combat_rounds, n_combats=number_of_combats))

print(f'Combats:    {number_of_combats}')
print(f'Rounds:     {combat_rounds}')
print(f'PC'f' speed:   {speed}')
print(f'Each round: {mean(just_rounds)}')
print(f'Just once:  {mean(full_combats)}')

