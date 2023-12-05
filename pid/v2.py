class PIDController:
    def __init__(self, Kp, Ki, Kd, rate_min, rate_max):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.rate_min = rate_min
        self.rate_max = rate_max
        self.error = 0
        self.previous_error = 0
        self.integral = 0

    def update(self, desired_position, current_position):
        self.error = desired_position - current_position
        self.integral += self.error
        derivative = self.error - self.previous_error
        output = self.Kp * self.error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = self.error

        # Apply output to the system (steering rate)
        rate = output

        # Clamp output to acceptable bounds
        rate = max(self.rate_min, min(rate, self.rate_max))

        return rate

# Example usage:
# Set your desired gains and constraints
Kp = 0.1
Ki = 0.01
Kd = 0.05
rate_min = -100
rate_max = 100

pid_controller = PIDController(Kp, Ki, Kd, rate_min, rate_max)

# Update the controller with desired position and current position
desired_steering_position = 0  # Set your desired steering position
current_steering_position = 10  # Set your initial steering position

resulting_rate = pid_controller.update(desired_steering_position, current_steering_position)
print("Resulting Steering Rate:", resulting_rate)
