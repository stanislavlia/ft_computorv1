
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

    def solve(self) -> tuple:
        pass

    def solve_degree_2(self):
        a = self.reduced_equation.get(key=2, default=0)
        b = self.reduced_equation.get(key=1, default=0)
        c = self.reduced_equation.get(key=0, default=0)

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
            sqrt_abs_d = abs(discriminant)
            img_part = sqrt_abs_d / ( 2 * a)

            x1 = ComplexNumber(real_part, img_part)
            x2 = ComplexNumber(real_part, -img_part)
            return ("negative", discriminant, [x1, x2])


    def solve_degree_1(self):
        pass

    def solve_degree_0(self):
        pass

    def solve_higher_degree(self):
        pass