from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

class pendaftaranAdmin(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

class pendaftaranWarga(FlaskForm):
    nik = StringField('NIK', validators=[DataRequired(),Length(16)])
    nama = StringField('Nama', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

class tambahDataProfile(FlaskForm):
    sambutan = TextAreaField('Sambutan', validators=[DataRequired()])
    sejarah = TextAreaField('Sejarah', validators=[DataRequired()])
    visimisi = TextAreaField('Visi Misi', validators=[DataRequired()])
    submit = SubmitField('Tambah')

class tambahDataGDS(FlaskForm):
    geografi = TextAreaField('Geografi', validators=[DataRequired()])
    demografi = TextAreaField('Demografi', validators=[DataRequired()])
    sosial = TextAreaField('Sosial', validators=[DataRequired()])
    submit = SubmitField('Tambah')

class tambahDataMedia(FlaskForm):
    judul = StringField('Judul', validators=[DataRequired()])
    deskripsi = TextAreaField('Deskripsi', validators=[DataRequired()])
    foto = FileField('Foto', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Tambah')