import numpy as np
import matplotlib.pyplot as plt

N1, N2 = 10, 100
A, B = 0, 2
h1 = (B - A) / N1
h2 = (B - A) / N2

x1 = np.arange(A, B+h1, h1)
x2 = np.arange(A, B+h2, h2)
def function(x: int | float) -> int | float:
    return x**4 - 2*x + 1

start_value = function(A)
end_value = function(B)
trapezoid1 = h1 * (start_value/2 + end_value/2 + np.sum(function(x1[1:-1])))
trapezoid2 = h2 * (start_value/2 + end_value/2 + np.sum(function(x2[1:-1])))

simpson1 = h1 / 3 * (
        function(A) + 
        function(B) + 
        4 * np.sum(function(x1[1:-1:2])) +
        2 * np.sum(function(x1[2:-1:2]))
        )
simpson2 = h2 / 3 * (
        function(A) + 
        function(B) + 
        4 * np.sum(function(x2[1:-1:2])) + 
        2 * np.sum(function(x2[2:-1:2]))
        )

print(trapezoid1, trapezoid2)
print(simpson1, simpson2)
