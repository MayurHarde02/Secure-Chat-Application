import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from cryptography.fernet import Fernet

# generate key and cipher
key = Fernet.generate_key()
cipher = Fernet(key)

# create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("Server started.. waiting for clients on localhost:9999")

# GUI setup
root = tk.Tk()
root.title("Secure Chat Server")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)
chat_area.insert(tk.END, f"Encryption key: {key.decode()}\n")
chat_area.config(state=tk.DISABLED)

entry_frame = tk.Frame(root)
entry_frame.pack(fill=tk.X, padx=10, pady=(0,10))

message_entry = tk.Entry(entry_frame, width=40, font=("Arial", 12))
message_entry.pack(side=tk.LEFT, padx=(0,10))
send_button = tk.Button(entry_frame, text="Send", width=10, state=tk.DISABLED)
send_button.pack(side=tk.LEFT)

conn_holder = {'conn': None}

def receive_messages():
    conn = conn_holder['conn']
    if conn is None:
        return
    try:
        while True:
            enc_msg = conn.recv(4096)
            if not enc_msg:
                break
            try:
                msg = cipher.decrypt(enc_msg).decode()
            except Exception:
                msg = "<decryption failed>"
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, f"Client: {msg}\n")
            chat_area.config(state=tk.DISABLED)
    except Exception:
        pass
    finally:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Client disconnected\n")
        chat_area.config(state=tk.DISABLED)
        send_button.config(state=tk.DISABLED)
        conn.close()
        conn_holder['conn'] = None

def send_message():
    conn = conn_holder['conn']
    if not conn:
        return
    msg = message_entry.get().strip()
    if not msg:
        return
    enc_msg = cipher.encrypt(msg.encode())
    try:
        conn.sendall(enc_msg)
    except Exception:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Failed to send message\n")
        chat_area.config(state=tk.DISABLED)
        return
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {msg}\n")
    chat_area.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)
send_button.config(command=send_message)

def accept_connections():
    while True:
        conn, addr = server.accept()
        conn_holder['conn'] = conn
        print(f"Connection from {addr} has been established!")
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Connected by {addr}\n")
        chat_area.config(state=tk.DISABLED)
        send_button.config(state=tk.NORMAL)
        threading.Thread(target=receive_messages, daemon=True).start()

# start accept thread then GUI loop
threading.Thread(target=accept_connections, daemon=True).start()
root.mainloop()