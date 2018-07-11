from django.contrib import admin
from .models import *

admin.site.register(Port)
admin.site.register(Interface)
admin.site.register(InterfaceVlan)
admin.site.register(LoopBack)
admin.site.register(Device)
admin.site.register(Topology)
admin.site.register(Link)
admin.site.register(SubInterface)
