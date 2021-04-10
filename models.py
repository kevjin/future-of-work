from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    xy = db.Column(db.String())
    value = db.Column(db.String())
    # result_no_stop_words = db.Column(JSON)

    def __init__(self, xy, value):
        self.xy = xy
        self.value = value
        # self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)