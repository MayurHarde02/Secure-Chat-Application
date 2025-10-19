# 🔐 Secure Chat Application (Python)

A beginner-friendly **cybersecurity project** built with **Python**, using **socket programming** and **encryption** to create a secure real-time chat between two users. This project demonstrates how encryption ensures privacy during message transmission.

---

## 🌟 Description

A secure chat application built in Python using socket programming, Tkinter GUI, and Fernet encryption. It enables real-time encrypted communication between a server and a client, demonstrating the basics of cybersecurity and data privacy with simple setup and strong AES-based message protection.

---

## 🌟 Aim

To develop a secure chat application that enables encrypted message exchange between a **server** and a **client** using the **Fernet symmetric encryption algorithm**.

---

## 🧠 Concepts Used

* **Socket Programming** – For communication between client and server.
* **Symmetric Encryption (Fernet from `cryptography`)** – To encrypt and decrypt chat messages.
* **Multithreading** – To allow simultaneous sending and receiving of messages.
* **Tkinter GUI** – For a user-friendly graphical interface.

---

## 🛠️ Requirements

Make sure Python 3.8+ is installed, then install the required library:

```bash
pip install cryptography
```

Tkinter is pre-installed with Python (no extra installation needed).

---

## 🗁 Project Files

| File                        | Description                                                               |
| --------------------------- | ------------------------------------------------------------------------- |
| `secure_chat_server_gui.py` | Server-side code that initializes connection and displays encryption key. |
| `secure_chat_client_gui.py` | Client-side code that connects using the shared key.                      |
| `README.md`                 | Documentation file explaining setup and usage.                            |

---

## 🧩 Features

✅ Real-time encrypted chat communication
✅ GUI interface for both server and client
✅ Uses Fernet encryption (AES 128-bit)
✅ Works locally or over the same Wi-Fi network
✅ Beginner-friendly, easy to extend with authentication or multi-client support

---

## 💻 How It Works

1. The **server** generates an encryption key and waits for a connection.
2. The **client** connects to the server and enters the provided key.
3. Both sides use the same key to **encrypt and decrypt** messages securely.
4. Messages appear in real-time in the GUI.

---

## ⚙️ How to Run in VS Code

### ✅ Step 1: Set Up Your Project Folder

1. Create a folder (e.g. `SecureChatApp`).
2. Inside it, create two files:

   * `secure_chat_server_gui.py`
   * `secure_chat_client_gui.py`
3. Paste the respective code into each file.

---

### ✅ Step 2: Install Required Libraries

Open VS Code’s terminal (**Ctrl + `**) and run:

```bash
pip install cryptography
```

---

### ✅ Step 3: Run the Server

1. Open **secure_chat_server_gui.py**.
2. Click **Run ▶️** (or press `Ctrl + F5`).
3. The server window will show an **encryption key** (e.g., `rA1D7l8f6T6KzG9kJvQ1F8x6A0sKzvQfVJ1M_6Z3m8E=`).
4. Keep this key visible — the client will need it.

---

### ✅ Step 4: Run the Client

You can run the client in two ways:

#### Option A – Use Two VS Code Windows

1. Open another VS Code window.
2. Open the same folder.
3. Open **secure_chat_client_gui.py** and run it.
4. Enter the key shown in the server window.

#### Option B – Use Two Terminals in One VS Code Window

1. Click the **“+”** button in the terminal panel to open a second terminal.
2. In the first terminal, run:

   ```bash
   python secure_chat_server_gui.py
   ```
3. In the second terminal, run:

   ```bash
   python secure_chat_client_gui.py
   ```
4. Paste the encryption key when prompted.

---

### ✅ Step 5: Chat Securely

* Type messages in either window — both sides will see encrypted messages being decrypted in real-time.
* All communication is protected using symmetric encryption.

---
