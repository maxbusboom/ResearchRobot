import sympy as sp

# Define symbols
T, theta = sp.symbols('T theta')
m = 17  # mass in kg
g_val = 9.81  # acceleration due to gravity in m/s^2

# Total vertical force balance: 2T * sin(theta) = mg
lhs = 2 * T * sp.sin(theta)
rhs = m * g_val

# Solve for T
tension_expr = sp.solve(lhs - rhs, T)[0]

# Substitute theta = 22 degrees (convert to radians)
theta_val = 22 * sp.pi / 180
tension_numeric = tension_expr.subs(theta, theta_val).evalf()

print("Symbolic tension expression:")
print(tension_expr)

print("\nNumeric tension value (in Newtons):")
print(tension_numeric)