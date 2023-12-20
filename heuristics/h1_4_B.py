import math
'''
    1.4.B
    Program powinien odczytać na początek 
    z wejścia pierwszą liczbę 
    (ma być to wartość nieujemna) 
    a następnie tyle liczb (całkowitych) 
    jaka jest wartość pierwszej odczytanej liczby 
    i zwrócić na wyjściu (jedynie) ich 
    średnią arytmetyczną zaokrągloną 
    do pełnej liczby całkowitej 
    (do średniej nie jest wliczana 
    pierwsza odczytana liczba, która 
    mówi z ilu liczb chcemy obliczyć średnią). 
    Na wejściu mogą być tylko całkowite liczby 
    w zakresie [-99,99], pierwsza liczba może być 
    tylko w zakresie [0,99].
'''

def h_1_4_B(input, output, output_generated):
    rate = 0
    if len(output_generated) != 1:
        rate -= 100000
    if output_generated[0] != output[0]:
        rate -= math.abs(output_generated[0] - output[0])
    return rate