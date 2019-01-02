from django.contrib import admin
from repository import models

for item in models.__all__:
    admin.site.register(getattr(models, item))
