from heuristics.h1_1_A import h_1_1_A
from heuristics.h1_1_B import h_1_1_B
from heuristics.h1_1_C import h_1_1_C
from heuristics.h1_1_D import h_1_1_D
from heuristics.h1_1_E import h_1_1_E
from heuristics.h1_1_F import h_1_1_F
from heuristics.h1_2_A import h_1_2_A
from heuristics.h1_2_B import h_1_2_B
from heuristics.h1_2_C import h_1_2_C
from heuristics.h1_2_D import h_1_2_D
from heuristics.h1_2_E import h_1_2_E
from heuristics.h1_3_A import h_1_3_A
from heuristics.h1_3_B import h_1_3_B
from heuristics.h1_4_A import h_1_4_A
from heuristics.h1_4_B import h_1_4_B


class Heuristic:
    def __init__(self):
        self.problem = 1

    def rate(self, heuristic, input, output, output_generated):
        match heuristic:
            case '1.1.A':
                return h_1_1_A(input, output, output_generated)
            case '1.1.B':    
                return h_1_1_B(input, output, output_generated)
            case '1.1.C':    
                return h_1_1_C(input, output, output_generated)
            case '1.1.D':    
                return h_1_1_D(input, output, output_generated)
            case '1.1.E':
                return h_1_1_E(input, output, output_generated)
            case '1.1.F':
                return h_1_1_F(input, output, output_generated)
            case '1.2.A':
                return h_1_2_A(input, output, output_generated)
            case '1.2.B':
                return h_1_2_B(input, output, output_generated)
            case '1.2.C':
                return h_1_2_C(input, output, output_generated)
            case '1.2.D':
                return h_1_2_D(input, output, output_generated)
            case '1.2.E':
                return h_1_2_E(input, output, output_generated)
            case '1.3.A':
                return h_1_3_A(input, output, output_generated)
            case '1.3.B':
                return h_1_3_B(input, output, output_generated)
            case '1.4.A':
                return h_1_4_A(input, output, output_generated)
            case '1.4.B':
                return h_1_4_B(input, output, output_generated)
            case _:
                return 0