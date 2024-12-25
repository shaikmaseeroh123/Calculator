import tkinter as tk

# Function to handle button clicks
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        input_var.set("")
    elif text == "←":
        expression = expression[:-1]
        input_var.set(expression)
    else:
        expression += text
        input_var.set(expression)

# Function to toggle between dark and light theme
def toggle_theme():
    global dark_theme
    if dark_theme:
        dark_theme = False
        root.configure(bg=light_bg_color)
        button_frame.configure(bg=light_bg_color)
        display.configure(bg=light_display_bg_color, fg=light_display_fg_color)
        for widget in button_frame.winfo_children():
            widget.configure(bg=light_button_bg_color, fg=light_button_fg_color,
                             activebackground=light_button_active_bg, activeforeground=light_button_fg_color)
    else:
        dark_theme = True
        root.configure(bg=dark_bg_color)
        button_frame.configure(bg=dark_bg_color)
        display.configure(bg=dark_display_bg_color, fg=dark_display_fg_color)
        for widget in button_frame.winfo_children():
            widget.configure(bg=dark_button_bg_color, fg=dark_button_fg_color,
                             activebackground=dark_button_active_bg, activeforeground=dark_button_fg_color)

    # Toggle the theme state
    theme_button.configure(bg=toggle_button_bg_color, fg=toggle_button_fg_color)

# Initialize the main application
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")  # Increased height to fit toggle button properly
root.resizable(False, False)

# Global variables
expression = ""
input_var = tk.StringVar()

# Dark Theme Colors
dark_bg_color = "#333333"
dark_button_bg_color = "#555555"
dark_button_active_bg = "#777777"
dark_button_fg_color = "#FFFFFF"
dark_display_bg_color = "#222222"
dark_display_fg_color = "#FFFFFF"

# Light Theme Colors
light_bg_color = "#FFFFFF"
light_button_bg_color = "#D3D3D3"
light_button_active_bg = "#B0B0B0"
light_button_fg_color = "#000000"
light_display_bg_color = "#F0F0F0"
light_display_fg_color = "#000000"

# Toggle button colors
toggle_button_bg_color = "#4C8CFF"
toggle_button_fg_color = "#FFFFFF"

# Initial theme is dark
dark_theme = True

# Display screen
display = tk.Entry(
    root,
    textvar=input_var,
    font=("Arial", 20),
    justify="right",
    bd=8,
    relief=tk.SUNKEN,
    bg=dark_display_bg_color,
    fg=dark_display_fg_color,
    insertbackground=dark_display_fg_color,  # Cursor color
)
display.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["C", "←", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "//", "="],
]

# Create button frame
button_frame = tk.Frame(root, bg=dark_bg_color)
button_frame.pack(fill=tk.BOTH, expand=True)

# Define button size
button_size = 80

# Create buttons
for row_idx, row in enumerate(buttons):
    for col_idx, text in enumerate(row):
        # Different color schemes for different buttons
        if text in ("C", "←"):
            color = dark_button_bg_color if dark_theme else light_button_bg_color
        elif text in ("+", "-", "*", "/", "%", "//", "="):
            color = dark_button_bg_color if dark_theme else light_button_bg_color
        else:
            color = dark_button_bg_color if dark_theme else light_button_bg_color

        btn = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 18),
            relief=tk.RAISED,
            bd=3,
            bg=color,
            fg=dark_button_fg_color if dark_theme else light_button_fg_color,
            activebackground=dark_button_active_bg if dark_theme else light_button_active_bg,
            activeforeground=dark_button_fg_color if dark_theme else light_button_fg_color,
        )
        btn.grid(
            row=row_idx,
            column=col_idx,
            ipadx=button_size // 10,
            ipady=button_size // 10,
            padx=5,
            pady=5,
            sticky="nsew",
        )
        btn.bind("<Button-1>", click)

# Configure rows and columns to maintain square button layout
for i in range(len(buttons)):
    button_frame.rowconfigure(i, weight=1, minsize=button_size)
for j in range(len(buttons[0])):
    button_frame.columnconfigure(j, weight=1, minsize=button_size)

# Create theme toggle button
theme_button = tk.Button(
    root,
    text="Change Theme",
    font=("Arial", 16),
    relief=tk.RAISED,
    bd=3,
    bg=toggle_button_bg_color,
    fg=toggle_button_fg_color,
    command=toggle_theme,
)
theme_button.pack(fill=tk.X, pady=10)

# Run the application
root.mainloop()
