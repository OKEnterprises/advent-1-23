""" This module contains functions relating to processing calibration values from text data. """

def process_line(curr_line):
    """ This function converts written numbers in the input string into digits.
    It removes all other non-numeric characters.
    EXAMPLE: 2nineopone -> 291
    """

    written_numbers = {
            'one':'1',
            'two':'2',
            'three':'3',
            'four':'4',
            'five':'5',
            'six':'6',
            'seven':'7',
            'eight':'8',
            'nine':'9'
    }

    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    processed = ""

    for i, _ in enumerate(curr_line):
        if curr_line[i:i+5] in written_numbers:
            processed += written_numbers[curr_line[i:i+5]]
        elif curr_line[i:i+4] in written_numbers:
            processed += written_numbers[curr_line[i:i+4]]
        elif curr_line[i:i+3] in written_numbers:
            processed += written_numbers[curr_line[i:i+3]]
        elif curr_line[i] in digits:
            processed += curr_line[i]

    return processed

def get_calibration_value(input_text):
    """ This function retrieves the calibration value from a line of text.
    It takes the first and last character from the input, joins them,
    and outputs the result cast to int. 
    EXAMPLE: 2nineopone -> 21 """
    processed_text = process_line(input_text)
    return int(processed_text[0] + processed_text[-1])

print(get_calibration_value('two1nine')) # 29
print(get_calibration_value('eightwothree')) # 83
print(get_calibration_value('abcone2threexyz')) # 13
print(get_calibration_value('xtwone3four')) # 24
print(get_calibration_value('4nineeightseven2')) # 42
print(get_calibration_value('zoneight234')) # 14
print(get_calibration_value('7pqrstsixteen')) # 76

with open('advent-1-23/input.txt', 'r', encoding='utf-8') as f:
    calibration_values = []

    for line in f:
        calibration_values.append(get_calibration_value(line))

    print(f"The sum of the calibration values is {sum(calibration_values)}")
    