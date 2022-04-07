#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

mysheet = DataManager()
sheet_data = mysheet.getData()
print(sheet_data)