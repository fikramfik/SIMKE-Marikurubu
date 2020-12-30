from flask import Flask, render_template, redirect, url_for, Blueprint, flash, request


ruser = Blueprint('ruser',__name__)

@ruser.route("/")
def home():
    return render_template("home.html")

@ruser.route("/akses-login")
def aksesLogin():
    return render_template("akses_login.html")

@ruser.route("/login-warga")
def loginWarga():
    return render_template("login_warga.html")

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

