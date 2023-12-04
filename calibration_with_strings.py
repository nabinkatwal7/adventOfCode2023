import re

def calculate_calibration_value(line):
    digits = re.findall(r'\d+|[a-zA-Z]+', line)
    
    digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    digits = [digit_mapping.get(d, d) for d in digits]
    
    first_digit = int(digits[0])
    last_digit = int(digits[-1])
    
    return int(f"{first_digit}{last_digit}")


lines = ["two1nine", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

calibration_values = [calculate_calibration_value(line) for line in lines]

total_calibration_value = sum(calibration_values)

print("Calibration values:", calibration_values)
print("Sum of calibration values:", total_calibration_value)
