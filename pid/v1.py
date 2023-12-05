class PIDController:
    def __init__(self, Kp, Ki, Kd, q_min, q_max):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.q_min = q_min
        self.q_max = q_max
        self.error = 0
        self.previous_error = 0
        self.integral = 0

    def update(self, h, p, r):
        self.error = h - p
        self.integral += self.error
        derivative = self.error - self.previous_error
        output = self.Kp * self.error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = self.error

        # Apply output to the system (quantity q)
        q = output + r

        # Clamp output to acceptable bounds
        q = max(self.q_min, min(q, self.q_max))

        return q

# Example usage:
# Set your desired gains and constraints
Kp = 0.1
Ki = 0.01
Kd = 0.05
q_min = -340
q_max = 340

pid_controller = PIDController(Kp, Ki, Kd, q_min, q_max)

# Update the controller with desired position (h), current position (p), and rate (r)
desired_position = 0  # Set your desired position
current_position = 10  # Set your initial position
rate = 5  # Set your initial rate

resulting_quantity = pid_controller.update(desired_position, current_position, rate)
print("Resulting Quantity:", resulting_quantity)
