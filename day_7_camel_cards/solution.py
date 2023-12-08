from collections import Counter
from functools import cmp_to_key


def main():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        part_1(lines)
        part_2(lines)


def part_1(lines):
    hands_and_bids = parse_input(lines, 1)
    hab_by_rank = rank_hands_and_bids(hands_and_bids, 1)
    total_winnings = calculate_total_winnings(hab_by_rank)
    print(total_winnings)


def part_2(lines):
    hands_and_bids = parse_input(lines, 2)
    hab_by_rank = rank_hands_and_bids(hands_and_bids, 2)
    total_winnings = calculate_total_winnings(hab_by_rank)
    print(total_winnings)


def parse_input(lines, part):
    hands_and_bids = [(hand, int(bid)) for hand, bid in (line.split() for line in lines)]
    frequencies = [
        {"counts": Counter(hand), "hand": hand, "bid": bid}
        for hand, bid in hands_and_bids
    ]
    if part == 1:
        return frequencies
    if part == 2:
        return convert_jokers(frequencies)


def convert_jokers(frequencies):
    for f in frequencies:
        counter = f["counts"]
        if counter["J"] == 5:
            continue

        num_jokers = counter.pop("J", 0)
        most_common_card, _ = f["counts"].most_common(1)[0]
        counter[most_common_card] += num_jokers
    return frequencies


def rank_hands_and_bids(frequencies, part):
    return sorted(frequencies, key=cmp_to_key(lambda f1, f2: compare_hands(f1, f2, part)), reverse=True)


def calculate_total_winnings(sorted_values):
    sum = 0
    for i, item in enumerate(sorted_values):
        sum += item["bid"] * (i + 1)
    return sum


def compare_hands(f1, f2, part):
    counts1, counts2 = f1["counts"], f2["counts"]
    if len(counts1) < len(counts2):
        return -1
    elif len(counts2) < len(counts1):
        return 1

    # same length, check custom rules
    values1, values2 = counts1.values(), counts2.values()
    if len(counts1) == 2:
        # possible hands: 4-of-a-kind, or full house
        if 4 in values1 and 4 not in values2:
            return -1
        elif 4 not in values1 and 4 in values2:
            return 1

    if len(counts1) == 3:
        # possible hands: 3-of-a-kind, or 2 pairs
        if 3 in values1 and 3 not in values2:
            return -1
        elif 3 not in values1 and 3 in values2:
            return 1

    return compare_same_type_of_hands(f1, f2, part)


def compare_same_type_of_hands(f1, f2, part):
    chars = zip(f1["hand"], f2["hand"])
    ordering = "AKQJT98765432" if part == 1 else "AKQT98765432J"
    for l, r in chars:
        l_index, r_index = ordering.index(l), ordering.index(r)
        if l_index < r_index:
            return -1
        elif r_index < l_index:
            return 1
    print("same idx??")
    return 0


if __name__ == "__main__":
    main()