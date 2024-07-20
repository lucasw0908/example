class Station:
    name: str
    lines: list[str]
    id: int
    def get_infor(self) -> str:
        return f"{self.name}({self.lines})"
    
station = Station()
station.name = "中正紀念堂"
station.lines = ["紅線", "綠線"]
print(station.get_infor())
# >>中正紀念堂(['紅線', '綠線'])