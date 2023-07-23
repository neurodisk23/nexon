import socket
import time

def send_data(ip_address, port, message,mode_delay):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the IP address and port
        sock.connect((ip_address, port))
        token  = 0
        while token < 25*mode_delay:
            # Send the message
            data = sock.send(message.encode())
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
send_data(ip_address, port, message,1)

message = "A,N,0,1,50,0,0,0,0,0,0\r\n"

send_data(ip_address, port, message,1)

message = "A,D,0,1,50,0,0,0,0,0,0\r\n"

send_data(ip_address, port, message,1)

send_data(ip_address, port, message,1)

message = "A,D,10,0,0,0,0,0,0,0,0\r\n"

send_data(ip_address, port, message,2)
message = "A,D,40,0,0,0,0,0,0,0,0\r\n"

send_data(ip_address, port, message,3)
message = "A,N,0,0,50,0,0,0,0,0,0\r\n"

send_data(ip_address, port, message,3)
message = "A,N,0,0,0,0,0,0,0,0,0\r\n"

send_data(ip_address, port, message,4)
