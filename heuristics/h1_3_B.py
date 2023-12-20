'''
    1.3.B
    Program powinien odczytać 
    dwie pierwsze liczy z wejścia 
    i zwrócić na wyjściu (jedynie) większą z nich. 
    Na wejściu mogą być tylko 
    całkowite liczby w zakresie [-9999,9999]
'''

def h_1_3_B(input, output, output_generated):
    rate = 0
    if len(output_generated) != 1:
        rate -= 100000
    if output_generated[0] != max(input[0], input[1]):
        rate -= 100
    return rate