from tkinter import *
import pyautogui
from colormap import rgb2hex
import keyboard
import pyperclip


class Janela:
    def __init__(self, master=None):

        self.firstContainer = Frame()
        self.firstContainer.pack()

        self.secondContainer = Frame()
        self.secondContainer.pack()

        self.screenLabel = Label(self.firstContainer, text="")
        self.screenLabel["font"] = "Arial 20 bold"
        self.screenLabel.grid(pady=30)

        self.rgbLabel = Label(self.secondContainer, text="")
        self.rgbLabel["font"] = "Arial 20 bold"
        self.rgbLabel.grid(pady=25)

        self.get_mouse_position()

    def get_mouse_position(self):
        # Pegar posição do mouse
        x, y = pyautogui.position()
        # Colocar as coordenadas na tela
        self.screenLabel["text"] = f"X = {x}, Y = {y}"

        # Pegar RGB
        x, y = pyautogui.position()
        self.rgb = pyautogui.screenshot().getpixel((x, y))

        # Tranforma RGB em Hexadecimal para a fonte do tkinter
        hex_color = rgb2hex(self.rgb[0], self.rgb[1], self.rgb[2])

        # Colocando os valores RGB na tela
        self.rgbLabel["text"] = f"R: {self.rgb[0]}, G: {self.rgb[1]}, B: {self.rgb[2]}"
        self.rgbLabel["fg"] = hex_color
        if self.rgb[0] & self.rgb[1] & self.rgb[2] >= 223:
            self.rgbLabel["fg"] = "black"

        # Copiar para o clipboard
        if keyboard.is_pressed("ctrl+t"):
            print("Copy")
            pyperclip.copy(str(f"rgb{self.rgb}"))

        # Update da tela
        root.update()
        self.screenLabel.after(1, self.get_mouse_position)


root = Tk()
root.geometry("350x200")
root.resizable(False, False)
root.title("Mouse Position")
Janela(root)
root.mainloop()
