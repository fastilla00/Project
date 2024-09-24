import tkinter as tk

def convert_to_uppercase():
    text = entry.get()
    uppercase_text = text.upper()
    label.config(text=uppercase_text)

app = tk.Tk()
app.title("Преобразование текста в верхний регистр")

entry = tk.Entry(app)
entry.pack(pady=10)

button = tk.Button(app, text="Преобразовать", command=convert_to_uppercase)
button.pack(pady=5)

label = tk.Label(app, text="")
label.pack(pady=10)

app.mainloop()
