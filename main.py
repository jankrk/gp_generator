import random
from config import Config
from state import State
from treeFactory import TreeFactory
from evolution import Evolution
from fitness import Fitness
from heuristic import Heuristic
import timeit

class TinyGPGenerator:
    def __init__(self):
        self.config = Config()
        self.state = State(self.config)
        self.heuristic = Heuristic()
        self.fitness = Fitness(self.heuristic, self.config)
        self.tree_factory = TreeFactory(self.state, self.fitness, self.config)
        self.evolution = Evolution(self.state, self.fitness, self.config)

    def run(self):
        self.config.assert_probabilities()

        # timeit
        start_time = timeit.default_timer()
        self.tree_factory.generate_population()
        end_time = timeit.default_timer()
        print(f"Time to generate population: {end_time - start_time}")

        v = self.evolution.evolve()
        
        self.end(v)
    
    def end(self, v):
        print('PROBLEM NOT SOLVED') if v != 1 else print('PROBLEM SOLVED')
        print('END')
        pass
        

if __name__ == "__main__":
    generator = TinyGPGenerator()
    generator.run()
