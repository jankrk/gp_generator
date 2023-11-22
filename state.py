import random 
from config import Config

class State:
    def __init__(self, syntax):
        self.current_indiv_index = None
        self.variables = []
        # it holds values of variables
        self.values = []
        self.stack = []
        self.syntax = syntax
        
    def init_new_indiv_state(self):
        if self.current_indiv_index == None:
            self.current_indiv_index = 0
        else:
            self.current_indiv_index += 1
        
        self.variables.append([])
        self.values.append({})
        self.stack.append([])
    
    def create_variable_with_initial_value(self, min_value, max_value):
        
        var_prefix = self.get_var_prefix()
        variable = f'{var_prefix}{len(self.variables[self.current_indiv_index])}'
        init_value = random.randint(min_value, max_value)
        self.variables[self.current_indiv_index].append(variable)
        self.values[self.current_indiv_index][variable] = init_value
        self._save_variable(variable)
        self._save_value(init_value)
        return (variable, init_value)
    

    def get_var_value(self, var):
        return self.values[self.current_indiv_index][var]
    
    def get_random_variable(self):
        var = random.choice(self.variables[self.current_indiv_index])
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

    def get_var_prefix(self):
        var_prefix = self.syntax['variable_prefix']
        return var_prefix

    def _get_current_stack(self):
        return self.stack[self.current_indiv_index]

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