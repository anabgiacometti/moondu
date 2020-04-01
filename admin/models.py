from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


class SlidersHome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text)
    video = db.Column(db.String(500))
    active = db.Column(db.Boolean)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text)
    image = db.Column(db.LargeBinary())

class AboutUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text)
    video = db.Column(db.String(500))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.LargeBinary())
    name = db.Column(db.String(500))


class ClientPhrases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_1 = db.Column(db.String())
    phone_2 = db.Column(db.String())
    email = db.Column(db.String())
    address_1 = db.Column(db.String())
    address_2 = db.Column(db.String())
    facebook = db.Column(db.String())
    whatsapp = db.Column(db.String())
    linkdeIn = db.Column(db.String())
    instagram = db.Column(db.String())
    blog = db.Column(db.String())
    areaDoCliente = db.Column(db.String())
    

class Methods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary())
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    