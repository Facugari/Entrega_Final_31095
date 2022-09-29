from django.contrib import admin
from .models import Item
from  embed_video.admin  import  AdminVideoMixin

class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Item, tutorialAdmin)

