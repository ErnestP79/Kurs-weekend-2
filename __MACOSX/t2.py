dni_robocze = {
    "Mon": "poniedziałek",
    "Tue": "wtorek",
    "Wed": "środa",
    "Thu": "czwartek",
    "Fri": "piątek",
    "Sat": None,
    "Sun": None,
}

weekendy = {
    "Sat": "sobota",
    "Sun": "niedziela",
}

nazwy_dni = {
    **dni_robocze,
    **weekendy,
}

print(weekendy.items())

print(weekendy.values())

print(weekendy.keys())

print(weekendy.get("Sat"))

print(dni_robocze)
print(weekendy)
print(nazwy_dni)