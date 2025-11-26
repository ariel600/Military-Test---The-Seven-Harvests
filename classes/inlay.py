from residential_buildings import Residential_buildings
from soldier import Soldier

class Inlay:
    waiting = []
    
    def print_waiting() -> None: #הדפסת חיילים ממתינים 
        for soldier in Inlay.waiting:
            print(soldier) 

    def add_waiting(soliders: list[dict]): #הוספה לרשימת המתנה 
        if len(soliders) >= 0:
            for solider in soliders:
                Inlay.waiting.append(solider)
    
    def add_error(solider): #הוספה לרשימת שגיאות 
        Inlay.errors.append(solider)

    def add_for_room(soldiers: list[dict]): #הוספת חיילים לחדר 
        for list_houses, index in Residential_buildings.houses:
            for room in range(list_houses["rooms"]):
                for beds in range(list_houses["beds"]):
                    Residential_buildings.add_sold_for_room(, soldiers[beds]) #מוסיף את החיילים לחדר
                    Soldier.add_house_for_soldier(soldiers[beds], f"House{list_houses["house"]}, room {room + 1}") #הוספת מקום מגורים
                    Soldier.status_update(soldiers[beds]) #משנה את הסטטוס מגורים
                    soldiers.pop(beds)
        Inlay.add_waiting(soldiers)
  
"""      
{"House": list_houses["house"], "Room": room + 1}
"""