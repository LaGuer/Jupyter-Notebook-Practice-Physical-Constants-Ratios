import numpy as np
from math import log, pi as π
from numpy import euler_gamma as γ

def calculate_constants(start, end, factor):
    Ч = sum(
        factor**-j * (1 - ((j + 1/j) * np.log(j) - j + 1/j)) / np.log(factor**(324*γ))
        for j in range(start, end)
    ) / 2

    Ж = π * Ч / γ
    α = 1 / Ж

    return α, Ж, Ч

# Define parameters for variation
parameters = [
    {"start": 1, "end": 100, "factor": 2},
    {"start": 1, "end": 200, "factor": 3},
    {"start": 50, "end": 150, "factor": 1.5},
]

# Run the calculations for each set of parameters
for param in parameters:
    α, Ж, Ч = calculate_constants(param["start"], param["end"], param["factor"])
    print(f"For start={param['start']}, end={param['end']}, factor={param['factor']}:")
    print(f"α (alpha) = {α}")
    print(f"Ж = {Ж}")
    print(f"Ч = {Ч}")
    print("-" * 30)

print("γ (Euler-Mascheroni constant) =", γ)
