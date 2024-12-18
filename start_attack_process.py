import socket

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect(('localhost', 9999))  # Connect to the main script
            client_socket.sendall(command.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            return response
        except ConnectionRefusedError:
            return "error: unable to connect to the main script"

if __name__ == '__main__':
    print("Interactive Command Sender")
    print("Type 'exit' to quit.")
    print("Available commands:")
    print("  replayattack bypass true")
    print("  replayattack bypass false")
    print("  entryattack \"Your message here\"")
    print("  stop")
    print()

    while True:
        user_input = input("Enter command: ").strip()
        if user_input.lower() == "exit":
            print("Exiting command sender.")
            break

        response = send_command(user_input)
        print(f"Response: {response}")
