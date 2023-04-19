import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import json

def remove_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)

def add_placeholder(event, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
            
root = tk.Tk()
root.title("Token Validator")

def validate_token():
    token = token_entry.get()
    selected = token_selector.get()
    if selected == "Roblox":
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': f'.ROBLOSECURITY={token}',
        }

        response = requests.get("https://users.roblox.com/v1/users/authenticated", headers=headers)
        data = json.loads(response.text)
        if 'name' in response.text:
            username = data['name']
            messagebox.showinfo("Token Valid", f"Successfully connected to {username}!")
        else:
            messagebox.showerror("Token Invalid", "Incorrect token")
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'X-Auth-Token': token
        }
        response = requests.get("https://rest-bf.blox.land/user", headers=headers)
        data = json.loads(response.text)
        if '"success":true' in response.text:
            username = data["user"]["robloxUsername"]
            messagebox.showinfo("Token Valid", f"Successfully connected to {username}!")
        else:
            messagebox.showerror("Token Invalid", "Incorrect token")

token_selector = ttk.Combobox(root, values=["Bloxflip", "Roblox"], state="readonly", width=27)
token_selector.current(0)
token_selector.pack(padx=10, pady=10)
            
token_placeholder = "token"
token_entry = ttk.Entry(root, width=30)
token_entry.pack(pady=10, padx=10)
token_entry.insert(0, token_placeholder)
token_entry.bind("<FocusIn>", lambda event: remove_placeholder(event, token_entry, token_placeholder))
token_entry.bind("<FocusOut>", lambda event: add_placeholder(event, token_entry, token_placeholder))

button = ttk.Button(root, text="Validate", command=validate_token)
button.pack(padx=10, pady=10)

root.mainloop()
