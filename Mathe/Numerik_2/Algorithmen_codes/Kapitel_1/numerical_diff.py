import numpy as np


def forward_differences(f,x,h=1e-5):
    """
    Implementation of forward differences
    """
    return (f(x+h) - f(x)) / h

def backward_differences(f,x,h=1e-5):
    """
    Implementation of backward differences
    """
    return (f(x) - f(x-h)) / h

def central_differences(f,x,h=1e-5):
    """
    Implementation of central differences
    """
    return (f(x+h) - f(x-h)) / (2*h)

def f(x):
    return np.sin(x)

x = np.pi/4

fd = forward_differences(f,x)
bd = backward_differences(f,x)
cd = central_differences(f,x)

true_derivative = np.cos(x)

print(f"Function: sin(x), evaluating at x = {x:.4f}")
print(f"Forward difference:  {fd:.6f} (Error: {abs(fd - true_derivative):.2e})")
print(f"Backward difference: {bd:.6f} (Error: {abs(bd - true_derivative):.2e})")
print(f"Central difference:  {cd:.6f} (Error: {abs(cd - true_derivative):.2e})")
print(f"True derivative:     {true_derivative:.6f}")
