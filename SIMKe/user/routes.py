from flask import Flask, render_template, redirect, url_for, Blueprint, flash, request
from SIMKe.user.forms import loginWarga
from SIMKe.models import Tadmin, Twarga, Tskbm, Tsktm, Tprofile, Tdatagds, Tmedia
from SIMKe import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import os
import secrets
from SIMKe import app
from PIL import Image

ruser = Blueprint('ruser',__name__)

@ruser.route("/")
def home():
    return render_template("home.html")

@ruser.route("/akses-login", methods=['GET', 'POST'])
def aksesLogin():
    if current_user.is_authenticated:
        return redirect(url_for('ruser.home'))
    form=loginWarga()
    if form.validate_on_submit():
        ceknik=Twarga.query.filter_by(nik=form.nik.data).first()
        if ceknik and bcrypt.check_password_hash(ceknik.password, form.password.data):
            login_user(ceknik)
            flash('Selamat Datang', 'warning')
            return redirect(url_for('ruser.home'))
        else:
            flash('Login Gagal, periksa NIK dan Password kembali!', 'danger')
    return render_template("akses_login.html", form=form)

@ruser.route("/logout-user")
def logoutUser():
    logout_user()
    return redirect(url_for('ruser.aksesLogin'))

@ruser.route("/profil-sambutan")
def pSambutan():
    return render_template("psambutan.html")

@ruser.route("/profil-sejarah")
def pSejarah():
    return render_template("psejarah.html")

@ruser.route("/profil-visimisi")
def pVisimisi():
    return render_template("pvisimisi.html")

@ruser.route("/data-geografi")
def dGeografi():
    return render_template("dgeografi.html")

@ruser.route("/data-demografi")
def dDemografi():
    return render_template("ddemografi.html")

@ruser.route("/data-sosial")
def dSosial():
    return render_template("dsosial.html")

@ruser.route("/media-galeri-foto")
def mFoto():
    return render_template("mfoto.html")

@ruser.route("/media-galeri-berita")
def mBerita():
    return render_template("mberita.html")

@ruser.route("/surat-online")
def suratOnline():
    return render_template("surat_online.html")

