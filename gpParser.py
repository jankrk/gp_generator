from config import Config


class GpParser:
    def __init__(self, config=Config()):
        self.config = config
        pass

    def _parse_input(self, data, i):
        return data[i]
    
    def _parse_operation(self, data, i):
        operation = data[i]
        i += 1

        left_side = ''
        if data[i] in self.config.syntax['operations']:
            left_side, i = self._parse_operation(data, i)
            i += 1
        else:
            left_side = data[i]
            i += 1
        
        right_side = ''
        if data[i] in self.config.syntax['operations']:
            right_side, i = self._parse_operation(data, i)
            # i += 1
        else:
            right_side = data[i]

        res = f"{left_side} {operation} {right_side}"
        return res, i



    def _parse_equation(self, data, i):
        i += 1
        left_side = data[i]
        i += 1
        right_side = ''
        
        if data[i] == self.config.syntax['input']:
            right_side = self._parse_input(data, i)
        
        elif data[i].isdigit():
            right_side = data[i]

        elif data[i] in self.config.syntax['operations']:
            right_side, i = self._parse_operation(data, i)

        
        res = f"{left_side} = {right_side};"
        return res, i
    
    # def _parse_condition(self, data, i):
    #     condition = data[i]
    #     i += 1

    #     left_side = ''
    #     right_side = ''

    #     if data[i] in self.config.syntax['logic']:
    #         left_side, i = self._parse_logic(data, i)
    #     elif data[i] in self.config.syntax['conditions']:
    #         pass
            
    # def _parse_logic(self, data, i):
    #     logic_expression = data[i]
    #     i += 1

    #     left_side = ''
    #     right_side = ''

    #     if data[i] in self.config.syntax['logic']:
    #         left_side, i = self._parse_logic(data, i)
    #     elif data[i] in self.config.syntax['conditions']:
    #         pass 

    def _parse_output(self, data, i): 
        output = data[i]
        i += 1
        variable = data[i]
        res = f"{output} {variable};"
        return res, i

    def parse(self, data):
        content = ''
        i = 0
        while i < len(data):
            if data[i] == self.config.syntax['equation']:
                res, i = self._parse_equation(data, i)
                print(res + '\n')
                content += res
            elif data[i] == self.config.syntax['output']:
                res, i = self._parse_output(data, i)
                print(res + '\n')
                content += res
            elif data[i] in self.config.syntax['logic']:
                print(f"LOGIC: {data[i]}")
                content += data[i]

            i += 1

        return content


data = ['=', 'var0', 'input', '=', 'var1', '16', '=', 'var2', 'input', '=', 'var4', '+', '-', '1', '*', '5', '2', '3', '=', 'var0', 'input']
gpParser = GpParser()
res = gpParser.parse(data)
print("RES: ", res)