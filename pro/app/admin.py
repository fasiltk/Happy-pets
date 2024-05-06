from django.contrib import admin
from .models import Users,Pets,Buy,Confirm,ChatUser,ChatManager

# Register your models here.
admin.site.register(Users)
admin.site.register(Pets)
admin.site.register(Buy)
admin.site.register(Confirm)
admin.site.register(ChatUser)
admin.site.register(ChatManager)
