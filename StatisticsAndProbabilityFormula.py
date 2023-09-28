# Dictionary of statistics and probability formulas
formulas = {
    "Mean": "Mean = (Σx) / N",
    "Median": "For an ordered dataset, the median is the middle value (if N is odd) or the average of the two middle values (if N is even).",
    "Mode": "The mode is the value(s) that occur most frequently in a dataset.",
    "Variance": "σ^2 = Σ(x - μ)^2 / N",
    "Standard Deviation": "σ = √(Σ(x - μ)^2 / N)",
    "Probability (Event A)": "P(A) = (Number of favorable outcomes for A) / (Total number of possible outcomes)",
    "Conditional Probability": "P(A | B) = P(A ∩ B) / P(B)",
    "Binomial Probability": "P(X = k) = (n choose k) * p^k * (1 - p)^(n - k)",
    "Normal Distribution": "The probability density function of the normal distribution is given by f(x) = (1 / (σ√(2π))) * e^(-(x-μ)^2 / (2σ^2))",
    "Exponential Distribution": "The probability density function of the exponential distribution is given by f(x) = λ * e^(-λx) for x >= 0",
}

while True:
    print("Options:")
    print("1. List available formulas")
    print("2. Search for a specific formula")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "3":
        break
    elif choice == "1":
        print("\nList of Available Formulas:")
        for formula_name, formula_description in formulas.items():
            print(f"{formula_name}:\n{formula_description}\n")
    elif choice == "2":
        search_term = input("Enter the name of the formula you want to search for: ")
        formula = formulas.get(search_term, "Formula not found.")
        print(formula)
    else:
        print("Invalid input. Please enter a valid option.")
