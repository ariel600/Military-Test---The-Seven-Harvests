import csv

class Soldier:
    soldiers = [{"id": 152632, "first_name": "aaa", "last_name": "qqq", "gender": "z", "citi": "1", "distance": 100, "status": False, "house": ()}]
    soldiers_error = list[dict]
    
    def loadCSV(file_path): # קבלת קובץ 
        data = []
        with open(file_path, mode ='r') as table:
            csvFile = csv.reader(table)
            columns = next(csvFile)  # Skip header
            for line in csvFile:
                data.append(dict(zip(columns, line)))
        return data
    
    def add_house_for_soldier(soldier: dict, house): #הוספת מקום מגורים לחייל + סטטוס 
        Soldier.soldiers["soldier"] = house
        Soldier.soldiers["status"] = True   
        
    def add_error(soldier: dict): #הוספת חיילים עם מס' אישי לא תקין 
        Soldier.soldiers_error.append(soldier)

    def integrity_check(soldiers: list[dict]): #בדיקת תקינות 
        result = []
        for soldier in soldiers:
            if isinstance(soldier["id"], int):
                result.append(soldier)
            else:
                Soldier.add_error(soldier)
        return result
         
    def sort_help(c): # פונקציית עזר למיון
        return c["distance"]

    def sort_by_km(soldiers: list[dict]): #מיון לפי ק"מ 
        return soldiers.sort(reverse=True, key=Soldier.sort_help)
    
    def print_errors(): #הדפסת החיילים עם מספר אישי שגוי 
        for soldiers_error in Soldier.soldiers_error:
            print(soldiers_error)