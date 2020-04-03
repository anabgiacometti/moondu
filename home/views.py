from app import app, db, mail
from flask import render_template, redirect, url_for, request, abort, session, jsonify, make_response
from admin.models import SlidersHome, AboutUs, Client, ClientPhrases, News, Contact, Methods
from base64 import b64encode
from flask_wtf.csrf import CSRFProtect
from flask_mail import Message

csrf = CSRFProtect(app)

@app.route('/')
def Home():   

    sliders = SlidersHome.query.order_by(SlidersHome.id).filter(SlidersHome.active == True).all();
    about = AboutUs.query.filter(AboutUs.id == 1).first();
    all_clients = Client.query.all()
    clients_text_all = ClientPhrases.query.all()
    all_news = News.query.all()
    contact = Contact.query.filter(Contact.id == 1).first()
    all_methods = Methods.query.order_by(Methods.id).all()

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

    methods = []
    for m in all_methods:
        image = b64encode(m.image).decode("utf-8")
        methods.append({"image": image, "title":m.title, "text":m.text})

    return render_template('home.html', sliders_home=sliders, about=about, clients=clients, clients_text=clients_text, news=news, contact=contact, methods=methods)





@app.route('/form', methods=["POST"])
def FormContact():   

     if request.method == 'POST':
                
        mail_msg = Message("Moondu: Novo contato", recipients=['anabgiacometti@gmail.com', 'contato@moondu.com.br'])

        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']

        mail_msg.html = render_template('email/contato.html', name = name, phone = phone, email = email, message = message)
        mail.send(mail_msg)
        
        msg = "Sua mensagem foi enviada! Logo entraremos em contato :)"
        category = "success"

        resp = {'feedback': msg, 'category': category}
        return make_response(jsonify(resp), 200)

