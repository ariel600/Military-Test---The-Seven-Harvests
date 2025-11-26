from residential_buildings import Residential_buildings
from soldier import Soldier

class Inlay:
    waiting = []
    
    @staticmethod
    def print_waiting() -> None: #הדפסת חיילים ממתינים 
        for soldier in Inlay.waiting:
            print(soldier) 

    @staticmethod
    def add_waiting(soliders: list[dict]): #הוספה לרשימת המתנה 
        if len(soliders) >= 0:
            for solider in soliders:
                Inlay.waiting.append(solider)
    
    @staticmethod
    def add_for_room(soldiers: list[dict]): #שיבוץ חדרים 
        for list_houses in range(Residential_buildings.houses):
            for room in range(list_houses["rooms"]):
                for beds in range(list_houses["beds"]):
                    Residential_buildings.add_sold_for_room(list_houses, soldiers[beds]) #מוסיף את החיילים לחדר 
                    Soldier.add_house_for_soldier(soldiers[beds], f"House{Residential_buildings.houses["house"]}, room {room + 1}") #הוספת מקום מגורים 
                    soldiers.pop(beds)
        Inlay.add_waiting(soldiers)