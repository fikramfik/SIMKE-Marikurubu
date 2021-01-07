from flask import Flask, render_template, redirect, url_for, Blueprint, flash, request
from SIMKe.admin.forms import pendaftaranAdmin, pendaftaranWarga, tambahDataProfile, tambahDataGDS, tambahDataMedia


radmin = Blueprint('radmin',__name__)

@radmin.route("/login-admin")
def loginAdmin():
    return render_template("login_admin.html")

@radmin.route("/admin-home")
def adminHome():
    return render_template("admin_home.html")

@radmin.route("/admin-profile")
def adminProfile():
    return render_template("admin_profile.html")

@radmin.route("/admin-settings")
def adminSettings():
    return render_template("admin_settings.html")

@radmin.route("/pendaftaran-akun-admin", methods=['GET', 'POST'])
def adminPendaftaranAkunAdmin():
    form = pendaftaranAdmin()
    if form.validate_on_submit():
        flash(f'Akun - {form.email.data} berhasil daftar','warning')
        return redirect(url_for('radmin.adminPendaftaranAkunAdmin'))
    return render_template("pendaftaran_akun_admin.html", form=form)

@radmin.route("/pendaftaran-akun-warga", methods=['GET', 'POST'])
def adminPendaftaranAkunWarga():
    form = pendaftaranWarga()
    if form.validate_on_submit():
        flash(f'Akun - {form.nik.data} berhasil daftar','warning')
        return redirect(url_for('radmin.adminPendaftaranAkunWarga'))
    return render_template("pendaftaran_akun_warga.html", form=form)

@radmin.route("/edit-akun-admin")
def adminEditAkunAdmin():
    return render_template("edit_akun_admin.html")

@radmin.route("/edit-akun-warga")
def adminEditAkunWarga():
    return render_template("edit_akun_warga.html")

@radmin.route("/tambah-data-profile", methods=['GET', 'POST'])
def adminTambahDataProfile():
    form = tambahDataProfile()
    if form.validate_on_submit():
        flash(f'Data Profile Berhasil ditambahkan','warning')
        return redirect(url_for('radmin.adminTambahDataProfile'))
    return render_template("tambah_data_profile.html", form=form)

@radmin.route("/tambah-data-gds", methods=['GET', 'POST'])
def adminTambahDataGds():
    form = tambahDataGDS()
    if form.validate_on_submit():
        flash(f'Data GDS Berhasil ditambahkan','warning')
        return redirect(url_for('radmin.adminTambahDataGds'))
    return render_template("tambah_data_gds.html", form=form)

@radmin.route("/tambah-data-media", methods=['GET', 'POST'])
def adminTambahDataMedia():
    form = tambahDataMedia()
    if form.validate_on_submit():
        flash(f'Data Media Berhasil ditambahkan','warning')
        return redirect(url_for('radmin.adminTambahDataMedia'))
    return render_template("tambah_data_media.html", form=form)

@radmin.route("/edit-data-profile")
def adminEditDataProfile():
    return render_template("edit_data_profile.html")

@radmin.route("/edit-data-gds")
def adminEditDataGds():
    return render_template("edit_data_gds.html")

@radmin.route("/edit-data-media")
def adminEditDataMedia():
    return render_template("edit_data_media.html")

@radmin.route("/pelayanan-sktm")
def adminPelayananSktm():
    return render_template("pelayanan_sktm.html")

@radmin.route("/pelayanan-skbm")
def adminPelayananSkbm():
    return render_template("pelayanan_skbm.html")