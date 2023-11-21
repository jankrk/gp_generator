import random 

class State:
    def __init__(self):
        self.variables = []
        # it holds values of variables
        self.values = {}
        self.program = []
        
    
    def create_variable_with_initial_value(self, min_value, max_value):
        variable = f'var{len(self.variables)}'
        init_value = random.randint(min_value, max_value)
        self.variables.append(variable)
        self.values[variable] = init_value
        self.program.append(variable)
        self.program.append(init_value)
        return (variable, init_value)
    

    def get_var_value(self, var):
        return self.values[var]
    
    def choose_random_variable(self):
        return random.choice(self.variables)
    
    def save_if_statement(self):
        self.program.append('if')

    def save_while_loop(self):
        self.program.append('while')

    def save_open_expression(self):
        self.program.append('{')

    def save_close_expression(self):
        self.program.append('}')

    def save_expression(self, condition, left, right):
        self.program.append(condition)
        self.program.append(left)
        self.program.append(right)