'''
    1.1.E
    Program powinien wygenerować 
    na pierwszej pozycji na wyjściu liczbę 789. 
    Poza liczbą 789 może też zwrócić inne liczby.
'''

def h_1_1_E(input, output, output_generated):
    rate = 0
    if output_generated[0] != 789:
        rate -= 100
    return rate