from market import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email_address = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        budget = str(self.budget)
        if len(budget) >= 4:
            return f"{budget[:-3]},{budget[-3:]}"
        return budget

    @property
    def password(self):
        raise (NotImplementedError("Password can only be set !"))

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'

    def assign_to_user(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def remove_from_user(self, user):
        print("DEBUG")
        self.owner = None
        user.budget += self.price
        db.session.commit()
