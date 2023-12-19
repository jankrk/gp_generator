'''
    1.1.B 
    Program powinien wygenerować na wyjściu 
    (na dowolnej pozycji w danych wyjściowych) 
    liczbę 789. 
    Poza liczbą 789 może też zwrócić inne liczby.
'''

def h_1_1_B(input, output, output_generated):
    rate = 0
    if 789 not in output_generated:
        rate -= 100
    return rate