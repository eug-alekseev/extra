from db.db_init import db


class Expense(db.Model):
    id = db.Column(db.Integer, name='id', primary_key=True)

    amount = db.Column(db.Integer, unique=False, nullable=False)
    category = db.Column(db.String(64), unique=False, nullable=False)
    comment = db.Column(db.String(256), unique=False, nullable=False)

    def __repr__(self):
        return f'<Expense {self.category}>'
