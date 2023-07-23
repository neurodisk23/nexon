import socket

def read_data(ip_address, port, buffer_size=1024):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the IP address and port
        sock.connect((ip_address, port))

        while True:
            # Receive data from the socket
            data = sock.recv(buffer_size)
            
            # Check if the connection is closed
            if not data:
                print("Connection closed by the server.")
                break
            
            # Process the received data (you can replace this with your desired processing logic)
            data_read = data.decode()
            print("Received:", data_read)
            break 

    except Exception as e:
        print('An error occurred while reading data:', str(e))
    
    finally:
        # Close the socket
        sock.close()

    return data_read
ip_address = '169.254.178.227'
port = 5001

dat = read_data(ip_address,port)

steering = dat.split(',')[2]
brake = dat.split(',')[1]
mode = dat.split(',')[4]
