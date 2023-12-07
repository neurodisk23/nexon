import asyncio

async def send_data():
    host = '169.254.178.227'
    port = 5001
    message = "A4,N,0,0,0,1,100,0,0,0,0\r\n"
    steering_rate = 100
    steering_position = 0
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        try:
            data = await reader.read(100)
            feedback = data.decode()
            steering_feedback = feedback.split(',')[2]

            if int(steering_feedback) > steering_position :
                message = "A4,N,0,0,0,1,-50,0,0,0,0\r\n"
                writer.write(message.encode())
                #print(f"Sent: {message}")

            elif int(steering_feedback) <= steering_position :
                message = "A4,N,0,0,0,1,50,0,0,0,0\r\n"
                writer.write(message.encode())
                #print(f"Sent: {message}")


    





            


            print("\nSteering Value : ", steering_feedback)

            #writer.close()
            #await writer.wait_closed()

        except Exception as e:
            print(f"Error: {e}")

        #await asyncio.sleep(1)  # Adjust the sleep duration as needed

async def main():
    await send_data()

if __name__ == "__main__":
    asyncio.run(main())
