import socket

def main():
    server_ip = "0.0.0.0" 
    server_port = 12345  

    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind((server_ip, server_port))
    s_socket.listen(1)
    
    print(f"Server listening on {server_ip}:{server_port}")
    
    c_socket, client_address = s_socket.accept()
    print(f"Connection from: {client_address}")
    
    while True:
        data = c_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print(f"Received from client: {data}")
        
        response = input("Enter a message to send to the client: ")
        c_socket.send(response.encode("utf-8"))
    
    c_socket.close()
    s_socket.close()

if __name__ == "__main__":
    main()
