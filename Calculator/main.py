from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, interface):
        # Adjust the window size and title
        interface.title("Calculator")
        interface.geometry('360x400')  
        interface.config(bg='black')
        interface.resizable(False, False)

        # Setup the display entry
        self.equation = StringVar()
        self.entry_value = ''
        Entry(interface, width=17, bg='#fff', font=('Arial Bold', 24), textvariable=self.equation).place(x=10, y=10, width=340, height=50)

        # Setup buttons
        # Define button properties in a grid-like structure for better organization
        buttons = [
            '(', ')', '%', 'C',
            '1', '2', '3', '/',
            '4', '5', '6', 'x',
            '7', '8', '9', '-',
            '.', '0', '=', '+'
        ]
        # Starting coordinates
        x, y = 10, 70
        for i, button in enumerate(buttons):
            action = lambda x=button: self.show(x) if x not in ['C', '='] else (self.clear() if x == 'C' else self.solve())
            Button(interface, text=button, width=5, height=2, bg='white', command=action).place(x=x, y=y, width=80, height=50)
            x += 90
            if (i + 1) % 4 == 0:  # Move to next row after every 4 buttons
                x = 10
                y += 60

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            # Safely evaluate the expression
            result = str(eval(self.entry_value.replace('x', '*')))
            self.entry_value = result
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''

screen = Tk()
calculator = Calculator(screen)
screen.mainloop()
