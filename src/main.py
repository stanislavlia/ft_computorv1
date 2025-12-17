import sys
from expression_parser import ExpressionParser
from solver import Solver
from formatter import OutputFormatter


def get_equation_input():
    """Get equation from command line or STDIN"""
    
    # Check if argument provided
    if len(sys.argv) > 1:
        return sys.argv[1]
    
    # Otherwise read from STDIN
    print("Enter equation: ", end='')
    equation = sys.stdin.readline().strip()
    
    if not equation:
        print("Error: No equation provided")
        sys.exit(1)
    
    return equation


def solve_equation(equation_str):
    """Parse, solve, and display"""
    try:
        parser = ExpressionParser(strict_mode=True)
        left, right = parser.parse(equation_str)
        
        reduced_coefficient = ExpressionParser.reduce_equation(left, right)
        
        print(f"Reduced form: {OutputFormatter.format_reduced_form(reduced_coefficient)}")
        print(f"Polynomial degree: {Solver._get_poly_degree(reduced_coefficient)}")
        
        solver = Solver(reduced_coefficient)
        solution_type, discriminant, solutions = solver.solve()
        
        output = OutputFormatter.format_solution(solution_type, discriminant, solutions)
        print(output)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    equation = get_equation_input()
    solve_equation(equation)


if __name__ == "__main__":
    main()