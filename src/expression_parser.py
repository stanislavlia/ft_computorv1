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
        """
        Extract terms and validate that entire expression matches pattern.
        Raises ValueError if expression contains invalid format.
        """
        if not expression:
            raise ValueError("Invalid equation: empty expression")
        
        matches = list(re.finditer(self.term_pattern, expression))
        
        # Check if any valid terms were found
        if not matches:
            raise ValueError(f"Invalid equation: no valid terms found in '{expression}'")
        
        # Validate by reconstructing the expression from matches
        reconstructed = ""
        for i, match in enumerate(matches):
            sign = match.group(1)
            # First term shouldn't have explicit + sign in reconstruction
            if i == 0 and sign == '+':
                sign = ''
            elif i > 0 and sign == '':
                sign = '+'  # Add + between terms if not present
            reconstructed += sign + match.group(2) + "*X^" + match.group(3)
        
        # Remove leading + for comparison
        expr_clean = expression[1:] if expression.startswith('+') else expression
        recon_clean = reconstructed[1:] if reconstructed.startswith('+') else reconstructed
        
        if expr_clean != recon_clean:
            raise ValueError(f"Invalid equation format: expression contains invalid terms")
        
        # Extract coefficients and exponents
        terms = {}
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
        # Begin with left side
        coefficients = left.copy()
        
        for exp, coeff in right.items():
            if exp in coefficients:
                coefficients[exp] -= coeff
            else:
                coefficients[exp] = -coeff
        
        # Remove near-zero coefficients
        coefficients = {
            exp: coeff for exp, coeff in coefficients.items()
            if abs(coeff) > 1e-10
        }
        
        if not coefficients:
            return {0: 0}
        
        return coefficients