import socket

def main():
    server_ip = "192.168.29.103"   
    server_port = 12345 

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect((server_ip, server_port))
    
    while True:
        message = input("Enter a message to send to the server: ")
        c_socket.send(message.encode("utf-8"))

        data = c_socket.recv(1024).decode("utf-8")
        print(f"Received from server: {data}")
        
        if message.lower() == "exit":
            break
    
    c_socket.close()

if __name__ == "__main__":
    main()
