
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
    
    @staticmethod   
    def add_sold_for_room(house_index: int, soldier: dict): #הוספת חייל לחדר 
        Residential_buildings.houses[house_index]["soldiers"].append(soldier)

    @staticmethod
    def print_houses(): #הדפסת כל הדירות 
        for house in Residential_buildings.houses:
            print(house)