from dreal import *  # pip3 install dreal.
x = Variable("x")

# To use dReal, we flip the inequality and verify that the slope being less
# that mu is unsatisfiable (over the finite domain).  I then found the largest
# mu that returns "none" (== unsatisfiable).  Larger values provide a witness
# that can verify satisfiability.
mu = .175
result = CheckSatisfiability(And(
    0.001 <= x, x <= 1000,
    0.5*(2*x + 6*sin(x)*cos(x))**2 <= mu*(x**2 + 3*sin(x)**2)
), 1e-6)
print(result)
