from db import db
#from flask_validator import ValidateString, ValidateLength


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # @classmethod
    # def __declare_last__(cls):
    #     ValidateString(cls.name, False, False,
    #                    message="enter a String Type value")
    #     ValidateLength(cls.name, max_length=80, min_length=1, throw_exception=False,
    #                    message="the length of value is too long")

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
