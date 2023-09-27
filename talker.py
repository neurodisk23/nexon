import time
import socket

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
            time.sleep(0.25)
        
    except Exception as e:
        print('An error occurred while sending data:', str(e))
    
    finally:
        # Close the socket
        sock.close()

# Example usage
ip_address = '169.254.178.227'
port = 5001


message = "A,N,0,1,100,0,0,0,0,0,0\r\n"
send_data(ip_address, port, message,40)
message = "A,N,0,0,0,0,0,0,0,0,0\r\n"
send_data(ip_address, port, message,50)
