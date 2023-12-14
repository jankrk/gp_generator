class Config:
    def __init__(self):
        self.min_inital_vars = 1
        self.max_initial_vars = 4

        self.min_const_val = 1
        self.max_const_val = 100

        self.min_blocks = 2
        self.max_blocks = 5

        self.max_blocks_depth = 3
        self.max_operations_depth = 2
        self.max_logic_depth = 2

        # between 0 and 1
        # 0 means no complexity
        # 1 means max complexity
        self.complexity_of_operations = 0.1
        self.complexity_of_logic = 0.1

        self.population = 3
        self.generations = 5
        self.tournament_size = 1

        self.evolution_prob = {
            'crossover': 20,
            'mutation': 80
        }

        # max 100
        self.mut_prob_per_node = 10
        
        self.block_prob = {
            'equation': 25,
            'while': 25,
            'if': 25,
            'output': 25,
        }

        # Use more vars or consts?
        self.operation_prob = {
            'variable': 50,
            'constant': 50,
        }

        self.equation_prob = {
            'operation': 34,
            'logic': 33,
            'input': 33,
        }

        self.syntax = {
            'if': 'if',
            'while': 'while',
            'open_scope': '{',
            'close_scope': '}',
            'equation': '=',
            'operations': ['+', '-', '*', '/'],
            'conditions': ['<', '>', '==', '!=', '>=', '<='],
            'logic': ['and', 'or'],
            'variable_prefix': 'var',
            'input': 'input',
            'output': 'output'
        }

    def assert_probabilities(self):
        assert sum(self.block_prob.values()) == 100, "Block probabilities should sum up to 100"
        assert sum(self.operation_prob.values()) == 100, "Expression probabilities should sum up to 100"
        assert sum(self.evolution_prob.values()) == 100, "Evolution probabilities should sum up to 100"
        assert sum(self.equation_prob.values()) == 100, "Equation probabilities should sum up to 100"