
def abs(x):
    if x > 0:
        return x
    return -x


def sqrt(x, precision=1e-10):
    if x < 0:
        raise ValueError("Cannot calculate sqrt of negative number")
    if x == 0:
        return 0
    
    #initial guess of sqrt(x)
    x_sqrt = x / 2

    while True:
        x_new = (x_sqrt + x / x_sqrt) / 2
        if abs(x_new - x_sqrt) < precision:
            return x_new

        x_sqrt = x_new


class ComplexNumber:
    """Simple complex number"""
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        """Format as: a + bi or a - bi"""
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"
        


class Solver():
    def __init__(self, reduced_equation: dict):
        
        self.reduced_equation = reduced_equation

    def _get_poly_degree(self, reduced_equation: dict):
        
        if not reduced_equation:
            return 0
        
        non_zero_degrees = []
        for degree, coeff in reduced_equation.items():
            if coeff:
                non_zero_degrees.append(degree)

        if not non_zero_degrees:
            return 0
        return max(non_zero_degrees)

    def solve(self) -> tuple:
        "General solver"
        
        poly_degree = self._get_poly_degree(self.reduced_equation)

        if poly_degree == 0:
            return self._solve_degree_0()
        if poly_degree == 1:
            return self._solve_degree_1()
        if poly_degree == 2:
            return self.solve_degree_2()

        return self._solve_higher_degree()

    def solve_degree_2(self):
        "Solve quadratic equation"
        a = self.reduced_equation.get(2, 0)
        b = self.reduced_equation.get(1, 0)
        c = self.reduced_equation.get(0, 0)
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            #two solutions in R
            sqrt_d = sqrt(discriminant)
            x1 = (-b + sqrt_d) / (2 * a)
            x2 = (-b - sqrt_d) / (2 * a)
            return ("positive", discriminant, [x1, x2])
        elif discriminant == 0:
            #one solution in R
            x1 = -b / (2 * a)
            return ("zero", discriminant, [x1])
        else:
            #solution only in Complex Numbers
            real_part = -b / (2 * a)
            sqrt_abs_d = sqrt(abs(discriminant))
            img_part = sqrt_abs_d / ( 2 * a)
            x1 = ComplexNumber(real_part, img_part)
            x2 = ComplexNumber(real_part, -img_part)
            return ("negative", discriminant, [x1, x2])


    def _solve_degree_1(self):
        """Solve linear equation"""
        b = self.reduced_equation.get(1, 0)
        c = self.reduced_equation.get(0, 0)
        x = -c / b
        return ('linear', None, [x])
    
    def _solve_degree_0(self):
        """Solve constant equation"""
        c = self.reduced_equation.get(0, 0)
        if abs(c) < 1e-10:
            return ('infinite', None, [])
        else:
            return ('none', None, [])
    
    def _solve_higher_degree(self):
        """Degree > 2"""
        return ('unsolvable', None, [])