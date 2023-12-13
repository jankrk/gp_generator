import random
from config import Config
from utils import Utils

class TreeFactory(Utils):
    def __init__(self, state, config=Config()):
        super().__init__(config)
        self.state = state


    def _generate_operation(self, depth=1):
        if depth > self.config.max_operations_depth or random.random() < (1 - self.config.complexity_of_operations):
            
            operation_leaf = self.get_random_operation_leaf()
            if operation_leaf == 'variable':
                self.state.get_random_variable()
            elif operation_leaf == 'constant':
                self.state.get_random_const()
        else: 
            # Choose an arithmetic expression
            self.state.get_random_operation()
            self._generate_operation(depth + 1)
            self._generate_operation(depth + 1)

    def _generate_condition(self):
        self.state.get_random_condition()
        self._generate_operation()
        self._generate_operation()
    
    def _generate_logic(self, depth=1):
        if depth > self.config.max_logic_depth or random.random() < (1 - self.config.complexity_of_logic):
            self._generate_condition()
        else:
            self.state.get_random_logic()
            self._generate_logic(depth + 1)
            self._generate_logic(depth + 1)
    
    def _generate_equation(self):
        self.state.get_equation()
        equation_type = self.get_random_equation_type()
        
        if equation_type == 'input':
            self.state.create_new_variable()
            self.state.get_input()
            return
        
        random_number = random.randint(1, 100)
        # Left side of the equation
        if random_number < 50:
            # Create new variable
            self.state.create_new_variable()
        else:
            # Choose existing variable
            self.state.get_random_variable()

        # Right side of the equation
        if equation_type == 'operation':
            self._generate_operation()
        elif equation_type == 'logic':
            self._generate_logic()

    def _generate_input(self):
        self.state.create_new_variable()
        self.state.get_input()
        
    def _generate_while(self, depth):
        self.state.get_while_loop()
        self._generate_logic()
        self.state.get_open_scope()
        self._generate_block(depth)
        self.state.get_close_scope()

    def _generate_if(self, depth):
        self.state.get_if_statement()
        self._generate_logic()
        self.state.get_open_scope()
        self._generate_block(depth)
        self.state.get_close_scope()

    def _generate_output(self):
        self.state.get_output()
        self.state.get_random_variable()


    def _generate_block(self, depth=1):
        number_of_blocks = random.randint(self.config.min_blocks, self.config.max_blocks)
        for _ in range(number_of_blocks):
            block = self.get_random_block()

            if block == 'equation':
                self._generate_equation()

            elif block == 'while':
                # If max depth is reached, skip while loop
                # because while loop creates a new block inside of it
                if depth == self.config.max_blocks_depth:
                    continue
                self._generate_while(depth + 1)

            elif block == 'if':
                # If max depth is reached, skip while loop
                # because if creates a new block inside of it
                if depth == self.config.max_blocks_depth:
                    continue
                self._generate_if(depth + 1)

            elif block == 'output':
                self._generate_output()

    # Create random number of variables with random values
    def _generate_initial_variables(self):
        for _ in range(random.randint(self.config.min_inital_vars, self.config.max_initial_vars)):
            self.state.get_equation()
            self.state.create_new_variable()

            random_number = random.randint(1, 100)

            if random_number < 50:
                self.state.get_random_const()
            else:
                self.state.get_input()

    def generate_population(self):
        for _ in range(self.config.population):
            self.state.init_new_indiv_state()
            self._generate_initial_variables()            
            self._generate_block()
    
