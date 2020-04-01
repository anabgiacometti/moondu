from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FileField, HiddenField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField
from wtf_tinymce.forms.fields import TinyMceField


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[InputRequired('Preencha este campo.')])
    password = PasswordField('Senha', validators=[InputRequired('Preencha este campo.')])

class HomeForm(FlaskForm):
    active_1 = BooleanField('Ativo')
    title_1 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    video_1 = StringField('Vídeo')
    text_1 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    active_2 = BooleanField('Ativo')
    title_2 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    video_2 = StringField('Vídeo')
    text_2 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    active_3 = BooleanField('Ativo')
    title_3 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    video_3 = StringField('Vídeo')
    text_3 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )


class NewsForm(FlaskForm):
    title_1 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_1 = StringField('Vídeo')
    text_1 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    title_2 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_2 = StringField('Vídeo')
    text_2 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    title_3 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_3 = StringField('Vídeo')
    text_3 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    
class AboutUsForm(FlaskForm):
    title = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    video = StringField('Vídeo')
    text = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

class ClientForm(FlaskForm):
    logo = FileField()

    
class ClientPhraseForm(FlaskForm):
    text1 =  StringField('Titulo #1')
    text2 =  StringField('Titulo #2')
    text3 =  StringField('Titulo #3')
    text4 =  StringField('Titulo #4')
    text5 =  StringField('Titulo #5')
    id = HiddenField()


class ContactForm(FlaskForm):
    phone_1 =  StringField('Telefone #1')
    phone_2 =  StringField('Telefone #2')
    address_1 =  StringField('Endereço #1')
    address_2 =  StringField('Endereço #2')
    email =  StringField('E-mail')
    facebook =  StringField('Facebook')
    whatsapp =  StringField('Whatsapp')
    instagram =  StringField('Instagram')
    linkedIn =  StringField('LinkedIn')
    blog =  StringField('Blog')
    areaCliente =  StringField('Área do Cliente')

    senderEmail =  StringField('E-mail')
    senderPassword =  PasswordField('Senha')
    senderProvider =  StringField('Provedor')

class MethodForm(FlaskForm):
    title_1 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_1 = FileField()
    text_1 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    title_2 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_2 = FileField()
    text_2 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    title_3 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_3 = FileField()
    text_3 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    title_4 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_4 = FileField()
    text_4 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    title_5 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_5 = FileField()
    text_5 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )

    title_6 = StringField('Título', validators=[InputRequired('Preencha este campo.')])
    image_6 = FileField()
    text_6 = TinyMceField(
        'Texto',
        tinymce_options={'toolbar': 'bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | link | code', 'height': "150"}
    )
