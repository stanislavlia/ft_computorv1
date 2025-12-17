from expression_parser import ExpressionParser

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


if __name__ == "__main__":
    all_passed = unit_test_parser()
