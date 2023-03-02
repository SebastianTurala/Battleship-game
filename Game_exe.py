import sys
import tkinter as tk
from tkinter import *
from random_ship_deployment import random_playboard

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        # root window config
        self.title('BATTLESHIP')

        # menu
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.game_menu = Menu(self.menu)
        self.menu.add_cascade(label="Game", menu=self.game_menu)
        self.game_menu.add_command(label="New Game", command=self.restart)
        self.game_menu.add_command(label="Help")
        self.game_menu.add_separator()
        self.game_menu.add_command(label='Exit', command=exit)

        # frame_1 - image and play button
        self.frame_1 = Frame(self)
        self.frame_1.pack()

            # image
        self.photo = PhotoImage(file=r"C:\Users\sebas\Desktop\Sea2.png")
        self.photo_label = Label(self.frame_1, image=self.photo)
        self.photo_label.pack()

            # play button
        self.play_button = Button(self.frame_1, text= 'Play', foreground='blue', font='arial 18', height=1, width=25, command=self.play_button)
        self.play_button.pack()

        # frame_2 - display
        self.frame_2 = Frame(self)

            # shots_count
        self.shots = 0
        self.shots_text = 'Shots: ' + str(self.shots)
        self.shots_display = StringVar()
        self.shots_display.set(self.shots_text)
                # shots_count place
        self.shots_label = Label(self.frame_2, textvariable=self.shots_display, relief='solid', width= 51)
        self.shots_label.pack()

            # message_display
        self.message = StringVar()
        self.message.set("Let's start!")
        self.message_display = Label(self.frame_2, textvariable=self.message)
        self.message_display.pack()

        # frame_3 - playboard
        self.frame_3 = Frame(self)

            # "ABC" and "123 border"
        self.border_generator()

            # playboard_matrix
        self.matrix = [['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '']]
        self.button_matrix_generator()

            # random_ship_matrix
        self.matrix2 = random_playboard()
        self.ship_symbols = ['A', 'B', 'C', 'F']

        self.hits = 0

        # Frame 4 - endgame
        self.frame_4 = Frame(self)

            # Yes button
        self.yes_button = Button(self.frame_4, text= 'YES')
        self.yes_button.grid(row=0, column =0)
            # No button
        self.no_button = Button(self.frame_4, text= 'NO', command= self.exit)
        self.no_button.grid(row=0, column=1)

    # commands
    def exit(self):
        sys.exit()

    def play_button(self):
        self.play_button.destroy()
        self.frame_2.pack()
        self.frame_3.pack()

    def border_generator(self):
        for i in range(11):
            self.letters = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            self.top_frame = Label(self.frame_3, width=4, height=2, text=self.letters[i])
            self.top_frame.grid(row=0, column=i)
        for i in range(10):
            self.left_frame = Label(self.frame_3, width=4, height=2, text=i + 1)
            self.left_frame.grid(row=i + 1, column=0)

    def button_press(self, x, y):
        if self.matrix2[x][y] == '':
            self.shots += 1
            self.shots_text = 'Shots: ' + str(self.shots)
            self.shots_display.set(self.shots_text)
            self.matrix2[x][y] = 'X'
            self.matrix[x][y].config(text='o')
            self.message.set('MISS!')

        elif self.matrix2[x][y] in self.ship_symbols:
            self.shots += 1
            self.shots_text = 'Shots: ' + str(self.shots)
            self.shots_display.set(self.shots_text)
            if self.matrix2[x][y] == "A":
                self.message.set("Hit. It's an aircraft carrier! (5)")
            if self.matrix2[x][y] == "B":
                self.message.set("Hit. It's a battleship! (4)")
            if self.matrix2[x][y] == "C":
                self.message.set("Hit. It's a cruiser! (3)")
            if self.matrix2[x][y] == "F":
                self.message.set("Hit. It's a fregate! (2)")
            self.matrix2[x][y] = 'X'
            self.matrix[x][y].config(text='X', background='red', cursor='pirate')
            self.hits_check()

        elif self.matrix2[x][y] == 'X':
            self.message.set("You already check this place!")

    def button_matrix_generator(self):
        for i in range(10):
            for j in range(10):
                self.matrix[i][j] = Button(self.frame_3, width=4, height=2, command=lambda x1=i, y1=j: self.button_press(x1, y1))
                self.matrix[i][j].grid(row=i + 1, column=j + 1)
    def hits_check(self):
        self.hits += 1
        if self.hits == 26: #max = 26
            self.frame_3.destroy()
            self.message.set("You Win! Play again?")
            self.frame_4.pack()

    def restart(self):
        self.message.set("Let's start!")




if __name__ == '__main__':
    app = App()
    app.mainloop()