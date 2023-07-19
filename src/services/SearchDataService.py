from models.base.StartDBModel import db
from models.dadosCashBack import dadosCashback
import json
from datetime import datetime, timedelta

class SearchDataConsult:
    def meta(store):
        currentTime = datetime.now()
        threeHoursAgo = currentTime - timedelta(hours=3)
        ruleScrapping = db.session.execute(db.select(dadosCashback).where(dadosCashback.created_at >= threeHoursAgo)).scalars()
        dataSerialized = json.dumps(ruleScrapping.all())
        return dataSerialized