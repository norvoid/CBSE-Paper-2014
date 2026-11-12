import sympy as sp

# Define the variable x
x = sp.symbols('x')

# Define the matrices
row_vector = sp.Matrix([[x, 1]])
matrix_b = sp.Matrix([[1, 0], [-2, 0]])
zero_matrix = sp.Matrix([[0, 0]])

# Perform matrix multiplication: (x 1) * [[1, 0], [-2, 0]]
product = row_vector * matrix_b
print('Matrix Product Expression:', product)

# Solve the matrix equation product = zero matrix
equation = sp.Eq(product, zero_matrix)
solution = sp.solve(equation, x)
print('Solved value(s) for x:', solution)

# Verification by substitution
verified_product = product.subs(x, 2)
print('Product when x = 2:', verified_product)
