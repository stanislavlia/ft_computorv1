from expression_parser import ExpressionParser
from solver import Solver, ComplexNumber


def unit_test_parser():
    """Unit tests for ExpressionParser class"""
    
    parser = ExpressionParser()
    
    # Test 1: Basic quadratic equation
    def test_basic_quadratic():
        equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
        left, right = parser.parse(equation)
        assert left == {0: 5.0, 1: 4.0, 2: -9.3}
        assert right == {0: 1.0}
        return "✓ Test 1: Basic quadratic"
    
    # Test 2: Linear equation
    def test_linear_equation():
        equation = "5 * X^0 + 4 * X^1 = 4 * X^0"
        left, right = parser.parse(equation)
        assert left == {0: 5.0, 1: 4.0}
        assert right == {0: 4.0}
        return "✓ Test 2: Linear equation"
    
    # Test 3: Cubic equation
    def test_cubic_equation():
        equation = "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
        left, right = parser.parse(equation)
        assert left == {0: 8.0, 1: -6.0, 2: 0.0, 3: -5.6}
        assert right == {0: 3.0}
        return "✓ Test 3: Cubic equation"
    
    # Test 4: Equal terms on both sides
    def test_equal_terms():
        equation = "6 * X^0 = 6 * X^0"
        left, right = parser.parse(equation)
        assert left == {0: 6.0}
        assert right == {0: 6.0}
        return "✓ Test 4: Equal terms"
    
    # Test 5: Contradiction equation
    def test_contradiction():
        equation = "10 * X^0 = 15 * X^0"
        left, right = parser.parse(equation)
        assert left == {0: 10.0}
        assert right == {0: 15.0}
        return "✓ Test 5: Contradiction"
    
    # Test 6: Complex solution equation
    def test_complex_solution():
        equation = "1 * X^0 + 2 * X^1 + 5 * X^2 = 0 * X^0"
        left, right = parser.parse(equation)
        assert left == {0: 1.0, 1: 2.0, 2: 5.0}
        assert right == {0: 0.0}
        return "✓ Test 6: Complex solution equation"
    
    # Test 7: Multiple terms with same degree (should combine)
    def test_combining_like_terms():
        equation = "2 * X^1 + 3 * X^1 = 5 * X^0"
        left, right = parser.parse(equation)
        assert left == {1: 5.0}  # 2 + 3 = 5
        assert right == {0: 5.0}
        return "✓ Test 7: Combining like terms"
    
    # Test 8: Negative coefficients
    def test_negative_coefficients():
        equation = "-5 * X^0 - 3 * X^1 = -2 * X^0"
        left, right = parser.parse(equation)
        assert left == {0: -5.0, 1: -3.0}
        assert right == {0: -2.0}
        return "✓ Test 8: Negative coefficients"
    
    # Test 9: Missing equals sign (should raise error)
    def test_missing_equals():
        equation = "5 * X^0 + 4 * X^1"
        try:
            parser.parse(equation)
            return "✗ Test 9: Should have raised ValueError"
        except ValueError as e:
            assert "missing '=' sign" in str(e)
            return "✓ Test 9: Missing equals sign error"
    
    # Test 10: Multiple equals signs (should raise error)
    def test_multiple_equals():
        equation = "5 * X^0 = 4 * X^1 = 2 * X^0"
        try:
            parser.parse(equation)
            return "✗ Test 10: Should have raised ValueError"
        except ValueError as e:
            assert "multiple '=' signs" in str(e)
            return "✓ Test 10: Multiple equals signs error"
    
    # Test 11: Utility method - get_max_degree
    def test_get_max_degree():
        equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
        max_degree = parser.get_max_degree(equation)
        assert max_degree == 2
        return "✓ Test 11: get_max_degree utility"
    
    # Test 12: Utility method - get_all_degrees
    def test_get_all_degrees():
        equation = "5 * X^0 + 4 * X^2 + 2 * X^3 = 1 * X^1"
        degrees = parser.get_all_degrees(equation)
        assert degrees == [0, 1, 2, 3]
        return "✓ Test 12: get_all_degrees utility"
    
    # Test 13: Utility method - has_term
    def test_has_term():
        equation = "5 * X^0 + 4 * X^2 = 1 * X^0"
        assert parser.has_term(equation, 2) == True
        assert parser.has_term(equation, 1) == False
        return "✓ Test 13: has_term utility"
    
    # Test 14: Decimal coefficients
    def test_decimal_coefficients():
        equation = "3.14 * X^0 + 2.71 * X^1 = 1.41 * X^2"
        left, right = parser.parse(equation)
        assert left == {0: 3.14, 1: 2.71}
        assert right == {2: 1.41}
        return "✓ Test 14: Decimal coefficients"
    
    # Run all tests
    tests = [
        test_basic_quadratic,
        test_linear_equation,
        test_cubic_equation,
        test_equal_terms,
        test_contradiction,
        test_complex_solution,
        test_combining_like_terms,
        test_negative_coefficients,
        test_missing_equals,
        test_multiple_equals,
        test_get_max_degree,
        test_get_all_degrees,
        test_has_term,
        test_decimal_coefficients,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except AssertionError as e:
            results.append(f"✗ {test.__name__}: {e}")
        except Exception as e:
            results.append(f"✗ {test.__name__}: Unexpected error: {e}")
    
    # Print results
    for result in results:
        print(result)
    
    # Summary
    passed = sum(1 for r in results if r.startswith("✓"))
    total = len(results)
    print(f"\n{'='*50}")
    print(f"Tests passed: {passed}/{total}")
    print(f"{'='*50}")
    
    return passed == total


def test_solver():
    """Test the Solver class with various polynomial equations"""
    
    print("="*60)
    print("TESTING SOLVER CLASS")
    print("="*60)
    
    # Test 1: Quadratic with positive discriminant (2 real solutions)
    def test_quadratic_positive_discriminant():
        print("\nTest 1: Quadratic with positive discriminant")
        print("Equation: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0")
        reduced = {0: 4.0, 1: 4.0, 2: -9.3}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "positive", f"Expected 'positive', got {solution_type}"
        assert discriminant > 0, f"Discriminant should be positive: {discriminant}"
        assert len(solutions) == 2, f"Should have 2 solutions, got {len(solutions)}"
        print(f"  Discriminant: {discriminant}")
        print(f"  Solutions: {solutions[0]}, {solutions[1]}")
        print("  ✓ Passed")
    
    # Test 2: Quadratic with zero discriminant (1 real solution)
    def test_quadratic_zero_discriminant():
        print("\nTest 2: Quadratic with zero discriminant")
        print("Equation: 1 * X^0 - 2 * X^1 + 1 * X^2 = 0")
        # (x - 1)^2 = 0, solution: x = 1
        reduced = {0: 1.0, 1: -2.0, 2: 1.0}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "zero", f"Expected 'zero', got {solution_type}"
        assert abs(discriminant) < 1e-10, f"Discriminant should be zero: {discriminant}"
        assert len(solutions) == 1, f"Should have 1 solution, got {len(solutions)}"
        assert abs(solutions[0] - 1.0) < 1e-6, f"Solution should be 1.0, got {solutions[0]}"
        print(f"  Discriminant: {discriminant}")
        print(f"  Solution: {solutions[0]}")
        print("  ✓ Passed")
    
    # Test 3: Quadratic with negative discriminant (complex solutions)
    def test_quadratic_negative_discriminant():
        print("\nTest 3: Quadratic with negative discriminant")
        print("Equation: 1 * X^0 + 2 * X^1 + 5 * X^2 = 0")
        reduced = {0: 1.0, 1: 2.0, 2: 5.0}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "negative", f"Expected 'negative', got {solution_type}"
        assert discriminant < 0, f"Discriminant should be negative: {discriminant}"
        assert len(solutions) == 2, f"Should have 2 solutions, got {len(solutions)}"
        assert isinstance(solutions[0], ComplexNumber), "Solutions should be ComplexNumber objects"
        print(f"  Discriminant: {discriminant}")
        print(f"  Solutions: {solutions[0]}, {solutions[1]}")
        print("  ✓ Passed")
    
    # Test 4: Linear equation (degree 1)
    def test_linear_equation():
        print("\nTest 4: Linear equation")
        print("Equation: 1 * X^0 + 4 * X^1 = 0")
        reduced = {0: 1.0, 1: 4.0}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "linear", f"Expected 'linear', got {solution_type}"
        assert len(solutions) == 1, f"Should have 1 solution, got {len(solutions)}"
        assert abs(solutions[0] - (-0.25)) < 1e-6, f"Solution should be -0.25, got {solutions[0]}"
        print(f"  Solution: {solutions[0]}")
        print("  ✓ Passed")
    
    # Test 5: Constant equation - infinite solutions (0 = 0)
    def test_infinite_solutions():
        print("\nTest 5: Constant equation - infinite solutions")
        print("Equation: 0 * X^0 = 0")
        reduced = {0: 0.0}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "infinite", f"Expected 'infinite', got {solution_type}"
        assert len(solutions) == 0, f"Should have no specific solutions"
        print("  Any real number is a solution")
        print("  ✓ Passed")
    
    # Test 6: Constant equation - no solution (5 = 0)
    def test_no_solution():
        print("\nTest 6: Constant equation - no solution")
        print("Equation: -5 * X^0 = 0")
        reduced = {0: -5.0}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "none", f"Expected 'none', got {solution_type}"
        assert len(solutions) == 0, f"Should have no solutions"
        print("  No solution")
        print("  ✓ Passed")
    
    # Test 7: Cubic equation (degree > 2, unsolvable)
    def test_cubic_unsolvable():
        print("\nTest 7: Cubic equation (unsolvable)")
        print("Equation: 5 * X^0 - 6 * X^1 - 5.6 * X^3 = 0")
        reduced = {0: 5.0, 1: -6.0, 3: -5.6}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "unsolvable", f"Expected 'unsolvable', got {solution_type}"
        assert len(solutions) == 0, f"Should have no solutions"
        print("  Degree > 2, cannot solve")
        print("  ✓ Passed")
    
    # Test 8: Simple quadratic (x^2 - 4 = 0, solutions: x = ±2)
    def test_simple_quadratic():
        print("\nTest 8: Simple quadratic")
        print("Equation: -4 * X^0 + 0 * X^1 + 1 * X^2 = 0")
        reduced = {0: -4.0, 1: 0.0, 2: 1.0}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "positive", f"Expected 'positive', got {solution_type}"
        assert len(solutions) == 2, f"Should have 2 solutions"
        # Solutions should be 2 and -2
        solutions_sorted = sorted(solutions)
        assert abs(solutions_sorted[0] - (-2.0)) < 1e-6, f"Expected -2.0, got {solutions_sorted[0]}"
        assert abs(solutions_sorted[1] - 2.0) < 1e-6, f"Expected 2.0, got {solutions_sorted[1]}"
        print(f"  Solutions: {solutions[0]}, {solutions[1]}")
        print("  ✓ Passed")
    
    # Test 9: Quadratic with fractional coefficients
    def test_fractional_coefficients():
        print("\nTest 9: Quadratic with fractional coefficients")
        print("Equation: 0.5 * X^0 + 1.5 * X^1 + 2.5 * X^2 = 0")
        reduced = {0: 0.5, 1: 1.5, 2: 2.5}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        # Discriminant = 1.5^2 - 4*2.5*0.5 = 2.25 - 5 = -2.75 (negative)
        assert solution_type == "negative", f"Expected 'negative', got {solution_type}"
        assert discriminant < 0, f"Discriminant should be negative"
        assert len(solutions) == 2, f"Should have 2 complex solutions"
        print(f"  Discriminant: {discriminant}")
        print(f"  Complex solutions: {solutions[0]}, {solutions[1]}")
        print("  ✓ Passed")
    
    # Test 10: Linear with negative solution
    def test_linear_negative_solution():
        print("\nTest 10: Linear with negative solution")
        print("Equation: 10 * X^0 + 2 * X^1 = 0")
        reduced = {0: 10.0, 1: 2.0}
        solver = Solver(reduced)
        solution_type, discriminant, solutions = solver.solve()
        
        assert solution_type == "linear", f"Expected 'linear', got {solution_type}"
        assert len(solutions) == 1, f"Should have 1 solution"
        assert abs(solutions[0] - (-5.0)) < 1e-6, f"Solution should be -5.0, got {solutions[0]}"
        print(f"  Solution: {solutions[0]}")
        print("  ✓ Passed")
    
    # Run all tests
    tests = [
        test_quadratic_positive_discriminant,
        test_quadratic_zero_discriminant,
        test_quadratic_negative_discriminant,
        test_linear_equation,
        test_infinite_solutions,
        test_no_solution,
        test_cubic_unsolvable,
        test_simple_quadratic,
        test_fractional_coefficients,
        test_linear_negative_solution,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            failed += 1
    
    # Summary
    print("\n" + "="*60)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("="*60)
    
    return passed == len(tests)


if __name__ == "__main__":
    all_passed = unit_test_parser()

    if all_passed:
        print("=============PARSER PASSED!==============\n\n")

    all_passed_solver = test_solver()

    if all_passed_solver:
        print("=============SOLVER PASSED!==============")