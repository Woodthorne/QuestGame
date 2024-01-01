from components import Location, Goblin, Player
from interface import Interface
from pygame_app import App

def run() -> None:
    interface = Interface()
    interface.main_menu()

if __name__ == '__main__':
    # app = App()
    # app.on_execute()
    run()
    pass