import random
from config import Config

class Evolution:
    def __init__(self, state, config=Config()):
        self.config = config
        self.state = state
    

    def _get_fintess(self, indiv_index):
        return 0
    
    def _mutation(self, indiv_index, depth=0):
        if depth > self.config.max_mutation_depth:
            return
        indiv_stack = self.state.stack[indiv_index]
        indiv_stack_len = len(indiv_stack)

        if indiv_stack_len == 0:
            return
        
        random_index = random.randint(0, indiv_stack_len - 1)
        random_element = indiv_stack[random_index]

        # If we encounter a scope, we retry the mutation
        if random_element in ["{" , "}"]:
            return self._mutation(indiv_index)

        if random_element in self.config.syntax['operations']:
            # Replace operation
            random_operation = random.choice(self.config.syntax['operations'])
            self.state.stack[indiv_index][random_index] = random_operation
            print(f"Mutated operation to from {random_element} to {random_operation} at index {random_index}")
            return

        if random_element in self.config.syntax['conditions']:
            # Replace condition
            random_condition = random.choice(self.config.syntax['conditions'])
            self.state.stack[indiv_index][random_index] = random_condition
            print(f"Mutated condition to from {random_element} to {random_condition} at index {random_index}")
            return
        
        if random_element == self.config.syntax['if']:
            # Replace if statement to while loop
            self.state.stack[indiv_index][random_index] = self.config.syntax['while']
            print(f"Mutated if statement to while loop at index {random_index}")
            return
        
        if random_element == self.config.syntax['while']:
            # Replace while loop to if statement
            self.state.stack[indiv_index][random_index] = self.config.syntax['if']
            print(f"Mutated while loop to if statement at index {random_index}")
            return

        if isinstance(random_element, (int, float, complex)):
            # Replace constant
            random_const = self.state.generate_random_const()
            self.state.stack[indiv_index][random_index] = random_const
            print(f"Mutated constant from {random_element} to {random_const} at index {random_index}")
            return

        if random_element.startswith(self.config.syntax['variable_prefix']):
            # Replace variable
            random_var_index = random.randint(0, len(self.state.variables[indiv_index]) - 1)
            random_variable = self.state.variables[indiv_index][random_var_index]
            self.state.stack[indiv_index][random_index] = random_variable
            print(f"Mutated variable from {random_element} to {random_variable} at index {random_index}")
            return


    def _tournament(self):
        best = float('inf')
        best_indiv_index = None

        for _ in range(self.config.tournament_size):
            random_indiv_index = random.randint(0, self.config.population - 1)
            fitness = self._get_fintess(random_indiv_index)
            if fitness < best:
                best = fitness
                best_indiv_index = random_indiv_index
        
        return best_indiv_index

    def evolve(self):
        for g in range(self.config.generations):
            print(f"Generation {g}")
            for i in range(self.config.population):
                random_number = random.randint(1, 100)

                if random_number < self.config.evolution_prob['crossover']:
                    # Crossover
                    print(f"Individual {i} will be crossed over")
                    pass
                elif random_number < self.config.evolution_prob['mutation']:
                    # Mutation
                    indiv_index = self._tournament()
                    print(f"Individual {i} will be mutated")
                    print("Before mutation: ")
                    print(self.state.stack[indiv_index])
                    self._mutation(indiv_index)
                    print("After mutation: ")
                    print(self.state.stack[indiv_index])
            