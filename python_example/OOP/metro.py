class Station:
    def __init__(self, name: str, lines: list[str], id: int) -> None:
        self.name = name
        self.lines = lines
        self.id = id
        
    def get_infor(self) -> str:
        return f"{self.name}({self.lines})"
    
    
class Metro:
    def __init__(self) -> None:
        self._stations: list[Station] = []
        
    def add_station(self, name: str, lines: list[str], id: int) -> None:
        self._stations.append(Station(name, lines, id))
        
    def remove_station(self, id: int) -> None:
        for station in self._stations:
            if station.id == id:
                self._stations.remove(station)
                break
            
    def get_station(self, id: int) -> Station | None:
        for station in self._stations:
            if station.id == id:
                return station
        return None
    
    
class ExtraMetro(Metro):
    def __init__(self, lines: list[str]) -> None:
        self._lines = lines
        super().__init__()
        
    def find_stations_on_line(self, line: str) -> list[Station] | None:
        if line not in self._lines:
            return None
        
        output = []
        for station in self._stations:
            if line in station.lines:
                output.append(station)
                
        return output