import random
from config import Config
from state import State

class TinyGPGenerator:
    def __init__(self, config=Config(), state=State()):
        self.config = config
        self.state = state

    def _generate_expression(self, depth=0):
        return self.state.choose_random_variable()

        if depth < 2 and random.random() < 0.5:
            # Choose random variable
            return self.choose_variable()
        else:
            # Generate an arithmetic expression
            left = self.generate_expression(depth + 1)
            operation = random.choice(self.operations)
            right = self.generate_expression(depth + 1)
            return f'({left} {operation} {right})'

    def _generate_condition(self):
        left = self._generate_expression()
        condition = random.choice(self.config.conditions)
        right = self._generate_expression()
        self.state.save_expression(condition, left, right)
        return f'{left} {condition} {right}'
    
    # Create random number of variables with random values from the range
    def _generate_initial_variables(self):
        for _ in range(random.randint(self.config.min_inital_vars, self.config.max_initial_vars)):
            self.state.create_variable_with_initial_value(self.config.min_var_initial_value, self.config.max_var_initial_value)

    def _print_config_probabilities(self):
        prev = 0
        for key, value in self.config.prob.items():
            prob = value - prev
            prev = value
            print(f'{key}: {prob}')



    def _generate_content(self, depth=0):
        content = ''
        
        if depth > self.config.max_depth:
            return content
        
        number_of_statements = random.randint(self.config.min_number_of_statements, self.config.max_number_of_statements)
        print('number_of_statements: ', number_of_statements)

        for _ in range(number_of_statements):
            random_number = random.randint(1, 100)

            # Generate variable declaration
            if random_number < self.config.prob['variable']:
                variable, init_value = self.state.create_variable_with_initial_value(self.config.min_var_initial_value, self.config.max_var_initial_value)
                content += f'int {variable} = {init_value};\n'
            
            # Generate while loop
            elif random_number < self.config.prob['while_loop']:
                self.state.save_while_loop()
                condition = self._generate_condition()
                self.state.save_open_expression()
                content += f'while ({condition}) {{\n'
                content += self._generate_content(depth + 1)
                content += '}\n'
                self.state.save_close_expression()

            elif random_number < self.config.prob['operation']:
                content += ''
            
            # Generate if statement
            elif random_number < self.config.prob['if_statement']:
                self.state.save_if_statement()
                condition = self._generate_condition()
                self.state.save_open_expression()
                content += f'if ({condition}) {{\n'
                content += self._generate_content(depth + 1)
                content += '}\n'
                self.state.save_close_expression()
        
        return content

    def _generate_program(self):
        self._generate_initial_variables()
        program = ''
        
        for var in self.state.variables:
            program += f'int {var} = {self.state.values[var]};\n'
        
        
        content = self._generate_content()
        program += content

        return program
    
    def run(self):
        self._print_config_probabilities()
        program = self._generate_program()
        print("program: ", self.state.program)
        return program
        

if __name__ == "__main__":
    generator = TinyGPGenerator()
    generated_program = generator.run()
    print("\n")
    print("GENERATED PROGRAM: \n")
    print(generated_program)