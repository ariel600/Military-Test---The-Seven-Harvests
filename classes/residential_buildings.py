
class Residential_buildings:
    count = 1
    houses = list[dict]
    def __init__(self, rooms: int = 10, beds_of_room: int = 8):
        self.house = Residential_buildings.count
        self.rooms = rooms
        self.beds = beds_of_room
        self.soldiers = []
        Residential_buildings.houses.append({"house": self.house, "rooms": self.rooms, "beds": self.beds, "soldiers": self.soldiers})
        Residential_buildings.count += 1
        
    def add_sold_for_room(house: dict, soldier: dict):
        Residential_buildings.houses[house[""]]
        Residential_buildings.houses[house_nam].append((soldiers[beds], f"House {Residential_buildings.houses["house"]}, room {room + 1}"))
        

"""
houses = [{"house": 1, "rooms": 10, "beds": 8, "soldiers": []}]
"""