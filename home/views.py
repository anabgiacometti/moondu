from app import app, db
from flask import render_template, redirect, url_for, request, abort, session
from admin.models import SlidersHome, AboutUs, Client, ClientPhrases, News, Contact
from base64 import b64encode

@app.route('/')
def Home():   

    sliders = SlidersHome.query.order_by(SlidersHome.id).filter(SlidersHome.active == True).all();
    about = AboutUs.query.filter(AboutUs.id == 1).first();
    all_clients = Client.query.all()
    clients_text_all = ClientPhrases.query.all()
    all_news = News.query.all()
    contact = Contact.query.filter(Contact.id == 1).first()

    clients_text = ""
    for t in clients_text_all:
        clients_text += t.text + "£"

    clients = []
    for c in all_clients:
        image = b64encode(c.logo).decode("utf-8")
        clients.append(image)

    news = []
    for n in all_news:
        image = b64encode(n.image).decode("utf-8")
        news.append({"image": image, "title":n.title, "text":n.text})


    return render_template('home.html', sliders_home=sliders, about=about, clients=clients, clients_text=clients_text, news=news, contact=contact)

