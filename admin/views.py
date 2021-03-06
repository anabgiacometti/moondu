from app import app, db, mail
from flask import render_template, redirect, url_for, request, abort, session
from flask_mail import Message
import random, string
from base64 import b64encode


from .models import User, SlidersHome, AboutUs, Client, ClientPhrases, News, Contact, Methods
from .forms import LoginForm, HomeForm, AboutUsForm, ClientForm, ClientPhraseForm, NewsForm, ContactForm, MethodForm, UserForm

@app.route('/admin', methods=["GET", "POST"])
def Login():   

    form = LoginForm()
    message = None

    if 'message' in session:
        message = session['message']
        session['message'] = None

    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if not user:
            form.username.errors.append('Usuário não encontrado.')
        
        elif form.password.data != user.password:
            form.password.errors.append('Senha incorreta.')

        else:
            session['username'] = user.username
            return redirect(url_for('Dashboard'))

    return render_template('admin/login.html', form=form, message_pass=message, Login=True)



@app.route('/admin/dashboard', methods=["GET"])
def Dashboard():   
    if 'username' not in session or session['username'] == None:
        return redirect(url_for('Admin'))

    return render_template('admin/dashboard.html')



@app.route('/logout')
def Logout():
    session.clear()
    return redirect(url_for('Login'))


def randomString(stringLength=4):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def sendMail(title, name, username, senha, email):
    msg = Message("Moondu: {}".format(title), recipients=[email])

    if title == "Recuperação de senha": 
        template = "email/recoverpass.html"
    else:
        template = "email/newuser.html"

    msg.html = render_template(template, name = name, username = username, senha = senha)
    mail.send(msg)


@app.route('/recoverpass/<username>')
def RecoverPass(username):
    random = randomString()
    user = User.query.filter(User.username == username).first()
    
    if not user:
        session['message'] = "Username não encontrado."

    else:
        name = user.username
        user.password = "{}{}".format(name, random)
        db.session.commit()
        sendMail("Recuperação de senha", user.name, user.username, user.password, user.email)
        session['message'] = "Uma nova senha foi encaminhada à seu e-mail."

    return redirect(url_for('Login'))



@app.route('/admin/home', methods=["POST", "GET"])
def AdminHome():
    form = HomeForm()

    if request.method == "POST" and form.validate_on_submit():
        
        slider1 = SlidersHome.query.filter(SlidersHome.id == 1).first()
        slider2 = SlidersHome.query.filter(SlidersHome.id == 2).first()
        slider3 = SlidersHome.query.filter(SlidersHome.id == 3).first()

        if slider1 == None:
            slider1 = SlidersHome(
                id = 1, 
                title = form.title_1.data, 
                text = form.text_1.data, 
                active = form.active_1.data, 
                video = form.video_1.data
            )

            db.session.add(slider1)
            db.session.commit()

        else:
            slider1.title = form.title_1.data
            slider1.text = form.text_1.data
            slider1.video = form.video_1.data
            slider1.active = form.active_1.data
            db.session.commit()

        if slider2 == None:
            slider2 = SlidersHome(
                id = 2, 
                title = form.title_2.data, 
                text = form.text_2.data, 
                active = form.active_2.data, 
                video = form.video_2.data
            )

            db.session.add(slider2)
            db.session.commit()
        
        else:
            slider2.title = form.title_2.data
            slider2.text = form.text_2.data
            slider2.video = form.video_2.data
            slider2.active = form.active_2.data
            db.session.commit()

        if slider3 == None:
            slider3 = SlidersHome(
                id = 3, 
                title = form.title_3.data, 
                text = form.text_3.data, 
                active = form.active_3.data, 
                video = form.video_3.data
            )

            db.session.add(slider3)
            db.session.commit()

        else:
            slider3.title = form.title_3.data
            slider3.text = form.text_3.data
            slider3.video = form.video_3.data
            slider3.active = form.active_3.data
            db.session.commit()

    else: 
        slider1 = SlidersHome.query.filter(SlidersHome.id == 1).first()
        slider2 = SlidersHome.query.filter(SlidersHome.id == 2).first()
        slider3 = SlidersHome.query.filter(SlidersHome.id == 3).first()

        if(slider1 != None):
            form.active_1.data = slider1.active
            form.text_1.data = slider1.text
            form.title_1.data = slider1.title
            form.video_1.data = slider1.video

        if(slider2 != None):
            form.active_2.data = slider2.active
            form.text_2.data = slider2.text
            form.title_2.data = slider2.title
            form.video_2.data = slider2.video

        if(slider3 != None):
            form.active_3.data = slider3.active
            form.text_3.data = slider3.text
            form.title_3.data = slider3.title
            form.video_3.data = slider3.video
        

    return render_template('admin/home.html', form=form)
    

@app.route('/admin/about', methods=["POST", "GET"])
def AdminAbout():
    form = AboutUsForm()

    if request.method == "POST" and form.validate_on_submit():
        
        about = AboutUs.query.filter(AboutUs.id == 1).first()

        if about == None:
            about = AboutUs(
                id = 1, 
                title = form.title.data, 
                text = form.text.data, 
                video = form.video.data
            )

            db.session.add(about)
            db.session.commit()

        else:
            about.title = form.title.data
            about.text = form.text.data
            about.video = form.video.data
            db.session.commit()
    else: 
        about = AboutUs.query.filter(AboutUs.id == 1).first()

        if(about != None):
            form.text.data = about.text
            form.title.data = about.title
            form.video.data = about.video       

    return render_template('admin/about.html', form=form)
    




@app.route('/admin/clients', methods=["POST", "GET"])
def AdminClients():
    form = ClientForm()

    form_phrase = ClientPhraseForm()

    phrase1 =  ClientPhrases.query.filter(ClientPhrases.id == 1).first()
    phrase2 =  ClientPhrases.query.filter(ClientPhrases.id == 2).first()
    phrase3 =  ClientPhrases.query.filter(ClientPhrases.id == 3).first()
    phrase4 =  ClientPhrases.query.filter(ClientPhrases.id == 4).first()
    phrase5 =  ClientPhrases.query.filter(ClientPhrases.id == 5).first()

    clients = Client.query.all()

    images = []

    for c in clients:
        image = b64encode(c.logo).decode("utf-8")
        images.append({"image":image, "id":c.id})

    if request.method == "POST" and form.validate_on_submit():

        if(form_phrase.id.data == "1"):

            if phrase1 == None:
                phrase1 = ClientPhrases(
                    id = 1, 
                    text = form_phrase.text1.data
                )
                db.session.add(phrase1)
                db.session.commit()
            else:
                phrase1.text = form_phrase.text1.data
                db.session.commit()

            
            if phrase2 == None:
                phrase2 = ClientPhrases(
                    id = 2, 
                    text = form_phrase.text2.data
                )
                db.session.add(phrase2)
                db.session.commit()
            else:
                phrase2.text = form_phrase.text2.data
                db.session.commit()

            
            if phrase3 == None:
                phrase3 = ClientPhrases(
                    id = 3, 
                    text = form_phrase.text3.data
                )
                db.session.add(phrase3)
                db.session.commit()
            else:
                phrase3.text = form_phrase.text3.data
                db.session.commit()

            
            if phrase4 == None:
                phrase4 = ClientPhrases(
                    id = 4, 
                    text = form_phrase.text4.data
                )
                db.session.add(phrase4)
                db.session.commit()
            else:
                phrase4.text = form_phrase.text4.data
                db.session.commit()

            
            if phrase5 == None:
                phrase5 = ClientPhrases(
                    id = 5, 
                    text = form_phrase.text5.data
                )
                db.session.add(phrase5)
                db.session.commit()
            else:
                phrase5.text = form_phrase.text5.data
                db.session.commit()       

        else:
            if form.logo.data != None:
                client = Client(
                    logo=form.logo.data.read(),
                    name=form.logo.data.filename
                )
                db.session.add(client)
                db.session.commit()
 
            
        return redirect(url_for('AdminClients'))

    else:
        if phrase1 != None:
	        form_phrase.text1.data = phrase1.text
        if phrase2 != None:
            form_phrase.text2.data = phrase2.text
        if phrase3 != None:
            form_phrase.text3.data = phrase3.text
        if phrase4 != None:
            form_phrase.text4.data = phrase4.text
        if phrase5 != None:
            form_phrase.text5.data = phrase5.text

    return render_template('admin/clients.html', form=form, form_phrase=form_phrase, images=images)
    

@app.route('/delete-client/<id>')
def DeleteClient(id):
    cliente = Client.query.filter(Client.id == id).first()
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
    return redirect(url_for('AdminClients'))





@app.route('/admin/news', methods=["POST", "GET"])
def AdminNews():
    form = NewsForm()

    if request.method == "POST" and form.validate_on_submit():
        
        news1 = News.query.filter(News.id == 1).first()
        news2 = News.query.filter(News.id == 2).first()
        news3 = News.query.filter(News.id == 3).first()

        if news1 == None:
            news1 = News(
                id = 1, 
                title = form.title_1.data, 
                text = form.text_1.data, 
                image = form.image_1.data.read()
            )

            db.session.add(news1)
            db.session.commit()

        else:
            news1.title = form.title_1.data
            news1.text = form.text_1.data
            news1.image = form.image_1.data.read()
            db.session.commit()

        if news2 == None:
            news2 = News(
                id = 2, 
                title = form.title_2.data, 
                text = form.text_2.data, 
                image = form.image_2.data.read()
            )

            db.session.add(news2)
            db.session.commit()
        
        else:
            news2.title = form.title_2.data
            news2.text = form.text_2.data
            news2.image = form.image_2.data.read()
            db.session.commit()

        if news3 == None:
            news3 = News(
                id = 3, 
                title = form.title_3.data, 
                text = form.text_3.data, 
                image = form.image_3.data.read()
            )

            db.session.add(news3)
            db.session.commit()

        else:
            news3.title = form.title_3.data
            news3.text = form.text_3.data
            news3.image = form.image_3.data.read()
            db.session.commit()

    else: 
        news1 = News.query.filter(News.id == 1).first()
        news2 = News.query.filter(News.id == 2).first()
        news3 = News.query.filter(News.id == 3).first()

        if(news1 != None):
            form.text_1.data = news1.text
            form.title_1.data = news1.title
            form.image_1.data = news1.image

        if(news2 != None):
            form.text_2.data = news2.text
            form.title_2.data = news2.title
            form.image_2.data = news2.image

        if(news3 != None):
            form.text_3.data = news3.text
            form.title_3.data = news3.title
            form.image_3.data = news3.image
        

    return render_template('admin/news.html', form=form)
    


@app.route('/admin/contact', methods=["POST", "GET"])
def AdminContact():
    form = ContactForm()

    if request.method == "POST" and form.validate_on_submit():
        
        contact = Contact.query.filter(Contact.id == 1).first()

        if contact == None:
            contact = Contact(
                id = 1, 
                phone_1 = form.phone_1.data,
                phone_2 = form.phone_2.data, 
                address_1 = form.address_1.data, 
                address_2 = form.address_2.data, 
                email = form.email.data, 
                instagram = form.instagram.data, 
                whatsapp = form.whatsapp.data, 
                facebook = form.facebook.data, 
                linkdeIn = form.linkedIn.data, 
                blog = form.blog.data, 
                areaDoCliente = form.areaCliente.data                
            )

            db.session.add(contact)
            db.session.commit()

        else:
            contact.phone_1 = form.phone_1.data,
            contact.phone_2 = form.phone_2.data, 
            contact.address_1 = form.address_1.data, 
            contact.address_2 = form.address_2.data, 
            contact.email = form.email.data, 
            contact.instagram = form.instagram.data, 
            contact.whatsapp = form.whatsapp.data, 
            contact.facebook = form.facebook.data, 
            contact.linkdeIn = form.linkedIn.data, 
            contact.blog = form.blog.data, 
            contact.areaDoCliente = form.areaCliente.data                
            db.session.commit()
    else: 
        contact = Contact.query.filter(Contact.id == 1).first()

        if(contact != None):
            form.phone_1.data = contact.phone_1
            form.phone_2.data = contact.phone_2
            form.address_1.data = contact.address_1
            form.address_2.data = contact.address_2
            form.facebook.data = contact.facebook
            form.whatsapp.data = contact.whatsapp
            form.instagram.data = contact.instagram
            form.linkedIn.data = contact.linkdeIn
            form.areaCliente.data = contact.areaDoCliente
            form.blog.data = contact.blog
            form.email.data = contact.email

    return render_template('admin/contact.html', form=form)
    


@app.route('/admin/method', methods=["POST", "GET"])
def AdminMethod():
    form = MethodForm()

    if request.method == "POST" and form.validate_on_submit():
        
        m1 = Methods.query.filter(Methods.id == 1).first()
        m2 = Methods.query.filter(Methods.id == 2).first()
        m3 = Methods.query.filter(Methods.id == 3).first()
        m4 = Methods.query.filter(Methods.id == 4).first()
        m5 = Methods.query.filter(Methods.id == 5).first()
        m6 = Methods.query.filter(Methods.id == 6).first()

        if m1 == None:
            m1 = Methods(
                id = 1, 
                title = form.title_1.data, 
                text = form.text_1.data, 
                image = form.image_1.data.read()
            )

            db.session.add(m1)
            db.session.commit()

        else:
            m1.title = form.title_1.data
            m1.text = form.text_1.data
            if form.image_1.data.filename:
                m1.image = form.image_1.data.read()
            db.session.commit()

        if m2 == None:
            m2 = Methods(
                id = 2, 
                title = form.title_2.data, 
                text = form.text_2.data, 
                image = form.image_2.data.read()
            )

            db.session.add(m2)
            db.session.commit()
        
        else:
            m2.title = form.title_2.data
            m2.text = form.text_2.data
            if form.image_2.data.filename:
                m2.image = form.image_2.data.read()
            db.session.commit()

        if m3 == None:
            m3 = Methods(
                id = 3, 
                title = form.title_3.data, 
                text = form.text_3.data, 
                image = form.image_3.data.read()
            )

            db.session.add(m3)
            db.session.commit()

        else:
            m3.title = form.title_3.data
            m3.text = form.text_3.data
            if form.image_3.data.filename:
                m3.image = form.image_3.data.read()
            db.session.commit()

        if m4 == None:
            m4 = Methods(
                id = 4, 
                title = form.title_4.data, 
                text = form.text_4.data, 
                image = form.image_4.data.read()
            )

            db.session.add(m4)
            db.session.commit()

        else:
            m4.title = form.title_4.data
            m4.text = form.text_4.data
            if form.image_4.data.filename:
                m4.image = form.image_4.data.read()
            db.session.commit()

        if m5 == None:
            m5 = Methods(
                id = 5, 
                title = form.title_5.data, 
                text = form.text_5.data, 
                image = form.image_5.data.read()
            )

            db.session.add(m5)
            db.session.commit()
        
        else:
            m5.title = form.title_5.data
            m5.text = form.text_5.data
            if form.image_5.data.filename:
                m5.image = form.image_5.data.read()
            db.session.commit()

        if m6 == None:
            m6 = Methods(
                id = 6, 
                title = form.title_6.data, 
                text = form.text_6.data, 
                image = form.image_6.data.read()
            )

            db.session.add(m6)
            db.session.commit()

        else:
            m6.title = form.title_6.data
            m6.text = form.text_6.data
            if form.image_6.data.filename:
                m6.image = form.image_6.data.read()
            db.session.commit()

    else: 
        m1 = Methods.query.filter(Methods.id == 1).first()
        m2 = Methods.query.filter(Methods.id == 2).first()
        m3 = Methods.query.filter(Methods.id == 3).first()
        m4 = Methods.query.filter(Methods.id == 4).first()
        m5 = Methods.query.filter(Methods.id == 5).first()
        m6 = Methods.query.filter(Methods.id == 6).first()

        if(m1 != None):
            form.text_1.data = m1.text
            form.title_1.data = m1.title
            form.image_1.data = m1.image

        if(m2 != None):
            form.text_2.data = m2.text
            form.title_2.data = m2.title
            form.image_2.data = m2.image

        if(m3 != None):
            form.text_3.data = m3.text
            form.title_3.data = m3.title
            form.image_3.data = m3.image
        
        if(m4 != None):
            form.text_4.data = m4.text
            form.title_4.data = m4.title
            form.image_4.data = m4.image

        if(m5 != None):
            form.text_5.data = m5.text
            form.title_5.data = m5.title
            form.image_5.data = m5.image

        if(m6 != None):
            form.text_6.data = m6.text
            form.title_6.data = m6.title
            form.image_6.data = m6.image
            
    return render_template('admin/method.html', form=form)

@app.route('/admin/users', methods=['GET', 'POST'])
def AdminUsers():
    form = UserForm()
    cad = False

    if request.method == "POST" and form.validate_on_submit():
        user_duplicated = User.query.filter(User.username == form.username.data).first()
        
        if user_duplicated: 
            form.username.errors.append("Já existe um cadastro para este username")
            cad = True
        
        else: 
            senha = "{}{}".format(form.name.data.split(' ')[0], randomString())
            user = User(
                name = form.name.data, 
                username = form.username.data, 
                email = form.email.data, 
                password = senha
            )
            db.session.add(user)
            db.session.commit()        
            sendMail("Bem vindo!", user.name, user.username, senha, user.email)

    users = User.query.all()
    return render_template("admin/users.html", users=users, form=form, cad=cad)



@app.route('/delete-user/<id>')
def DeleteUser(id):
    user = User.query.filter(User.id == id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('AdminUsers'))