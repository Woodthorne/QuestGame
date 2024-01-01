from components import Location, Player
from data_access import DataAccess

class GameLogic():
    def __init__(self) -> None:
        self._dal = DataAccess()
        self._player_list: list[Player] = []
        self._location_list: list[Location] = []
        location_data = self._dal.read_csv('location_data.csv')
        for location in location_data:
            name = location['name']
            encounters = location['encounters'].split('|')
            self._location_list.append(Location(name, encounters))
        

    def add_player(self, player_name, location_id: int = 0) -> None:
        print(self._location_list[location_id])
        self._player_list.append(Player(player_name,
                                        self._location_list[location_id]
                                        )
                                 )