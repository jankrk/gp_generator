import random
from config import Config

class TreeFactory:
    def __init__(self, state, config=Config()):
        self.config = config
        self.state = state

    def _generate_expression(self, depth=0):
        if depth > self.config.max_expressions_depth or random.random() < (1 - self.config.complexity_of_expressions):
            random_num = random.randint(1, 100)
            
            if random_num < self.config.expression_prob['variable']:
                return self.state.get_random_variable()
            else:
                return self.state.get_random_const()
        else:
            # Choose an arithmetic expression
            operation = self.state.get_random_operation()

            left = self._generate_expression(depth + 1)
            right = self._generate_expression(depth + 1)
            return f'({left} {operation} {right})'

    def _generate_condition(self):
        # Generate and save a condition
        condition = self.state.get_random_condition()

        left = self._generate_expression()
        right = self._generate_expression()
        return f'{left} {condition} {right}'
    
    # Create random number of variables with random values from the range
    def _generate_initial_variables(self):
        for _ in range(random.randint(self.config.min_inital_vars, self.config.max_initial_vars)):
            self.state.create_variable_with_initial_value()


    def _generate_statement(self, depth=0):
        content = ''
        
        if depth > self.config.max_statements_depth:
            return content
        
        number_of_statements = random.randint(self.config.min_number_of_statements, self.config.max_number_of_statements)
        print('number_of_statements: ', number_of_statements)

        for _ in range(number_of_statements):
            random_number = random.randint(1, 100)

            # Generate variable declaration
            if random_number < self.config.prob['variable']:
                variable, init_value = self.state.create_variable_with_initial_value()
                content += f'int {variable} = {init_value};\n'
            
            # Generate while loop
            elif random_number < self.config.prob['while_loop']:
                while_loop_syntax = self.state.get_while_loop()
                condition = self._generate_condition()
                open_scope_syntax = self.state.get_open_scope()
                content += f'{while_loop_syntax} ({condition}) {open_scope_syntax}\n'
                content += self._generate_statement(depth + 1)
                close_scope_syntax = self.state.get_close_scope()
                content += f'{close_scope_syntax}\n'

            # Generate operation
            elif random_number < self.config.prob['operation']:
                variable = self.state.get_random_variable()
                expression = self._generate_expression()
                content += f'{variable} = {expression};\n'
            
            # Generate if statement
            elif random_number < self.config.prob['if_statement']:
                if_statement_syntax = self.state.get_if_statement()
                condition = self._generate_condition()
                open_scope_syntax = self.state.get_open_scope()
                content += f'{if_statement_syntax} ({condition}) {open_scope_syntax}\n'
                content += self._generate_statement(depth + 1)
                close_scope_syntax = self.state.get_close_scope()
                content += f'{close_scope_syntax}\n'
        
        return content

    def generate_population(self):
        population = []
        # Generate population of programs
        for _ in range(self.config.population):
            self.state.init_new_indiv_state()
            self._generate_initial_variables()
            program = ''
            
            for var in self.state.variables[self.state.current_indiv_index]:
                program += f'int {var} = {self.state.values[self.state.current_indiv_index][var]};\n'
            
            
            content = self._generate_statement()
            program += content

            population.append(program)
        return population
    
    
