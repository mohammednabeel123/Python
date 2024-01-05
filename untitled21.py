class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.steps = 0
        self.calories_burned = 0

    def log_steps(self, num_steps):
        self.steps += num_steps
        print(f"Logged {num_steps} steps for {self.user_name}.")

    def log_calories_burned(self, calories):
        self.calories_burned += calories
        print(f"Logged {calories} calories burned for {self.user_name}.")

    def display_summary(self):
        print(f"Fitness Summary for {self.user_name}:")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories_burned}")

# Example Usage:
user1 = FitnessTracker("Alice")
user2 = FitnessTracker("Bob")

user1.log_steps(5000)
user2.log_calories_burned(200)

user1.display_summary()
user2.display_summary()
