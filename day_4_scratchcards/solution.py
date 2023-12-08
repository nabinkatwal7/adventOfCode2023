t = 0
m = {}

for i, x in enumerate(open('input.txt', 'r')):
    if i not in m:
        m[i] = 1
    x = x.split(":")[1].strip()
    a, b = [list(map(int, k.split())) for k in x.split(" | ")]
    j = sum(q in a for q in b)
    if j > 0:
        t += 2**(j-1)

    for n in range(i+1, i+j+1):
        m[n] = m.get(n, 1) + m[i]

print(f"part 1 answer is {t}")
print(f"part 2 answer is {sum(m.values())}")
