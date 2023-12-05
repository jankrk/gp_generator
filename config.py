class Config:
    def __init__(self):
        self.min_inital_vars = 1
        self.max_initial_vars = 5

        self.min_const_val = 1
        self.max_const_val = 30

        self.min_number_of_statements = 1
        self.max_number_of_statements = 5

        self.max_statements_depth = 2
        self.max_expressions_depth = 2
        self.max_mutation_depth = 5

        self.population = 5
        self.generations = 5
        self.tournament_size = 1

        self.evolution_prob = {
            'crossover': 20,
            'mutation': 100
        }
        
        self.prob = {
            'variable': 30,
            'while_loop': 50,
            'operation': 90,
            'if_statement': 100
        }

        self.expression_prob = {
            'variable': 50,
            'const': 100,
        }

        # between 0 and 1
        # 0 means no complexity
        # 1 means max complexity
        self.complexity_of_expressions = 0.7

        self.syntax = {
            'if': 'if',
            'while': 'while',
            'open_scope': '{',
            'close_scope': '}',
            'operations': ['+', '-', '*', '/'],
            'conditions': ['<', '>', '==', '!='],
            'variable_prefix': 'var',
        }
