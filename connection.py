import socket
import time

def send_data(ip_address, port, message):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the IP address and port
        sock.connect((ip_address, port))
        token  = 0
        while token < 25:
            # Send the message
            data = sock.send(message.encode())
            print(data)
            token += data 
            
            # Delay for 1 second
            time.sleep(1)
        
    except Exception as e:
        print('An error occurred while sending data:', str(e))
    
    finally:
        # Close the socket
        sock.close()

# Example usage
ip_address = '169.254.178.227'
port = 5001
message = "A1,N,0,0,0,0,0,0,0,0,0\r\n"

# Call the send_data function
send_data(ip_address, port, message)

message = "A,N,0,1,50,0,0,0,0,0,0\r\n"

# Call the send_data function
send_data(ip_address, port, message)
