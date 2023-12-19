# Read input data
inputs = {}

with open("day2_input.txt", "r") as inputf:
    for row in inputf:
        gameno = int(row.split(":")[0].split()[-1])
        samples = row.split(":")[-1].split(";")
        samples_output = []
        for sample in samples:
            sample_items_output = []
            sample_items = sample.split(",")
            for sample_item in sample_items:
                number = sample_item.strip().split()[0]
                colour = sample_item.strip().split()[1]
                sample_dict = {colour : int(number)}
                sample_items_output.append(sample_dict)
            samples_output.append(sample_items_output)
        inputs[gameno] = samples_output

## Part 1

game_rules = {
    "red" : 12,
    "green": 13,
    "blue": 14
}

possible_game_ids = []
        
for game in inputs:
    possible = True
    for sample in inputs[game]:
        for sample_item in sample:
            for key in sample_item:
                if game_rules[key] < sample_item[key]:
                    possible = False
    if possible == True:
        possible_game_ids.append(game)

print(f"The Part 1 answer is: {sum(possible_game_ids)}")

## Part 2

import math

game_min_sets = {}

for game in inputs:
    min_sample = {"red" : 0, "green" : 0, "blue" : 0}
    for sample in inputs[game]:
        for sample_item in sample:
            for key in sample_item:
                if sample_item[key] > min_sample[key]:
                    min_sample[key] = sample_item[key]
    game_min_sets[game] = min_sample

power_values = []

for game in game_min_sets:
    power_val = []
    for min_sample in game_min_sets[game]:
        power_val.append(game_min_sets[game][min_sample])
    power_value = math.prod(power_val)
    power_values.append(power_value)

print(f"The Part 2 answer is: {sum(power_values)}")

                    