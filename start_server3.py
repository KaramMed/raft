#!/usr/bin/env python
from raft import RaftNode
import json
import socket
import threading

address_book_fname = 'address_book.json'

def handle_commands(s0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', 9999))  # Bind to localhost on port 9999
        server_socket.listen(5)
        print("Command listener started on port 9999")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                command = data.decode('utf-8').strip()

                try:
                    if command.startswith("replayattack bypass "):
                        _, _, bypass_value = command.split(maxsplit=2)
                        bypass = bypass_value.lower() == "true"
                        print(f"Executing replay_attack with bypass_timestamp={bypass}")
                        s0.replay_attack(bypass_timestamp=bypass)
                        conn.sendall(b"replayattack executed successfully")

                    elif command.startswith("entryattack "):
                        _, message = command.split(maxsplit=1)
                        print(f"Executing send_entry_attack with message: {message}")
                        s0.send_entry_attack(message)
                        conn.sendall(b"entryattack executed successfully")

                    elif command == "stop":
                        print("Stopping the node")
                        s0.stop()
                        conn.sendall(b"node stopped successfully")
                        break

                    else:
                        print(f"Unknown command: {command}")
                        conn.sendall(b"error: invalid command")
                except Exception as e:
                    print(f"Error handling command '{command}': {e}")
                    conn.sendall(b"error: failed to execute command")

if __name__ == '__main__':
    d = {"node1": {"ip": "192.46.237.85", "port": "2380"},
         "node2": {"ip": "172.105.85.119", "port": "2380"},
         "node3": {"ip": "172.104.149.60", "port": "2380"}}
        
    with open(address_book_fname, 'w') as outfile:
        json.dump(d, outfile)

    s0 = RaftNode(address_book_fname, 'node3', 'follower')

    s0.start()

    # Start a thread to handle external commands
    threading.Thread(target=handle_commands, args=(s0,), daemon=True).start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        s0.stop()
