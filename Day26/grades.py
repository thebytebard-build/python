#this is student grade mosule and it will be use for future import in try.py

def calculate_grade(grade):
    match grade:
        case g if g >= 90:
            return 'A'
        case g if g >= 80:
            return 'B'
        case g if g >= 70:
            return 'C'
        case g if g >= 60:
            return 'D'
        case _:
            return 'F'

