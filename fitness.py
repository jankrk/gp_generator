import random
from gpParser import GpParser

class Fitness():
    def fitness_function(self, indiv):
        random_number = random.randint(1, 100)
        gpParser = GpParser(indiv)
        result = gpParser.parse()
        print(result + "\n\n")
        return random_number