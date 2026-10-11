for c in (65, 97):
    for i in range(26):
        print(i + c, end=" ")
    print()

for shift in range(14):
    d = {}  # mapa

    for c in (65, 97):  # zaczynamy od A, kończymy na Z, potem zaczynamy od a, kończymy na z
        for i in range(26):  # alfabet musi mieć 26 liter
            d[chr(i + c)] = chr((i + shift) % 26 + c)

    print()
    print()
    print(f"Przesunięcie o {shift}:")
    print(" ".join(d.keys()))
    print(" ".join(d.values()))