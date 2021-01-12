from flask import Flask, render_template, redirect, url_for, Blueprint, flash, request
from SIMKe.admin.forms import pendaftaranAdmin, pendaftaranWarga, tambahDataProfile, tambahDataGDS, tambahDataMedia, floginAdmin
from SIMKe.models import Tadmin, Twarga, Tskbm, Tsktm, Tprofile, Tdatagds, Tmedia
from SIMKe import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


radmin = Blueprint('radmin',__name__)

@radmin.route("/login-admin", methods=['GET', 'POST'])
def loginAdmin():
    if current_user.is_authenticated:
        return redirect(url_for('radmin.loginAdmin'))
    form=floginAdmin()
    if form.validate_on_submit():
        cekemail=Tadmin.query.filter_by(email=form.email.data).first()
        if cekemail and bcrypt.check_password_hash(cekemail.password, form.password.data):
            login_user(cekemail)
            flash('Selamat Datang', 'warning')
            return redirect(url_for('radmin.adminHome'))
        else:
            flash('Login Gagal, periksa EMAIL dan Password kembali!', 'danger')
    return render_template("login_admin.html", form=form)

@radmin.route("/admin-home")
@login_required
def adminHome():
    return render_template("admin_home.html")

@radmin.route("/logout-admin")
def logoutAdmin():
    logout_user()
    return redirect(url_for('radmin.loginAdmin'))

@radmin.route("/admin-profile")
@login_required
def adminProfile():
    return render_template("admin_profile.html")

@radmin.route("/admin-settings")
@login_required
def adminSettings():
    return render_template("admin_settings.html")

@radmin.route("/pendaftaran-akun-admin", methods=['GET', 'POST'])
@login_required
def adminPendaftaranAkunAdmin():
    form = pendaftaranAdmin()
    if form.validate_on_submit():
        pass_hash=bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        add_admin=Tadmin(nama=form.nama.data, email=form.email.data, password=pass_hash)
        db.session.add(add_admin)
        db.session.commit()
        flash(f'Akun - {form.email.data} berhasil daftar, silahkan Login !!!','dark')
        return redirect(url_for('radmin.adminPendaftaranAkunAdmin'))
    return render_template("pendaftaran_akun_admin.html", form=form)

@radmin.route("/pendaftaran-akun-warga", methods=['GET', 'POST'])
@login_required
def adminPendaftaranAkunWarga():
    form = pendaftaranWarga()
    if form.validate_on_submit():
        pass_hash=bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        add_warga=Twarga(nik=form.nik.data, nama=form.nama.data, password=pass_hash)
        db.session.add(add_warga)
        db.session.commit()
        flash(f'Akun - {form.nik.data} berhasil daftar','warning')
        return redirect(url_for('radmin.adminPendaftaranAkunWarga'))
    return render_template("pendaftaran_akun_warga.html", form=form)

@radmin.route("/edit-akun-admin")
@login_required
def adminEditAkunAdmin():
    return render_template("edit_akun_admin.html")

@radmin.route("/edit-akun-warga")
@login_required
def adminEditAkunWarga():
    return render_template("edit_akun_warga.html")

@radmin.route("/tambah-data-profile", methods=['GET', 'POST'])
@login_required
def adminTambahDataProfile():
    form = tambahDataProfile()
    if form.validate_on_submit():
        add_dataprofile=Tprofile(sambutan=form.sambutan.data, sejarah=form.sejarah.data, visimisi=form.visimisi.data)
        db.session.add(add_dataprofile)
        db.session.commit()
        flash(f'Data Profile Berhasil ditambahkan','warning')
        return redirect(url_for('radmin.adminTambahDataProfile'))
    return render_template("tambah_data_profile.html", form=form)

@radmin.route("/tambah-data-gds", methods=['GET', 'POST'])
@login_required
def adminTambahDataGds():
    form = tambahDataGDS()
    if form.validate_on_submit():
        add_datagds=Tdatagds(geografi=form.geografi.data, demografi=form.demografi.data, sosial=form.sosial.data)
        db.session.add(add_datagds)
        db.session.commit()
        flash(f'Data GDS Berhasil ditambahkan','warning')
        return redirect(url_for('radmin.adminTambahDataGds'))
    return render_template("tambah_data_gds.html", form=form)

@radmin.route("/tambah-data-media", methods=['GET', 'POST'])
@login_required
def adminTambahDataMedia():
    form = tambahDataMedia()
    if form.validate_on_submit():
        add_datamedia=Tmedia(judul=form.judul.data, deskripsi=form.deskripsi.data, foto=form.foto.data)
        db.session.add(add_datamedia)
        db.session.commit()
        flash(f'Data Media Berhasil ditambahkan','warning')
        return redirect(url_for('radmin.adminTambahDataMedia'))
    return render_template("tambah_data_media.html", form=form)

@radmin.route("/edit-data-profile")
@login_required
def adminEditDataProfile():
    return render_template("edit_data_profile.html")

@radmin.route("/edit-data-gds")
@login_required
def adminEditDataGds():
    return render_template("edit_data_gds.html")

@radmin.route("/edit-data-media")
@login_required
def adminEditDataMedia():
    return render_template("edit_data_media.html")

@radmin.route("/pelayanan-sktm")
@login_required
def adminPelayananSktm():
    return render_template("pelayanan_sktm.html")

@radmin.route("/pelayanan-skbm")
@login_required
def adminPelayananSkbm():
    return render_template("pelayanan_skbm.html")