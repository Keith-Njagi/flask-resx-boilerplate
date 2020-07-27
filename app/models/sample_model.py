from datetime import datetime

from marshmallow import Schema, fields

from . import db, ma

class Sample(db.Model):
    __tablename__='samples'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow(), nullable=True)

    def insert_record(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def fetch_all(cls):
        return cls.query.order_by(cls.id.asc()).all()

    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def fetch_by_role(cls, role):
        return cls.query.filter_by(role).first()

    @classmethod  
    def update(cls, id, name=None):
        record = cls.fetch_by_id(id)
        if name:
            record.name = name
        db.session.commit()
        return True

    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True

class SampleSchema(ma.Schema):
    class Meta:
        fields = ('id','name','created','updated')

