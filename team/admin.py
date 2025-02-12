from django.contrib import admin

from .models import *

admin.site.register(User) 
admin.site.register(UIDesigners)
admin.site.register(Developers)
admin.site.register(SocialMedia)
admin.site.register(Account)
admin.site.register(Client)
admin.site.register(Projects)
admin.site.register(Invoice)