import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog
import socket
import threading
import os

class ClientGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Client")
        self.geometry("500x500")
        self.resizable(False, False)

        self.connect_btn = tk.Button(self, text="Connect to Server", command=self.connect_server)
        self.connect_btn.pack(pady=20)

        self.disconnect_btn = tk.Button(self, text="Disconnect", command=self.disconnect_server, state=tk.DISABLED)
        self.disconnect_btn.pack(pady=10)

        self.send_btn = tk.Button(self, text="Send Data", command=self.send_data, state=tk.DISABLED)
        self.send_btn.pack(pady=10)

        self.send_file_btn = tk.Button(self, text="Send File", command=self.send_file, state=tk.DISABLED)
        self.send_file_btn.pack(pady=10)

        self.entry_label = tk.Label(self, text="Enter data:")
        self.entry_label.pack()

        self.entry_text = tk.Entry(self)
        self.entry_text.pack()

        self.client_socket = None

    def connect_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(("192.168.0.9", 8080))
            self.connect_btn.config(state=tk.DISABLED)
            self.disconnect_btn.config(state=tk.NORMAL)
            self.send_btn.config(state=tk.NORMAL)
            self.send_file_btn.config(state=tk.NORMAL)
        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Failed to connect to the server.")
            self.client_socket = None

    def disconnect_server(self):
        if self.client_socket:
            self.client_socket.close()
        self.connect_btn.config(state=tk.NORMAL)
        self.disconnect_btn.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED)
        self.send_file_btn.config(state=tk.DISABLED)
        self.client_socket = None

    def send_data(self):
        data = self.entry_text.get()
        self.client_socket.send(data.encode())
        self.entry_text.delete(0, tk.END)

    def send_file(self):
        filepath = tk.filedialog.askopenfilename(initialdir="/", title="Select a file")
        if filepath:
            filename = os.path.basename(filepath)
            filesize = os.path.getsize(filepath)

            self.client_socket.send("file".encode())
            self.client_socket.send(filename.encode())
            self.client_socket.send(str(filesize).encode())

            with open(filepath, "rb") as file:
                while True:
                    data = file.read(4096)
                    if not data:
                        break
                    self.client_socket.send(data)

            print(f"Sent file: {filename}")
            messagebox.showinfo("File Sent", "File has been successfully sent.")
client_gui = ClientGUI()
client_gui.mainloop()
