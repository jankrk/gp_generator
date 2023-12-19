'''
    1.1.F
    Program powinien wygenerować 
    na wyjściu liczbę jako jedyną liczbę 1. 
    Poza liczbą 1 NIE powinien nic więcej wygenerować.
'''

def h_1_1_F(input, output, output_generated):
    rate = 0
    if len(output_generated) != 1:
        rate -= 1000
    if output_generated[0] != 1:
        rate -= 100
    return rate