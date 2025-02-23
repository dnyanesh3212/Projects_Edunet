import tkinter as tk
from tkinter import messagebox, ttk
import os

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        return "\n".join(str(workout) for workout in self.workouts) if self.workouts else "No workouts recorded yet."

    def save_data(self, filename):
        try:
            with open(filename, "w") as file:
                for workout in self.workouts:
                    file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")
            return "Data saved successfully!"
        except Exception as e:
            return f"Error saving data: {e}"

    def load_data(self, filename):
        try:
            if not os.path.exists(filename):
                return "File not found!"
            self.workouts.clear()
            with open(filename, "r") as file:
                for line in file:
                    date, exercise_type, duration, calories_burned = line.strip().split(",")
                    self.workouts.append(Workout(date, exercise_type, int(duration), int(calories_burned)))
            return "Data loaded successfully!"
        except Exception as e:
            return f"Error loading data: {e}"

class WorkoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Tracker")
        self.root.geometry("600x500")
        self.root.config(bg="#F4F6F9")

        # User Details
        self.user_frame = tk.Frame(root, bg="white", padx=20, pady=10, relief="solid", bd=2)
        self.user_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(self.user_frame, text="Name:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.user_frame, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.user_frame, text="Age:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.user_frame, font=("Arial", 12))
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.user_frame, text="Weight (kg):", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=5, pady=5)
        self.weight_entry = tk.Entry(self.user_frame, font=("Arial", 12))
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

        self.create_user_button = tk.Button(self.user_frame, text="Create User", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                                            command=self.create_user, padx=10, pady=5)
        self.create_user_button.grid(row=3, columnspan=2, pady=10)

        # Workout Entry
        self.workout_frame = tk.Frame(root, bg="white", padx=20, pady=10, relief="solid", bd=2)
        self.workout_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(self.workout_frame, text="Date (YYYY-MM-DD):", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.workout_frame, font=("Arial", 12))
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.workout_frame, text="Exercise Type:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5, pady=5)
        self.exercise_entry = tk.Entry(self.workout_frame, font=("Arial", 12))
        self.exercise_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.workout_frame, text="Duration (min):", font=("Arial", 12), bg="white").grid(row=2, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(self.workout_frame, font=("Arial", 12))
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.workout_frame, text="Calories Burned:", font=("Arial", 12), bg="white").grid(row=3, column=0, padx=5, pady=5)
        self.calories_entry = tk.Entry(self.workout_frame, font=("Arial", 12))
        self.calories_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_workout_button = tk.Button(self.workout_frame, text="Add Workout", font=("Arial", 12, "bold"), bg="#2196F3", fg="white",
                                            command=self.add_workout, padx=10, pady=5)
        self.add_workout_button.grid(row=4, columnspan=2, pady=10)

        # View Workouts
        self.view_button = tk.Button(root, text="View Workouts", font=("Arial", 12, "bold"), bg="#FFC107", fg="white",
                                     command=self.view_workouts, padx=10, pady=5)
        self.view_button.pack(pady=10)

        # Save & Load
        self.file_entry = tk.Entry(root, font=("Arial", 12))
        self.file_entry.pack(pady=5, padx=10, fill="x")
        
        self.save_button = tk.Button(root, text="💾 Save Data", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                                     command=self.save_data, padx=10, pady=5)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text="📂 Load Data", font=("Arial", 12, "bold"), bg="#FF5722", fg="white",
                                     command=self.load_data, padx=10, pady=5)
        self.load_button.pack(pady=5)

        self.user = None

    def create_user(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        weight = self.weight_entry.get()

        if name and age and weight:
            self.user = User(name, int(age), int(weight))
            messagebox.showinfo("Success", f"User {name} created successfully!")
        else:
            messagebox.showerror("Error", "All fields must be filled!")

    def add_workout(self):
        if not self.user:
            messagebox.showerror("Error", "Create a user first!")
            return

        workout = Workout(self.date_entry.get(), self.exercise_entry.get(), self.duration_entry.get(), self.calories_entry.get())
        self.user.add_workout(workout)
        messagebox.showinfo("Success", "Workout added successfully!")

    def view_workouts(self):
        if not self.user:
            messagebox.showerror("Error", "Create a user first!")
            return
        messagebox.showinfo("Workouts", self.user.view_workouts())

    def save_data(self):
        messagebox.showinfo("Info", self.user.save_data(self.file_entry.get()))

    def load_data(self):
        messagebox.showinfo("Info", self.user.load_data(self.file_entry.get()))

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutApp(root)
    root.mainloop()
