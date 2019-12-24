from django.contrib import admin
from wain_nro7_app.models import Place, Question, Answer, Trivia, Difference, Coordinate#, Profile
# Register your models here.
admin.site.register(Place)
admin.site.register(Trivia)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Difference)
admin.site.register(Coordinate)

# admin.site.register(Profile)
