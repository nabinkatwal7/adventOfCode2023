def extract_calibration_value(line):
    first_digit = next(char for char in line if char.isdigit())
    last_digit = next(char for char in reversed(line) if char.isdigit())
    return int(first_digit + last_digit)

def sum_calibration_values(calibration_document):
    total_sum = sum(extract_calibration_value(line) for line in calibration_document)
    return total_sum

calibration_document = []

f = open("calibration.txt", "r")

for line in f:
    calibration_document.append(line.replace("\n", ""))

result = sum_calibration_values(calibration_document)
print("Sum of calibration values:", result)
