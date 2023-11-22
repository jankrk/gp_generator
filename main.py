import random
from config import Config
from state import State
from tree_factory import TreeFactory

class TinyGPGenerator:
    def __init__(self, config=Config(), state=State(), tree_factory=TreeFactory):
        self.config = config
        self.state = state
        self.tree_factory = tree_factory(self.state)

    def _print_config_probabilities(self):
        prev = 0
        for key, value in self.config.prob.items():
            prob = value - prev
            prev = value
            print(f'{key}: {prob}')

    def run(self):
        self._print_config_probabilities()
        population = self.tree_factory.generate_population()

        for i, indiv in enumerate(population):
            print("\n")
            print("INDIVIDUAL: ", i)
            print("\n")
            print(indiv)
            print("\n")
            print("STACK: ", self.state.stack[i])

        return population
        

if __name__ == "__main__":
    generator = TinyGPGenerator()
    population = generator.run()
