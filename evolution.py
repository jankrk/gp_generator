import random
from utils import Utils
from gpParser import GpParser

class Evolution(Utils):
    def __init__(self, state, fitness, config):
        self.state = state
        self.fitness = fitness
        self.config = config

    def _mutation(self, parent_index):
        parent_stack_copy = self.state.stack[parent_index][:]
        parent_stack_length = len(parent_stack_copy)
        
        for i in range(parent_stack_length):
            random_number = random.randint(0, 100)

            if random_number > self.config.mut_prob_per_node:
                continue

            token = parent_stack_copy[i]

            # If random token is a scope, input/output or equation, continue
            if (self.is_open_scope(token) or 
                self.is_close_scope(token) or
                self.is_input(token) or
                self.is_output(token) or
                self.is_equation(token)
            ):    
                continue

            elif self.is_operation(token):
                # Replace operation
                random_operation = self.choose_random_operation(token)
                parent_stack_copy[i] = random_operation
                # print(f"Mutated operation to from {token} to {random_operation} at index {i}")

            elif self.is_condition(token):
                # Replace condition
                random_condition = self.choose_random_condition(token)
                parent_stack_copy[i] = random_condition
                # print(f"Mutated condition to from {token} to {random_condition} at index {i}")
                
            
            elif self.is_if(token):
                # Replace if statement to while loop
                parent_stack_copy[i] = self.config.syntax['while']
                # print(f"Mutated if statement to while loop at index {i}")
                
            
            elif self.is_while(token):
                # Replace while loop to if statement
                parent_stack_copy[i] = self.config.syntax['if']
                # print(f"Mutated while loop to if statement at index {i}")
                
            elif self.is_logic(token):
                # Replace logic
                random_logic = self.choose_random_logic(token)
                parent_stack_copy[i] = random_logic
                # print(f"Mutated logic from {token} to {random_logic} at index {i}")

            elif self.is_constant(token):
                # Replace constant
                random_const = self.choose_random_const()
                parent_stack_copy[i] = random_const
                # print(f"Mutated constant from {token} to {random_const} at index {i}")

            elif self.is_variable(token):
                # Replace variable
                random_var_index = random.randint(0, len(self.state.variables[parent_index]) - 1)
                random_variable = self.state.variables[parent_index][random_var_index]
                parent_stack_copy[i] = random_variable
                # print(f"Mutated variable from {token} to {random_variable} at index {i}")


        return parent_stack_copy

    def _crossover(self, parent1_index, parent2_index):
        pass

    def _tournament(self):
        best = float('-inf')
        best_indiv_index = 0

        for _ in range(self.config.tournament_size):
            random_indiv_index = random.randint(0, self.config.population - 1)
            fitness = self.state.get_fitness(random_indiv_index)
            if fitness > best:
                best = fitness
                best_indiv_index = random_indiv_index
        
        return best_indiv_index
    
    def negative_tournament(self):
        worst = float('inf')
        worst_indiv_index = 0

        for _ in range(self.config.tournament_size):
            random_indiv_index = random.randint(0, self.config.population - 1)
            fitness = self.state.get_fitness(random_indiv_index)
            if fitness < worst:
                worst = fitness
                worst_indiv_index = random_indiv_index
        
        return worst_indiv_index
    
    def stats(self, g):
        fitness_avg = -sum(self.state.fitness) / len(self.state.fitness)
        best_fitness = max(self.state.fitness)
        best_indiv_index = self.state.fitness.index(best_fitness)
        best_indiv = self.state.stack[best_indiv_index]
        gpParser = GpParser(best_indiv)
        indiv = gpParser.parse()
        print(f"Generation: {g} \nAvg_fitness: {fitness_avg} \nBest_fitness: {-best_fitness} \nBest_individual: {indiv}\n")

    def problem_solved(self):
        best_indiv_index = self.state.fitness.index(0)
        best_indiv = self.state.stack[best_indiv_index]
        gpParser = GpParser(best_indiv)
        indiv = gpParser.parse()
        print(f"\n\n\nFound solution: {indiv}\n\n")
        return 1 
    
    def evolve(self):
        for g in range(self.config.generations):
            self.stats(g)
            if max(self.state.fitness) == 0:
                    return self.problem_solved()
                    
            # print(f"Generation {g}")
            for i in range(self.config.population):
                evolution_type = self.get_random_evolution_type()

                if evolution_type == 'crossover':
                    # print(f"Individual {i} will be crossed over")
                    # TODO: What if parents are the same?
                    parent1_index = self._tournament()
                    parent2_index = self._tournament()
                    continue
                    pass

                elif evolution_type == 'mutation':
                    indiv_index = self._tournament()
                    new_indiv = self._mutation(indiv_index)

                new_fitness = self.fitness.fitness_function(new_indiv)

                # Get worst individual and replace it with new individual
                offspring_index = self.negative_tournament()
                self.state.replace_indiv(offspring_index, new_indiv, new_fitness)
                
                
            

                

                

                
            