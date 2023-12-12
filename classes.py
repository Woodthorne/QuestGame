from abc import ABC

class Encounter(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
    
    def activate(self) -> None:
        pass

class Location:
    def __init__(self, name: str, encounters: list[Encounter]) -> None:
        self._name = name
        self._encounters = encounters
        self._paths: list[Location] = []

    @property
    def name(self):
        return self.name

    @property
    def paths(self):
        return self._paths
    
    @paths.setter
    def paths(self, location):
        self._paths.append(location)

    def activate(self) -> None:
        if len(self.paths) == 1:
            encounter = self.paths[0]
        else:
            