import random 
from config import Config

class State:
    def __init__(self, syntax):
        self.variables = []
        # it holds values of variables
        self.values = {}
        self.stack = []
        self.syntax = syntax
        
    
    def create_variable_with_initial_value(self, min_value, max_value):
        variable = f'var{len(self.variables)}'
        init_value = random.randint(min_value, max_value)
        self.variables.append(variable)
        self.values[variable] = init_value
        self._save_variable(variable)
        self._save_value(init_value)
        return (variable, init_value)
    

    def get_var_value(self, var):
        return self.values[var]
    
    def get_random_variable(self):
        var = random.choice(self.variables)
        self._save_variable(var)
        return var
    
    def get_while_loop(self):
        while_syntax = self.syntax['while']
        self._save_while_loop(while_syntax)
        return while_syntax
    
    def get_if_statement(self):
        if_syntax = self.syntax['if']
        self._save_if_statement(if_syntax)
        return if_syntax   
     
    def get_random_condition(self):
        condition = random.choice(self.syntax['conditions'])
        self._save_condition(condition)
        return condition
    
    def get_random_operation(self):
        operation = random.choice(self.syntax['operations'])
        self._save_operation(operation)
        return operation
    
    def get_open_scope(self):
        open_scope_syntax = self.syntax['open_scope']
        self._save_open_scope(open_scope_syntax)
        return open_scope_syntax
    
    def get_close_scope(self):
        close_scope_syntax = self.syntax['close_scope']
        self._save_close_scope(close_scope_syntax)
        return close_scope_syntax


    def _save_if_statement(self, if_syntax):
        self.stack.append(if_syntax)

    def _save_while_loop(self, while_syntax):
        self.stack.append(while_syntax)

    def _save_open_scope(self, open_scope_syntax):
        self.stack.append(open_scope_syntax)

    def _save_close_scope(self, close_scope_syntax):
        self.stack.append(close_scope_syntax)

    def _save_condition(self, condition):
        self.stack.append(condition)

    def _save_variable(self, variable):
        self.stack.append(variable)

    def _save_value(self, value):
        self.stack.append(value)
    
    def _save_operation(self, operation):
        self.stack.append(operation)