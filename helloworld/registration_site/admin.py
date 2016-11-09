from django.contrib import admin
<<<<<<< HEAD
from registration_site.models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Location)
admin.site.register(Piece)
admin.site.register(Performer)
admin.site.register(Profile)

=======
from .models import (
	Piece,
	Parent,
	Teacher,
	Performer,
	Profile,
)

admin.site.register(Piece)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Performer)
admin.site.register(Profile)
>>>>>>> d1a9b281c064460c4143b2b4ffa86a09340a8b9d
