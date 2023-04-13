def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_superieur = ((note + 2) // 5) * 5
            if multiple_de_5_superieur - note < 3:
                notes_arrondies.append(multiple_de_5_superieur)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

notes = [38, 42, 83, 77, 58, 91, 49]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)  