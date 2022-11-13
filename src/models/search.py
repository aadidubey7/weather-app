from db import db
from datetime import datetime, timezone

class SearchModel(db.Model):
    __tablename__ = "search_history"
    
    id = db.Column(db.Integer, primary_key=True)
    search_key = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.String(length=30), nullable=False)
    minimum_temp = db.Column(db.Float, nullable=False)
    maximum_temp = db.Column(db.Float, nullable=False)
    day = db.Column(db.String(length=50), nullable=False)
    night = db.Column(db.String(length=50), nullable=False)
    
    def __init__(self, search_args, search_data):
        self.search_key = search_args
        self.date = search_data.get("Date")
        self.minimum_temp = search_data.get("Temperature").get("Minimum").get("Value")
        self.maximum_temp = search_data.get("Temperature").get("Maximum").get("Value")
        self.day = search_data.get("Day").get("IconPhrase")
        self.night = search_data.get("Night").get("IconPhrase")

    def save(self):
        db.session.add(self)
        db.session.commit()
