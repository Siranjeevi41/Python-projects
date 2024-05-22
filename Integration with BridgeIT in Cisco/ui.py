import tkinter as tk
from bridgeit_api import get_bridgeit_response

def on_submit():
    query = query_entry.get()
    category = category_var.get()
    response = get_bridgeit_response(query, category)
    response_label.config(text=response)

app = tk.Tk()
app.title("BridgeIT Integration")

tk.Label(app, text="Enter your query:").pack()
query_entry = tk.Entry(app)
query_entry.pack()

category_var = tk.StringVar(value="Non-Cisco course")
categories = ["Non-Cisco course", "Cisco course", "Movie", "Cisco products"]
tk.OptionMenu(app, category_var, *categories).pack()

tk.Button(app, text="Submit", command=on_submit).pack()
response_label = tk.Label(app, text="")
response_label.pack()

app.mainloop()
