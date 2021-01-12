from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from SIMKe.models import Tadmin, Twarga, Tskbm, Tsktm, Tprofile, Tdatagds, Tmedia
from flask_login import current_user

class floginAdmin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class pendaftaranAdmin(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

    # cek validation email
    def validate_email(self, email):
        cekemail=Tadmin.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError('EMAIL Sudah Terdaftar, Gunakan EMAIL lain!')

class pendaftaranWarga(FlaskForm):
    nik = StringField('NIK', validators=[DataRequired(),Length(16)])
    nama = StringField('Nama', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Daftar')

    # cek validation nik
    def validate_nik(self, nik):
        ceknik=Twarga.query.filter_by(nik=nik.data).first()
        if ceknik:
            raise ValidationError('NIK Sudah Terdaftar, Gunakan NIK lain!')

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

class editAkunAdmin(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    foto= FileField('Ubah Foto Profile', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Simpan')

    # cek validation email
    def validate_npm(self, email):
        if email.data != current_user.email:
            cekemail=Tadmin.query.filter_by(email=email.data).first()
            if ceknpm:
                raise ValidationError('EMAIL Sudah Terdaftar, Gunakan EMAIL yang lain')

class editPassAdmin(FlaskForm):
    password = PasswordField('Password Baru', validators=[DataRequired(),Length(min=6, max=20)])
    konf_pass = PasswordField('Konfirmasi Password Baru', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Simpan')