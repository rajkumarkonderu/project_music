from projectmusic import db
import datetime

class Song(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    duration = db.Column(db.Integer,nullable = False)
    uploaded_time = db.Column(db.DateTime,default = datetime.datetime.now())

    def __init__(self,name = None,duration = None, uploaded_time = None):
        self.name = name
        self.duration = duration
        self.uploaded_time = uploaded_time
    
    def __repr__(self):
        return f'Id = {self.id}\nName = {self.name}'

    def get_data(self):
        return f'Id = {self.id}\nName = {self.name}\nDuration = {self.duration}\nuploaded_time = {self.uploaded_time}'

class Podcast(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    duration = db.Column(db.Integer,nullable = False)
    uploaded_time = db.Column(db.DateTime,default = datetime.datetime.now())
    host = db.Column(db.String(100),nullable = False)
    participants = db.Column(db.PickleType)

    def __init__(self,name = None,duration = None,uploaded_time = None,host = None,participants = None):
        self.name = name
        self.duration = duration
        self.uploaded_time = uploaded_time
        self.host = host
        self.participants = participants

    def __repr__(self):
        return f'Id = {self.id}\nName = {self.name}'
    
    def get_data(self):
        return f'Id = {self.id}\nName = {self.name}\nDuration = {self.duration}\nuploaded_time = {self.uploaded_time}\nhost = {self.host}\nparticipants = {self.participants}'

class Audiobook(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    narrator = db.Column(db.String(100),nullable = False)
    duration = db.Column(db.Integer,nullable = False)
    uploaded_time = db.Column(db.DateTime,default = datetime.datetime.now())

    def __init__(self,title = None,narrator = None,duration = None,uploaded_time = None,):
        self.title = title
        self.narrator = narrator
        self.duration = duration
        self.uploaded_time = uploaded_time

    def __repr__(self):
        return f'Id = {self.id}\nName = {self.name}'
    
    def get_data(self):
        return f'Id = {self.id}\ntitle = {self.title}\nNarrator = {self.narrator}\nDuration = {self.duration}\nuploaded_time = {self.uploaded_time}'