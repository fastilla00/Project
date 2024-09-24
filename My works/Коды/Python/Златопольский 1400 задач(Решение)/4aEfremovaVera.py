import platform
import tkinter as tk

def get_system_info():
    system_info = ""
    system_info += f"Операционная система: {platform.system()} {platform.release()}\n"
    system_info += f"Версия Python: {platform.python_version()}\n"
    system_info += f"Архитектура процессора: {platform.machine()}\n"
    system_info += f"Платформа: {platform.platform()}\n"
    system_info += f"Имя пользователя: {platform.node()}\n"
    system_info += f"Тип системы: {platform.system()}"

    return system_info

app = tk.Tk()
app.title("Информация о системе")

info_label = tk.Label(app, text=get_system_info(), justify="left")
info_label.pack(padx=10, pady=10)

app.mainloop()
