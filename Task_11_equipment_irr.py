#Estimate the IRR of a small equipment investment."""
import numpy as np
from scipy.optimize import newton, root_scalar

cash_flows = np.array([-10000, 3000, 3500, 4000, 2500], dtype=float)

def npv(rate):
    if rate <= -1:
        return np.inf
    periods = np.arange(len(cash_flows))
    return np.sum(cash_flows / (1 + rate) ** periods)

def npv_derivative(rate):
    periods = np.arange(1, len(cash_flows))
    return np.sum(-periods * cash_flows[1:] / (1 + rate) ** (periods + 1))

newton_guess = 0.15  # changed from 0.10
irr_newton = newton(npv, newton_guess, fprime=npv_derivative, maxiter=100)
secant_result = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)

print(f"IRR (Newton-Raphson): {irr_newton:.6%}")
print(f"IRR (Secant): {secant_result.root:.6%}")
print(f"NPV at Newton solution: {npv(irr_newton):.8f}")
print("IRR is the rate at which the modeled NPV equals zero.")