import re

TERM_PATTERN = r'([+-]?)(\d+\.?\d*)\*X\^(\d+)'
VALID_CHARS_PATTERN = r'^[0-9\+\-\*\.\^X=]+$'

class ExpressionParser:
    """
    Parser for polynomial equations.
    Handles parsing, validation, and term extraction.
    """
    
    def __init__(self, strict_mode=False):
        self.term_pattern = TERM_PATTERN
        self.strict_mode = strict_mode
        
    def parse(self, equation_str):

        equation = self._normalize(equation_str)
        self._validate_equation(equation)
        left_side, right_side = self._split_equation(equation)
        left_terms = self._extract_terms(left_side)
        right_terms = self._extract_terms(right_side)
        
        if self.strict_mode:
            self._validate_terms(left_terms, right_terms)
        
        return left_terms, right_terms
    
    def _normalize(self, equation_str):
        return equation_str.replace(" ", "")
    
    def _split_equation(self, equation):
        parts = equation.split("=")
        return parts[0], parts[1]
    
    def _validate_equation(self, equation):
        if '=' not in equation:
            raise ValueError("Invalid equation: missing '=' sign")
        
        if equation.count('=') != 1:
            raise ValueError("Invalid equation: multiple '=' signs found")
        
        valid_chars_pattern = VALID_CHARS_PATTERN
        if not re.match(valid_chars_pattern, equation):
            raise ValueError("Invalid equation: contains invalid characters")
        
        left, right = equation.split('=')
        if not left or not right:
            raise ValueError("Invalid equation: empty side detected")
    
    def _validate_terms(self, left_terms, right_terms):

        if not left_terms and not right_terms:
            raise ValueError("No valid terms found in equation")
        
        all_exponents = list(left_terms.keys()) + list(right_terms.keys())
        if any(exp < 0 for exp in all_exponents):
            raise ValueError("Negative exponents not supported")
    
    def _extract_terms(self, expression):
        terms = {}
        matches = re.finditer(self.term_pattern, expression)
        
        for match in matches:
            sign = match.group(1)
            coefficient = match.group(2)
            exponent = match.group(3)
            
            coef = self._parse_coefficient(sign, coefficient)
            exp = int(exponent)
            
            terms[exp] = terms.get(exp, 0) + coef
        
        return terms
    
    def _parse_coefficient(self, sign, coefficient_str):
        coef = float(coefficient_str)
        return -coef if sign == '-' else coef
    
    def get_max_degree(self, equation_str):

        left_terms, right_terms = self.parse(equation_str)
        all_degrees = list(left_terms.keys()) + list(right_terms.keys())
        return max(all_degrees) if all_degrees else 0
    
    def get_all_degrees(self, equation_str):

        left_terms, right_terms = self.parse(equation_str)
        all_degrees = set(left_terms.keys()) | set(right_terms.keys())
        return sorted(all_degrees)
    
    def has_term(self, equation_str, degree):
        left_terms, right_terms = self.parse(equation_str)
        return degree in left_terms or degree in right_terms
    
    @staticmethod
    def reduce_equation(left: dict, right: dict) -> dict:

        #begin with left side
        coefficients = left.copy()

        for exp, coeff in right.items():
            if exp in coefficients:
                coefficients[exp] -= coeff
            else:
                coefficients[exp] = - coeff
        
        if not coefficients:
            return {0 : 0}
        
        return coefficients

