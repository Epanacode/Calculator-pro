import tkinter as tk

root = tk.Tk()
root.title("Calculator Pro")
root.configure(bg="black")

# لیست تاریخچه نتایج
history = []

# نمایشگر
display = tk.Entry(
    root, font=("Arial", 24, "bold"),
    bg="#333333", fg="white", bd=0, justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="nsew")

# استایل رنگ‌ها
colors = {
    "number": "#1a1a1a",
    "operator": "#8000ff",
    "action": "#ff6600",
    "equal": "#00cc66"
}

button_font = ("Arial", 18, "bold")

# تابع نمایش تاریخچه
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("تاریخچه نتایج")
    history_window.configure(bg="black")
    tk.Label(history_window, text="تاریخچه:", font=("Arial", 16, "bold"), fg="white", bg="black").pack(pady=10)
    for item in history:
        tk.Label(history_window, text=item, font=("Arial", 14), fg="#00cc66", bg="black").pack()

# تابع مدیریت کلیک دکمه‌ها
def on_button_click(value):
    if value == "C":
        display.delete(0, tk.END)
    elif value == "←":
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, current[:-1])
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, str(result))
            history.append(str(result))  # ذخیره نتیجه در تاریخچه
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "خطا")
    elif value == "History":
        show_history()
    else:
        display.insert(tk.END, value)

# تابع ساخت دکمه‌ها برای راحتی
def make_button(text, row, col, color, colspan=1):
    tk.Button(
        root, text=text, font=button_font, fg="white",
        bg=color, bd=0, relief="ridge",
        activebackground=color, activeforeground="white",
        command=lambda: on_button_click(text)
    ).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)

# ردیف 1
make_button("C", 1, 0, colors["action"], colspan=2)
make_button("←", 1, 2, colors["action"])
make_button("/", 1, 3, colors["operator"])

# ردیف 2
make_button("7", 2, 0, colors["number"])
make_button("8", 2, 1, colors["number"])
make_button("9", 2, 2, colors["number"])
make_button("*", 2, 3, colors["operator"])

# ردیف 3
make_button("4", 3, 0, colors["number"])
make_button("5", 3, 1, colors["number"])
make_button("6", 3, 2, colors["number"])
make_button("-", 3, 3, colors["operator"])

# ردیف 4
make_button("1", 4, 0, colors["number"])
make_button("2", 4, 1, colors["number"])
make_button("3", 4, 2, colors["number"])
make_button("+", 4, 3, colors["operator"])

# ردیف 5
make_button("0", 5, 0, colors["number"])
make_button(".", 5, 1, colors["number"])
make_button("=", 5, 2, colors["equal"])
make_button("History", 5, 3, colors["action"])

# تنظیم اندازه نسبی سلول‌ها
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()
