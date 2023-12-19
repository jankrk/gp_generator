'''
    1.1.C 
    Program powinien wygenerować na wyjściu 
    (na dowolnej pozycji w danych wyjściowych) 
    liczbę 31415. 
    Poza liczbą 31415 może też zwrócić inne liczby.
'''

def h_1_1_C(input, output, output_generated):
    rate = 0
    if 31415 not in output_generated:
        rate -= 100
    return rate