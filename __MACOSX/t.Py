s = "Python jest super"

d = {}

for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in s]))


d = {}  # mapa znak -> znak

for c in (65, 97):  # zaczynamy od A, kończymy na Z, potem zaczynamy od a, kończymy na z
    for i in range(26):  # alfabet musi mieć 26 liter. Między A i Z oraz a i z muszą być kolejne litery alfabetu łacińskiego
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in s]))

s = "Hello World"

d = {}  # mapa znak -> znak

for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

print("".join([d.get(c, c) for c in s]))

for c in (65, 97):
    for i in range(26):
        print((i + 13) % 26 + c, end=" ")
    print()

for c in (65, 97):
    for i in range(26):
        print(i + c, end=" ")
    print()

for c in (65, 97):
    for i in range(26):
        print((i + 13) % 26 + c, end=" ")
    print()