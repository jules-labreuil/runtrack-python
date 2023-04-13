def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Le triangle est équilatéral.")
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Le triangle est rectangle isocèle.")
            else:
                print("Le triangle est isocèle.")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est rectangle.")
        else:
            print("Le triangle est quelconque.")
    else:
        print("Impossible de construire un triangle avec ces longueurs.")

type_triangle(5, 5, 5)
type_triangle(3, 5, 5)