import random 

class Utils:
    def __init__(self, config):
        self.config = config

    def is_operation(self, token):
        return token in self.config.syntax['operations']
    
    def is_logic(self, token):
        return token in self.config.syntax['logic']
    
    def is_condition(self, token):
        return token in self.config.syntax['conditions']
    
    def is_equation(self, token):
        return token == self.config.syntax['equation']
    
    def is_output(self, token):
        return token == self.config.syntax['output']
    
    def is_input(self, token):
        return token == self.config.syntax['input']
    
    def is_if(self, token):
        return token == self.config.syntax['if']
    
    def is_while(self, token):
        return token == self.config.syntax['while']
    
    def is_open_scope(self, token):
        return token == self.config.syntax['open_scope']
    
    def is_close_scope(self, token):
        return token == self.config.syntax['close_scope']
    
    def is_variable(self, token):
        return token.startswith(self.config.syntax['variable_prefix'])
    
    def is_constant(self, token):
        return str(token).isdigit()
    
    def choose_random_operation(self, exclude=None):
        operations = self.config.syntax['operations'][:]
        if exclude:
            operations.remove(exclude)
        return random.choice(operations)
    
    def choose_random_logic(self, exclude=None):
        logic = self.config.syntax['logic'][:]
        if exclude:
            logic.remove(exclude)
        return random.choice(logic)
    
    def choose_random_condition(self, exclude=None):
        conditions = self.config.syntax['conditions'][:]
        if exclude:
            conditions.remove(exclude)
        return random.choice(self.config.syntax['conditions'])
    
    def choose_random_const(self):
        val = random.randint(self.config.min_const_val, self.config.max_const_val)
        return str(val)
    

    def get_random_key(self, obj):
        random_number = random.randint(1, 100)

        for key, value in obj.items():
            if random_number <= value:
                return key
            random_number -= value

    def get_random_block(self):
        block = self.get_random_key(self.config.block_prob)
        return block
    
    def get_random_operation_leaf(self):
        operation = self.get_random_key(self.config.operation_prob)
        return operation
        
    def get_random_equation_type(self):
        equation_type = self.get_random_key(self.config.equation_prob)
        return equation_type
    
    def get_random_evolution_type(self):
        evolution_type = self.get_random_key(self.config.evolution_prob)
        return evolution_type