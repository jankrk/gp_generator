from antlr4 import *
from antlr.GPMiniLexer import GPMiniLexer
from antlr.GPMiniListener import GPMiniListener
from antlr.GPMiniParser import GPMiniParser
from antlr.MyGPMiniVisitor import MyGPMiniVisitor
from gpParser import GpParser
import math

class Fitness():
    def __init__(self, heuristic, config):
        self.heuristic = heuristic
        self.config = config
        self.input = []
        self.output = [] 
        self.prepare_data()
        
    def prepare_data(self):
        file = open(self.config.data, 'r')
        data = file.read().split('\n')

        for line in data:
            line = line.split(':')
            self.input.append(line[0].split())
            self.output.append(line[1].split())

    def fitness_function(self, indiv):
        fitness = 0
        output_generated = []

        #parse
        gpParser = GpParser(indiv)
        result = gpParser.parse()
        # result = 'var1 = -34;var4 = -53;var2 = input;var3 = -76;var4 = ((not false) >= true);output var2;var5 = input;if ((not ((not false) > (not false)))){output var4;}var6 = (-76 // var5);'

        # interpreter
        input_stream = InputStream(result)
        lexer = GPMiniLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = GPMiniParser(stream)
        tree = parser.program()
        for i in range(len(self.input)):
            visitor = MyGPMiniVisitor(self.config.max_interpreter_steps, self.input[i])
            tab = visitor.visitProgram(tree)
            output_generated = tab[0]
            fitness += tab[1] - self.config.max_interpreter_steps
            if 'ERROR' in output_generated:
                fitness -= math.inf
            else:
                fitness += self.heuristic.rate(self.config.heuristic, self.input[i], self.output[i], output_generated)
            # print(f"output_generated = {output_generated} \nfitness = {fitness}\n")
        return fitness