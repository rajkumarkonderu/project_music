import datetime
from projectmusic.models import Song,Audiobook,Podcast

class ModelFactory():

    def get_model(self,type):
        self.type = type
        if self.type == 'song':
            return Song()
        elif self.type == 'audiobook':
            return Audiobook()
        elif self.type == 'podcast':
            return Podcast()
    
    def get_model(self,type,**data):
        self.type = type
        if self.type == 'song':
                return Song(**data)
        elif self.type == 'audiobook':
                return Audiobook(**data)
        elif self.type == 'podcast':
                return Podcast(**data)

class UpdateFactory():
    
    def get_object(self,type):
        self.type = type
        if self.type == 'song':
            return UpdateSong()
        elif self.type == 'audiobook':
            return UpdateAudiobook()
        elif self.type == 'podcast':
            return UpdatePodcast()

class UpdateSong():
    def update(self,instance,data):
        instance.name = data.get('name',instance.name)
        instance.duration = data.get('duration',instance.duration)
        instance.uploaded_time = datetime.datetime.now()

class UpdatePodcast():
    def update(self,instance,data):
        instance.name = data.get('name',instance.name)
        instance.duration = data.get('duration',instance.duration)
        instance.uploaded_time = datetime.datetime.now()
        instance.host = data.get('host',instance.host)
        instance.participants = data.get('participants',instance.participants)

class UpdateAudiobook():
    def update(self,instance,data):
        instance.title = data.get('title',instance.title)
        instance.narrator = data.get('narrator',instance.narrator)
        instance.duration = data.get('duration',instance.duration)
        instance.uploaded_time = datetime.datetime.now()


