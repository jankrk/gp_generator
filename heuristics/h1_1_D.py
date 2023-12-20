'''
    1.1.D
    Program powinien wygenerować 
    na pierwszej pozycji na wyjściu liczbę 1. 
    Poza liczbą 1 może też zwrócić inne liczby.
'''

def h_1_1_D(input, output, output_generated):
    rate = 0
    if output_generated[0] != 1:
        rate -= abs(1 - output_generated[0])
    return rate