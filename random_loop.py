import random
from kivy.app import App
from kivy.lang import Builder

class RandomLoop(App):
    def build(self):
        self.title = " "
        self.root = Builder.load_file('random_loop.kv')
        return self.root





def main():

    menu = input("Enter y for continue, or q for quit: >>> ")
    while menu != "q".lower():
        if menu == "y".lower():
            names = ['Mardy', 'Molly', 'Bunny', 'Penny', 'Akela', 'Toby', 'Pepper', 'Cassie']
            print(random.choice(names))
            menu = input("play again: >>>").lower()
        else:
            menu = input("Try y or q: >>>").lower()
    print("game over")
main()
