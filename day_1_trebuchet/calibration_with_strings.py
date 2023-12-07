with open("calibration.txt") as f:
    s = f.read()

m = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

r = 0
for x in s.strip().split("\n"):
    fst = None
    lst = None
    s=""
    for c in x:
        dig = None
        if c.isdigit():
            dig=c
        else:
            s+=c
            for k,v in m.items():
                if s.endswith(k):
                    dig = str(v)
        if dig is not None:
            lst = dig
            if fst is None:
                fst = dig
    r += int(fst+lst)

print(r)