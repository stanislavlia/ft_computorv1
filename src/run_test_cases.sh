#!/bin/bash

# test.sh - Test script for computor polynomial solver

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
BLUE='\033[0;34m'
CYAN='\033[0;36m'

TOTAL=0

# Function to run a test case
run_test() {
    local test_num=$1
    local equation=$2
    local expected=$3
    
    TOTAL=$((TOTAL + 1))
    
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}Test $test_num${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Equation:${NC} $equation"
    echo ""
    
    # Run the program and capture output
    actual=$(python3 ./main.py "$equation" 2>&1)
    
    echo -e "${GREEN}Expected Output:${NC}"
    echo "$expected"
    echo ""
    echo -e "${YELLOW}Actual Output:${NC}"
    echo "$actual"
    echo ""
}

clear
echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║              COMPUTOR V1 - TEST SUITE                        ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Test 1: Quadratic with positive discriminant
run_test 1 \
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" \
"Reduced form: 4.0 * X^0 + 4.0 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131"

# Test 2: Linear equation
run_test 2 \
    "5 * X^0 + 4 * X^1 = 4 * X^0" \
"Reduced form: 1.0 * X^0 + 4.0 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25"

# Test 3: Cubic equation (unsolvable)
run_test 3 \
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0" \
"Reduced form: 5.0 * X^0 - 6.0 * X^1 + 0.0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is strictly greater than 2, I can't solve."

# Test 4: Infinite solutions
run_test 4 \
    "6 * X^0 = 6 * X^0" \
"Reduced form: 0.0 * X^0 = 0
Polynomial degree: 0
Any real number is a solution."

# Test 5: No solution
run_test 5 \
    "10 * X^0 = 15 * X^0" \
"Reduced form: -5.0 * X^0 = 0
Polynomial degree: 0
No solution."

# Test 6: Complex solutions
run_test 6 \
    "1 * X^0 + 2 * X^1 + 5 * X^2 = 0 * X^0" \
"Reduced form: 1.0 * X^0 + 2.0 * X^1 + 5.0 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly negative, the two complex solutions are:
-0.2 + 0.4i
-0.2 - 0.4i"

# Test 7: Zero discriminant
run_test 7 \
    "1 * X^0 - 2 * X^1 + 1 * X^2 = 0 * X^0" \
"Reduced form: 1.0 * X^0 - 2.0 * X^1 + 1.0 * X^2 = 0
Polynomial degree: 2
The solution is:
1.0"

# Test 8: Simple quadratic (x^2 - 4 = 0)
run_test 8 \
    "0 * X^0 + 0 * X^1 + 1 * X^2 = 4 * X^0" \
"Reduced form: -4.0 * X^0 + 1.0 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
2.0
-2.0"

# Test 9: Invalid format (should fail)
run_test 9 \
    "5 * X = 0" \
"Error: Invalid equation: no valid terms found"

# Test 10: Missing equals sign (should fail)
run_test 10 \
    "5 * X^0 + 4 * X^1" \
"Error: Invalid equation: missing '=' sign"

# Summary
echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                    TESTS COMPLETED                           ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo -e "Total tests run: ${CYAN}$TOTAL${NC}"
echo ""