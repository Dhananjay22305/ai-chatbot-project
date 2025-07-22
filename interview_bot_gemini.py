import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai


genai.configure(api_key="AIzaSyC84hKRgSMRcXteYmR4_YeBvPMaz2rdgRc")


model = genai.GenerativeModel("models/gemini-1.5-flash")

# Function to handle user input and get response
def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    user_entry.delete(0, tk.END)

    try:
        response = model.generate_content(user_input)
        bot_response = response.text.strip()
        chat_window.insert(tk.END, f"Bot: {bot_response}\n", "bot")
    except Exception as e:
        chat_window.insert(tk.END, f"Bot: [Error] {e}\n", "bot")

    chat_window.config(state='disabled')
    chat_window.see(tk.END)

# Create main app window
root = tk.Tk()
root.title("Gemini Chatbot")
root.geometry("600x600")
root.configure(bg="#1e1e1e")


header_frame = tk.Frame(root, bg="#1e1e1e")
header_frame.pack(pady=(10, 0), fill=tk.X)

welcome_label = tk.Label(
    header_frame,
    text="Welcome to Chatbot",
    bg="#1e1e1e",
    fg="#00ffff",
    font=("Arial", 20, "bold")
)
welcome_label.pack(anchor="center")

# Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', bg="#252526", fg="#d4d4d4", font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.tag_config("user", foreground="#9cdcfe", font=("Arial", 12, "bold"))
chat_window.tag_config("bot", foreground="#ce9178", font=("Arial", 12, "italic"))


input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=10, fill=tk.X, padx=10)

user_entry = tk.Entry(input_frame, font=("Arial", 14), bg="#3c3c3c", fg="#ffffff", insertbackground="white")
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
user_entry.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", command=send_message, font=("Arial", 12, "bold"), bg="#007acc", fg="white")
send_button.pack(side=tk.RIGHT)
root.mainloop()
