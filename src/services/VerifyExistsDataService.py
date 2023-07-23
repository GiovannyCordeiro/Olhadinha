from models.base.StartDBModel import db
from datetime import datetime, timedelta

class VerifyExistsDataService:
    def search():
        currentTime = datetime.now() 
        threeHrsAgo = currentTime - timedelta(hours=3)
        
        return f"{threeHrsAgo}"