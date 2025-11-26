from classes.inlay import Inlay
# from classes.residential_buildings import Residential_buildings
from classes.soldier import Soldier
from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

@app.get("/")
def get_root():
    return "Welcome to the Soldiers' Apartment Assignment System!"

@app.post("/send-file")
def get_file(file: UploadFile = File()):
    data = Soldier.loadCSV(file) #העלאת קובץ 
    test = Soldier.integrity_check(data) #בדיקת תקינות מספר אישי 
    sort = Soldier.sort_by_km(test) #מיון לפי מרחק 
    add = Inlay.add_for_room(sort) #שיבוץ חדרים 
    return {
        "soldier_errors": Soldier.print_errors(),
        "soldier_waiting": Inlay.print_waiting()
    }

if __name__ == "__main__":
    uvicorn.run(app)