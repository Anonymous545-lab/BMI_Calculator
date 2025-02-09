import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")

        # Determine the weight category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        elif 30 <= bmi < 34.9:
            category = "Obese (Class 1)"
        elif 35 <= bmi < 39.9:
            category = "Obese (Class 2)"
        else:
            category = "Obese (Class 3)"
        
        category_label.config(text=f"Category: {category}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place the widgets
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate", command=calculate_bmi).grid(row=2, columnspan=2, pady=10)

result_label = tk.Label(root, text="BMI: ")
result_label.grid(row=3, columnspan=2, pady=10)

category_label = tk.Label(root, text="Category: ")
category_label.grid(row=4, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
