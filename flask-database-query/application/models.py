from . import db


class Todos(db.Model):
    __tablename__ = 'todos'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    todo = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    def __repr__(self):
        return '<Todo {}>'.format(self.todo)