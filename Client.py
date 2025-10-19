import socket
import threading
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# GUI for key input
root = tk.Tk()
root.withdraw()
key_input = simpledialog.askstring("Encryption Key", "Enter encryption key provided by server:")
key = key_input.encode()
cipher = Fernet(key)

# Connect to server
client = socket.socket()
client.connect(('localhost', 9999))

# GUI setup
window = tk.Tk()
window.title("Secure Chat - Client")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20)
chat_area.pack(padx=10, pady=10)
chat_area.config(state=tk.DISABLED)

message_entry = tk.Entry(window, width=40)
message_entry.pack(side=tk.LEFT, padx=10, pady=10)
send_button = tk.Button(window, text="Send", width=10)
send_button.pack(side=tk.LEFT)

def receive_messages():
    while True:
        enc_msg = client.recv(1024)
        if not enc_msg:
            break
        msg = cipher.decrypt(enc_msg).decode()
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Server: {msg}\n")
        chat_area.config(state=tk.DISABLED)

def send_message():
    msg = message_entry.get()
    enc_msg = cipher.encrypt(msg.encode())
    client.send(enc_msg)
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {msg}\n")
    chat_area.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

send_button.config(command=send_message)

threading.Thread(target=receive_messages, daemon=True).start()
window.mainloop()