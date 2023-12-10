import random 
from config import Config

class State:
    def __init__(self, config=Config()):
        self.current_indiv_index = None
        self.variables = []
        self.stack = []
        self.config = config


    def init_new_indiv_state(self):
        if self.current_indiv_index == None:
            self.current_indiv_index = 0
        else:
            self.current_indiv_index += 1
        
        self.variables.append([])
        self.stack.append([])
    
    def create_new_variable(self):
        var_prefix = self.get_var_prefix()
        variable = f'{var_prefix}{len(self.variables[self.current_indiv_index])}'
        self._save_variable(variable)
        self.variables[self.current_indiv_index].append(variable)
        return variable

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

    
    def generate_random_const(self):
        val = random.randint(self.config.min_const_val, self.config.max_const_val)
        return str(val)
    


    # ------------------- GET -------------------

    def get_random_const(self):
        val = self.generate_random_const()
        self._save_value(val)
        return val
    
    def get_random_variable(self):
        var = random.choice(self.variables[self.current_indiv_index])
        self._save_variable(var)
        return var
    
    def get_while_loop(self):
        while_syntax = self.config.syntax['while']
        print("SAVEIONN G WHILE LOOP")
        self._save_while_loop(while_syntax)
        return while_syntax
    
    def get_if_statement(self):
        if_syntax = self.config.syntax['if']
        self._save_if_statement(if_syntax)
        return if_syntax   
     
    def get_random_condition(self):
        condition = random.choice(self.config.syntax['conditions'])
        self._save_condition(condition)
        return condition
    
    def get_random_operation(self):
        operation = random.choice(self.config.syntax['operations'])
        self._save_operation(operation)
        return operation
    
    def get_random_logic(self):
        logic = random.choice(self.config.syntax['logic'])
        self._save_logic(logic)
        return logic
    
    def get_open_scope(self):
        open_scope_syntax = self.config.syntax['open_scope']
        self._save_open_scope(open_scope_syntax)
        return open_scope_syntax
    
    def get_close_scope(self):
        close_scope_syntax = self.config.syntax['close_scope']
        self._save_close_scope(close_scope_syntax)
        return close_scope_syntax

    def get_var_prefix(self):
        var_prefix = self.config.syntax['variable_prefix']
        return var_prefix
    
    def get_input(self):
        input_syntax = self.config.syntax['input']
        self._save_input(input_syntax)
        return input_syntax
    
    def get_output(self):
        output_syntax = self.config.syntax['output']
        self._save_output(output_syntax)
        return output_syntax

    def get_equation(self):
        equation_syntax = self.config.syntax['equation']
        self._save_equation(equation_syntax)
        return equation_syntax



    def _get_current_stack(self):
        return self.stack[self.current_indiv_index]


    # ------------------- SAVE -------------------

    def _save_if_statement(self, if_syntax):
        stack = self._get_current_stack()
        stack.append(if_syntax)

    def _save_while_loop(self, while_syntax):
        stack = self._get_current_stack()
        stack.append(while_syntax)

    def _save_open_scope(self, open_scope_syntax):
        stack = self._get_current_stack()
        stack.append(open_scope_syntax)

    def _save_close_scope(self, close_scope_syntax):
        stack = self._get_current_stack()
        stack.append(close_scope_syntax)

    def _save_condition(self, condition):
        stack = self._get_current_stack()
        stack.append(condition)

    def _save_variable(self, variable):
        stack = self._get_current_stack()
        stack.append(variable)

    def _save_value(self, value):
        stack = self._get_current_stack()
        stack.append(value)
    
    def _save_operation(self, operation):
        stack = self._get_current_stack()
        stack.append(operation)

    def _save_input(self, input_syntax):
        stack = self._get_current_stack()
        stack.append(input_syntax)
    
    def _save_output(self, output_syntax):
        stack = self._get_current_stack()
        stack.append(output_syntax)

    def _save_equation(self, equation_syntax):
        stack = self._get_current_stack()
        stack.append(equation_syntax)

    def _save_logic(self, logic):
        stack = self._get_current_stack()
        stack.append(logic)