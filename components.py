import random
from abc import ABC

class Encounter(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
    
    def activate(self) -> None:
        pass


class Goblin(Encounter):
    def __init__(self, name: str = 'Goblins') -> None:
        super().__init__(name)
    
    def activate(self) -> None:
        super().activate()
        d6 = random.randint(1, 6)
        if d6 < 4:
            return 'Fail'
        elif d6 < 6:
            return 'Partial'
        else:
            return 'Full'


class Location:
    def __init__(self, name: str, encounters: list[Encounter]) -> None:
        self._name = name
        self._encounters = encounters
        self._paths: list[Location] = []

    @property
    def name(self):
        return self._name

    @property
    def encounters(self):
        return self._encounters

    @property
    def paths(self):
        return self._paths
    
    @paths.setter
    def paths(self, location):
        self._paths.append(location)


class Player:
    def __init__(self, name: str, location: Location) -> None:
        self._name = name
        self._location = location
    
    def travel(self, destination: Location) -> bool:
        if destination in self._location.paths:
            self._location = destination
            return True
        else:
            return False
    
    def _activate(self) -> None:
        pass