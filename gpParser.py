from config import Config
from utils import Utils

class GpParser(Utils):
    def __init__(self, data, config=Config()):
        super().__init__(config)
        self.data = data
        self.iterator = 0
        self.length = len(data)
        self.result = ''

    def increment_iterator(self):
        self.iterator += 1

    def current_token(self):
        return self.data[self.iterator]

    def next_token(self):
        self.increment_iterator()
        return self.current_token()

    def add_to_result(self, parsed_string):
        self.result += parsed_string
    
    def _parse_operation(self):
        operation_token = self.current_token()
        token = self.next_token()

        left_side = ''
        if self.is_operation(token):
            left_side = self._parse_operation()
        else:
            left_side = token
        
        token = self.next_token()
        right_side = ''
        if self.is_operation(token):
            right_side = self._parse_operation()
        else:
            right_side = token

        parsed = f"({left_side} {operation_token} {right_side})"
        return parsed
    
    def _parse_condition(self):
        condition_token = self.current_token()
        token = self.next_token()

        left_side = ''
        if self.is_operation(token):
            left_side = self._parse_condition()
        else:
            left_side = token
        
        token = self.next_token()
        right_side = ''
        if self.is_operation(token):
            right_side = self._parse_condition()
        else:
            right_side = token

        parsed = f"({left_side} {condition_token} {right_side})"
        return parsed

    def _parse_logic(self):
        logic_token = self.current_token()
        token = self.next_token()

        left_side = ''
        if self.is_logic(token):
            left_side = self._parse_logic()
        elif self.is_condition(token):
            left_side = self._parse_condition()
        else:
            left_side = token

        right_side = ''
        token = self.next_token()
        if self.is_logic(token):
            right_side = self._parse_logic()
        elif self.is_condition(token):
            right_side = self._parse_condition()
        else:
            right_side = token

        parsed = f"({left_side} {logic_token} {right_side})"
        return parsed

    def _parse_equation(self):
        left_side = self.next_token()
        token = self.next_token()
        right_side = ''
        
        if self.is_input(token) or token.isdigit():
            right_side = token

        elif self.is_operation(token):
            right_side = self._parse_operation()

        elif self.is_logic(token):
            right_side = self._parse_logic()

        elif self.is_condition(token):
            right_side = self._parse_condition()

        else:
            right_side = token
        
        parsed = f"{left_side} = {right_side};"
        return parsed
        

    def _parse_output(self): 
        output_token = self.current_token()
        variable_token = self.next_token()
        parsed = f"{output_token} {variable_token};"
        return parsed
    
    def _parse_if(self):
        if_token = self.current_token()
        token = self.next_token()
        condition = ''

        if self.is_logic(token):
            condition = self._parse_logic()
        elif self.is_condition(token):
            condition = self._parse_condition()
        else:
            condition = token

        parsed = f"{if_token} ({condition})"
        return parsed
    
    def _parse_while(self):
        while_token = self.current_token()
        token = self.next_token()
        condition = ''

        if self.is_logic(token):
            condition = self._parse_logic()
        elif self.is_condition(token):
            condition = self._parse_condition()
        else:
            condition = token

        parsed = f"{while_token} ({condition})"
        return parsed

    def parse(self):
        while self.iterator < self.length:
            token = self.current_token()
            parsed = ''

            if self.is_equation(token):
                parsed = self._parse_equation()
            elif self.is_output(token):
                parsed = self._parse_output()
            elif self.is_logic(token):
                parsed = self._parse_logic()
            elif self.is_if(token):
                parsed = self._parse_if()
            elif self.is_while(token):
                parsed = self._parse_while()
            elif self.is_open_scope(token):
                parsed = token
            elif self.is_close_scope(token):
                parsed = token
            
            self.add_to_result(parsed)
            self.increment_iterator()

        return self.result


# read from output.txt
# with open('output.txt', 'r') as f:
#     data = f.read()

# data = [elem.strip().replace("'", "") for elem in data.strip()[1:-1].split(',')]
# gpParser = GpParser(data)
# res = gpParser.parse()
# print("RES: ", res)