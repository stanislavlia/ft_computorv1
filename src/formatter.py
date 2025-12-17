
class OutputFormatter:
    """Format solver output according to project requirements"""
    
    @staticmethod
    def format_solution(solution_type, discriminant, solutions):

        if solution_type == 'positive':
            # Two distinct real solutions
            return (
                f"Discriminant is strictly positive, the two solutions are:\n"
                f"{solutions[0]}\n"
                f"{solutions[1]}"
            )
        
        elif solution_type == 'zero':
            # One real solution (double root)
            return (
                f"The solution is:\n"
                f"{solutions[0]}"
            )
        
        elif solution_type == 'negative':
            # Two complex conjugate solutions
            return (
                f"Discriminant is strictly negative, the two complex solutions are:\n"
                f"{solutions[0]}\n"
                f"{solutions[1]}"
            )
        
        elif solution_type == 'linear':
            # One solution from linear equation
            return (
                f"The solution is:\n"
                f"{solutions[0]}"
            )
        
        elif solution_type == 'infinite':
            # All real numbers are solutions (0 = 0)
            return "Any real number is a solution."
        
        elif solution_type == 'none':
            # No solution (contradiction like 5 = 0)
            return "No solution."
        
        elif solution_type == 'unsolvable':
            # Degree > 2
            return "The polynomial degree is strictly greater than 2, I can't solve."
        
        else:
            return "Unknown solution type."
    
    @staticmethod
    def format_reduced_form(coefficients):
    
        if not coefficients:
            return "0 = 0"
        
        # Sort terms by degree
        sorted_degrees = sorted(coefficients.keys())
        
        # Build the string
        terms = []
        for degree in sorted_degrees:
            coef = coefficients[degree]
            
            # Format coefficient with sign
            if terms:  # Not the first term
                if coef >= 0:
                    terms.append(f"+ {coef} * X^{degree}")
                else:
                    terms.append(f"- {-coef} * X^{degree}")
            else:  # First term
                terms.append(f"{coef} * X^{degree}")
        
        return " ".join(terms) + " = 0"
    
    @staticmethod
    def format_polynomial_degree(degree):
        return f"Polynomial degree: {degree}"