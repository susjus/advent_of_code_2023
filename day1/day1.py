# Read input data into a list
inputs = []

with open("day1_input.txt", "r") as inputf:
    for row in inputf:
        inputs.append(row)

# Keep only the digits
inputs_digits = []

for item in inputs:
    ordered_digits = [int(s) for s in item if s.isdigit()]
    inputs_digits.append(ordered_digits)

# Now we combine the first a last digit in each item

inputs_digits_combined = [int(str(i[0]) + str(i[-1])) for i in inputs_digits]

# Add sum them to get the Part 1 answer

print(f"The first answer is: {sum(inputs_digits_combined)}")

## Part 2 - Convert spelled out digits to digits
# Gotcha: some digit spellings can have a common first and last letter (e.g. eightwo or oneight).
# Replace approach didn't work needed to switch to re findall (I did google it on first question ! :())

import re

inputs_digits_spelled_combined = []

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

for item in inputs:
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', item)
    value = int(''.join([numbers[d] if d.isalpha() else d for d in [digits[0], digits[-1]]]))
    inputs_digits_spelled_combined.append(value)

# Add sum to get the Part 2 answer

print(f"The second answer is: {sum(inputs_digits_spelled_combined)}")