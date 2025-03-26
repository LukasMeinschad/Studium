import numpy as np
import matplotlib.pyplot as plt

def gauss_newton(model, jacobian, t_data, y_data, x0, max_iter=100, tol=1e-6):
    """
    Gauss-Newton method for nonlinear least squares
    Wt are my arg?
        model: function(x, t): compute the model predictions
        jacobian: function(x, t): compute the Jacob matrix
        t_data: this is just the independent variable values!
        y_data: observed dependent variable values
        x0: initial param guess
        max_iter: max no of iter
        tol: cv tol
    I return what?
        x_opt: optimized parameters
        error: final sum of squared errors
    """
    x = x0.copy()
    prev_error = np.inf
    
    for i in range(max_iter):
        # Compute residuals and Jacob
        r = y_data - model(x, t_data)
        J = jacobian(x, t_data)
        
        # Gauss-Newton update: Δx = (JᵀJ)⁻¹Jᵀr (formula from the script)
        try:
            delta_x = np.linalg.pinv(J.T @ J) @ J.T @ r
        except np.linalg.LinAlgError:
            print("Matrix inversion failed - using gradient descent")
            delta_x = 0.1 * J.T @ r  # back to simple gradient descent
            
        x += delta_x
        
        # Check cvgc
        current_error = np.sum(r**2)
        if abs(prev_error - current_error) < tol:
            break
        prev_error = current_error
    
    return x, current_error

def population_model(x, t):
    """Exponential model for population growth: x[0] * exp(x[1] * t)"""
    return x[0] * np.exp(x[1] * t)

def population_jacobian(x, t):
    """Jacobian for population model"""
    J = np.zeros((len(t), 2))
    J[:, 0] = np.exp(x[1] * t)  # df/dx1
    J[:, 1] = x[0] * t * np.exp(x[1] * t)  # df/dx2
    return J

def temperature_model(x, t):
    """Sinusoidal model: x[0]*sin(x[1]*t + x[2]) + x[3]"""
    return x[0] * np.sin(x[1] * t + x[2]) + x[3]

def temperature_jacobian(x, t):
    """Jacobian for temperature model"""
    J = np.zeros((len(t), 4))
    arg = x[1]*t + x[2]
    J[:, 0] = np.sin(arg)  # df/dx1
    J[:, 1] = x[0] * t * np.cos(arg)  # df/dx2
    J[:, 2] = x[0] * np.cos(arg)  # df/dx3
    J[:, 3] = 1.0  # df/dx4
    return J

def robust_temperature_fit(t_data, y_data):
    """Robust fitting for temperature model with good initialization"""
    # Smart initial parameter estimation (Achtung ! your alg cvgc depends on the initial para!!!! but don't ask me how we choose them like that haha)
    x4 = np.mean(y_data) 
    x1 = (np.max(y_data) - np.min(y_data))/2 
    x2 = 2*np.pi/12  
    max_temp_month = t_data[np.argmax(y_data)]
    x3 = np.pi/2 - x2*max_temp_month 
    
    initial_guess = np.array([x1, x2, x3, x4])
    
    # Run optimization with parameter constraints
    bounds = [(0, None), (0, 1), (-2*np.pi, 2*np.pi), (None, None)]
    x_opt, error = constrained_gauss_newton(
        temperature_model,
        temperature_jacobian,
        t_data,
        y_data,
        initial_guess,
        bounds=bounds
    )
    
    return x_opt, error

def constrained_gauss_newton(model, jacobian, t_data, y_data, x0, bounds=None, max_iter=100, tol=1e-6):
    """
    Gauss-Newton with simple parameter constraints
    """
    x = x0.copy()
    
    for i in range(max_iter):
        # Compute residuals and Jacob
        r = y_data - model(x, t_data)
        J = jacobian(x, t_data)
        
        try:
            # Gauss-Newton update
            delta_x = np.linalg.pinv(J.T @ J) @ J.T @ r
        except np.linalg.LinAlgError:
            # back to gradient descent if matrix is sing
            delta_x = 0.1 * J.T @ r
            
        # Apply constraints after update
        x_new = x + delta_x
        if bounds:
            for j in range(len(x)):
                if bounds[j][0] is not None:
                    x_new[j] = max(bounds[j][0], x_new[j])
                if bounds[j][1] is not None:
                    x_new[j] = min(bounds[j][1], x_new[j])
        
        # Check cvgc
        new_error = np.sum((y_data - model(x_new, t_data))**2)
        if abs(np.sum((x_new - x)**2)) < tol:
            break
            
        x = x_new
    
    return x, new_error

def plot_results(t_data, y_data, model, params, title):
    """Plot data and fitted model"""
    plt.figure(figsize=(10, 6))
    plt.scatter(t_data, y_data, color='red', label='Data')
    
    t_fine = np.linspace(min(t_data), max(t_data), 100)
    y_fit = model(params, t_fine)
    plt.plot(t_fine, y_fit, 'b-', label='Fitted model')
    
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Load data
    temperature_data = np.genfromtxt("temperature.csv", delimiter=',')
    population_data = np.genfromtxt("population.csv", delimiter=',')
    
    # data
    t_temp = temperature_data[:, 0]
    y_temp = temperature_data[:, 1]
    t_pop = population_data[:, 0] - population_data[0, 0]  # Normalize the time
    y_pop = population_data[:, 1]
    
    # Fit population model
    pop_params, pop_error = gauss_newton(
        population_model, population_jacobian, 
        t_pop, y_pop, 
        x0=np.array([8.0, 0.02]) # choice of initial param for the population
    )
    print("\nPopulation Model Results:")
    print(f"Parameters: x1 = {pop_params[0]:.4f}, x2 = {pop_params[1]:.4f}")
    print(f"Final SSE: {pop_error:.4f}")
    plot_results(t_pop, y_pop, population_model, pop_params, "Population Growth Model")
    
    # Fit temperature model
    temp_params, temp_error = robust_temperature_fit(t_temp, y_temp)
    print("\nTemperature Model Results:")
    print(f"Parameters: A = {temp_params[0]:.4f}, ω = {temp_params[1]:.4f}")
    print(f"φ = {temp_params[2]:.4f}, D = {temp_params[3]:.4f}")
    print(f"Final SSE: {temp_error:.4f}")
    plot_results(t_temp, y_temp, temperature_model, temp_params, "Temperature Variation Model")

if __name__ == "__main__":
    main()
