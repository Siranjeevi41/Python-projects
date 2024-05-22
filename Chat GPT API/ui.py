import tkinter as tk
from chatgpt_api import get_gpt_response

def on_submit():
    query = query_entry.get()
    response = get_gpt_response(query)
    response_label.config(text=response)

app = tk.Tk()
app.title("ChatGPT Integration")

tk.Label(app, text="Enter your query:").pack()
query_entry = tk.Entry(app)
query_entry.pack()
tk.Button(app, text="Submit", command=on_submit).pack()
response_label = tk.Label(app, text="")
response_label.pack()

app.mainloop()
