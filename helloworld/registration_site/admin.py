from django.contrib import admin
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