import random
from config import Config
from state import State
from treeFactory import TreeFactory
from evolution import Evolution

class TinyGPGenerator:
    def __init__(self, config=Config(), state=State(), tree_factory=TreeFactory):
        self.config = config
        self.state = state
        self.tree_factory = tree_factory(self.state)

    def write_to_file(self):
        with open('output.txt', 'w') as f:
            for indiv_stack in self.state.stack:
                f.write(str(indiv_stack))
                f.write('\n\n')

    def run(self):
        self.config.assert_probabilities()
        self.tree_factory.generate_population()

        evolution = Evolution(self.state)
        evolution.evolve()
        
        self.write_to_file()
        

if __name__ == "__main__":
    generator = TinyGPGenerator()
    generator.run()
