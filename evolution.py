import random
from config import Config
from utils import Utils

class Evolution(Utils):
    def __init__(self, state, config=Config()):
        super().__init__(config)
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
        random_token = indiv_stack[random_index]

        print(f"Individual {indiv_index} will be mutated using token {random_token}")

        # If random token is a scope, retry mutation
        if (self.is_open_scope(random_token) or 
            self.is_close_scope(random_token) or
            self.is_input(random_token) or
            self.is_output(random_token)
        ):    
            self._mutation(indiv_index)

        elif self.is_operation(random_token):
            # Replace operation
            random_operation = self.choose_random_operation(random_token)
            self.state.stack[indiv_index][random_index] = random_operation
            print(f"Mutated operation to from {random_token} to {random_operation} at index {random_index}")

        elif self.is_condition(random_token):
            # Replace condition
            random_condition = self.choose_random_condition(random_token)
            self.state.stack[indiv_index][random_index] = random_condition
            print(f"Mutated condition to from {random_token} to {random_condition} at index {random_index}")
            
        
        elif self.is_if(random_token):
            # Replace if statement to while loop
            self.state.stack[indiv_index][random_index] = self.config.syntax['while']
            print(f"Mutated if statement to while loop at index {random_index}")
            
        
        elif self.is_while(random_token):
            # Replace while loop to if statement
            self.state.stack[indiv_index][random_index] = self.config.syntax['if']
            print(f"Mutated while loop to if statement at index {random_index}")
            
        elif self.is_logic(random_token):
            # Replace logic
            random_logic = self.choose_random_logic(random_token)
            self.state.stack[indiv_index][random_index] = random_logic
            print(f"Mutated logic from {random_token} to {random_logic} at index {random_index}")

        elif self.is_constant(random_token):
            # Replace constant
            random_const = self.choose_random_const()
            self.state.stack[indiv_index][random_index] = random_const
            print(f"Mutated constant from {random_token} to {random_const} at index {random_index}")

        elif self.is_variable(random_token):
            # Replace variable
            random_var_index = random.randint(0, len(self.state.variables[indiv_index]) - 1)
            random_variable = self.state.variables[indiv_index][random_var_index]
            self.state.stack[indiv_index][random_index] = random_variable
            print(f"Mutated variable from {random_token} to {random_variable} at index {random_index}")


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
                evolution_type = self.get_random_evolution_type()

                if evolution_type == 'crossover':
                    print(f"Individual {i} will be crossed over")
                    pass

                elif evolution_type == 'mutation':
                    indiv_index = self._tournament()
                    self._mutation(indiv_index)
                    print("After mutation: ")
                    print(self.state.stack[indiv_index])
            