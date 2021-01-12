from datetime import datetime
from SIMKe import db


class Tadmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    foto = db.Column(db.String(30), nullable=False, default='default.jpg')
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Tadmin('{self.nama}','{self.email}','{self.foto}','{self.password}')"

class Twarga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nik = db.Column(db.String(16), unique=True, nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    ttl = db.Column(db.String(30), nullable=False, default='-')
    jk = db.Column(db.String(20), nullable=False, default='-')
    gd = db.Column(db.String(20), nullable=False, default='-')
    alamat = db.Column(db.String(100), nullable=False, default='-')
    agama = db.Column(db.String(30), nullable=False, default='-')
    email = db.Column(db.String(50), unique=True, nullable=False, default='-')
    notlp = db.Column(db.String(13), unique=True, nullable=False, default='-')
    sp = db.Column(db.String(20), nullable=False, default='-')
    pekerjaan = db.Column(db.String(50), nullable=False, default='-')
    kewarganegaraan = db.Column(db.String(20), nullable=False, default='-')
    foto = db.Column(db.String(30), nullable=False, default='default.jpg')
    password = db.Column(db.String(80), nullable=False)
    sktms = db.relationship('Tsktm', backref='warga', lazy=True)
    skbms = db.relationship('Tskbm', backref='warga', lazy=True)

    def __repr__(self):
        return f"Twarga('{self.nik}','{self.nama}','{self.ttl}','{self.jk}','{self.gd}','{self.alamat}','{self.alamat}','{self.agama}','{self.email}','{self.notlp}','{self.sp}','{self.pekerjaan}','{self.kewarganegaraan}','{self.foto}','{self.password}')"

class Tsktm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namaortu = db.Column(db.String(50), nullable=False)
    ttlortu = db.Column(db.String(30), nullable=False)
    jkortu = db.Column(db.String(20), nullable=False)
    statusortu = db.Column(db.String(20), nullable=False)
    agamaortu = db.Column(db.String(30), nullable=False)
    pekerjaanortu = db.Column(db.String(50), nullable=False)
    alamatortu = db.Column(db.String(100), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    warga_id = db.Column(db.Integer, db.ForeignKey('twarga.id'))

    def __repr__(self):
        return f"Tsktm('{self.namaortu}','{self.ttlortu}','{self.jkortu}','{self.statusortu}','{self.agamaortu}','{self.pekerjaanortu}','{self.alamatortu}','{self.tgl_post}')"

class Tskbm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    warga_id = db.Column(db.Integer, db.ForeignKey('twarga.id'))
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Tsktm('{self.tgl_post}')"

class Tprofile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sambutan = db.Column(db.String(200), nullable=False)
    sejarah = db.Column(db.String(200), nullable=False)
    visimisi = db.Column(db.String(200), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Tsktm('{self.sambutan}','{self.sejarah}','{self.visimisi}','{self.tgl_post}')"

class Tdatagds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    geografi = db.Column(db.String(200), nullable=False)
    demografi = db.Column(db.String(200), nullable=False)
    sosial = db.Column(db.String(200), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Tsktm('{self.geografi}','{self.demografi}','{self.sosial}','{self.tgl_post}')"

class Tmedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.String(200), nullable=False)
    foto = db.Column(db.String(30), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Tsktm('{self.judul}','{self.deskripsi}','{self.foto}','{self.tgl_post}')"