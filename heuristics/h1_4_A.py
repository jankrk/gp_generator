'''
    1.4.A
    Program powinien odczytać 
    dziesięć pierwszych liczy z wejścia 
    i zwrócić na wyjściu (jedynie) ich 
    średnią arytmetyczną 
    (zaokrągloną do pełnej liczby całkowitej). 
    Na wejściu mogą być tylko 
    całkowite liczby w zakresie [-99,99]
'''

def h_1_4_A(input, output, output_generated):
    rate = 0
    if len(output_generated) != 1:
        rate -= 100000
    if output_generated[0] != output[0]:
        rate -= abs(output_generated[0] - output[0])
    return rate