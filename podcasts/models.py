from django.db import models
from django.db.models.fields import CharField, URLField
from  embed_video.fields  import  EmbedVideoField

class Item(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    video= EmbedVideoField(default='SOME STRING')
    

