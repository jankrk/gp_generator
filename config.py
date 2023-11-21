class Config:
    def __init__(self):
        self.min_inital_vars = 1
        self.max_initial_vars = 5

        self.min_var_initial_value = 0
        self.max_var_initial_value = 10

        self.min_number_of_statements = 1
        self.max_number_of_statements = 5

        self.max_depth = 2
        
        self.prob = {
            'variable': 30,
            'while_loop': 50,
            'operation': 90,
            'if_statement': 100
        }


        self.operations = ['+', '-', '*', '/']
        self.conditions = ['<', '>', '==', '!=']
