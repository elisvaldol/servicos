from django.contrib import admin
from .models import servicos
from .models import cliente

admin.site.register(servicos)
admin.site.register(cliente)