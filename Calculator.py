from tkinter import Tk, Button, Entry, StringVar

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")
        master.config(bg="lightgray")
        master.resizable(0, 0)

        self.expression = ""
        self.input_text = StringVar()

        self.input_field = Entry(master, bg="white", textvariable=self.input_text, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            Button(master, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(key)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()