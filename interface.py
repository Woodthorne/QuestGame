import os
from game_logic import GameLogic

class Interface:

    def main_menu(self) -> None:
        while True:
            self._print_menu('QUEST GAME', options = ['New Game'], escape = 'Quit Game')
            opt = input('>>> ')
            if opt == '0':
                quit()
            elif opt == '1':
                self._new_game()

    def _new_game(self) -> None:
        self._gll = GameLogic()
        while True:
            self._print_menu('QUEST GAME: New Game',
                    listing = ['Enter number of players',
                                '0. Return to main menu'])
            opt = input('>>> ')
            if opt == '0':
                return
            elif opt.isnumeric():
                self._print_menu('QUEST GAME: Characters',
                        listing = ['Enter names of players',
                                    '0. Return to main menu'])
                for num in range(1, int(opt) + 1):
                    name = input(f'Player {num}: ')
                    if name == '0':
                        return
                    else:
                        self._gll.add_player(name)
                self._play_game()
            else:
                pass

    def _play_game(self) -> None:
        pass

    def _new_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def _print_menu(self,
                    header: str,
                    menu_width: int = 6,
                    description: str = None,
                    listing: list[str] = None,
                    options: list[str] = None,
                    escape: str = None
                    ) -> None:
        self._new_screen()
        if len(header) > 2:
            menu_width += len(header) - 2
        if listing:
            for item in listing:
                if len(item) + 4 > menu_width:
                    menu_width = len(item) + 4
        if options:
            for item in options:
                if len(item) + 7 > menu_width:
                    menu_width = len(item) + 7
        if escape and len(escape) + 7 > menu_width:
            menu_width = len(escape) + 7
        content_width = menu_width - 4

        print(menu_width) # REMOVE AFTER TESTING
        print(f'=={header}{"=" * (content_width - len(header))}==')
        option_num = 0
        if description:
            if len(description) <= content_width:
                padding = content_width - len(description)
                print(f'| {description}{" " * padding} |')
            else:
                split_description = description.split(' ')
                while split_description:
                    current_row = ''
                    while split_description and len(current_row) \
                                                + len(split_description[0]) \
                                                + 1 \
                                                    <= content_width:
                        current_row += ' ' + split_description.pop(0)
                    padding = content_width - len(current_row)
                    print(f'| {current_row}{" " * padding} |')
            print('=' * menu_width)
        
        if listing:
            for item in listing:
                padding = content_width - len(item)
                print(f'| {item}{" " * padding} |')
            print('=' * menu_width)

        if options:
            for item in options:
                option_num += 1
                padding = content_width - len(item) - 3
                print(f'| {option_num}. {item}{" " * padding} |')
        if escape:
            padding = content_width - len(escape) - 2
            print(f'| 0. {escape}{" " * padding}|')
        if options or escape:
            print('=' * menu_width)
