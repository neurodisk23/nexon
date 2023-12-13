import asyncio
import os
import time 





class PIDController:
    def __init__(self, Kp, Ki, Kd, rate_min, rate_max):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.rate_min = rate_min
        self.rate_max = rate_max
        self.error =  0
        self.previous_error = 0
        self.integral = 0

    def update(self, desired_position, current_position):
        self.error = desired_position - current_position
        self.integral += self.error
        derivative = self.error - self.previous_error
        output = self.Kp * self.error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = self.error

    
        rate = output

     
        rate = max(self.rate_min, min(rate, self.rate_max))

        return rate




async def send_data():
    host = '169.254.178.227'
    port = 5001
    reader, writer = await asyncio.open_connection(host, port)
    message = "A,N,0,1,100,0,0,0,0,0,0\r\n"  
    writer.write(message.encode())
    time.sleep(1)
    message = "A,D,0,1,30,0,0,0,0,0,0\r\n"
    writer.write(message.encode())
    message = "A,D,0,0,0,0,0,0,0,0,0\r\n"
    writer.write(message.encode())
    while True:
        try:
            data = await reader.read(100)
            feedback = data.decode()
            print(feedback)
            #steering_feedback = feedback.split(',')[2]
            #steering_feedback = int(steering_feedback)
            #resulting_rate = pid_controller.update(steering_position, steering_feedback)
            #current_time = time.time() - start_time
            #text = "["+str(steering_feedback)+","+str(current_time)+"],\n"
            #file.write(text)
            #file.write(f"[{steering_feedback,current_time}],\n")
            message = "A,D,10,0,0,0,0,0,0,0,0\r\n"
            writer.write(message.encode())
            # message = "A,N,0,0,0,0,0,0,0,0,0\r\n"  
            # writer.write(message.encode())
            print(f"Sent: {message}")
        except Exception as e:
            print(f"Error: {e}")

        #await asyncio.sleep(1)  # Adjust the sleep duration as needed

async def main():
    await send_data()

if __name__ == "__main__":
    asyncio.run(main())
