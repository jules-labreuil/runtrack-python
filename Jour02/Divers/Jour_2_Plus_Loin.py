def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Le triangle est équilatéral."
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Le triangle est rectangle isocèle."
            else:
                return "Le triangle est isocèle."
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Le triangle est rectangle."
        else:
            return "Le triangle est quelconque."
    else:
        return "Impossible de construire un triangle avec ces longueurs."

print(type_triangle(5, 5, 5))