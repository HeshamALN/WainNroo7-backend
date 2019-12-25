from django.contrib import admin
from wain_nro7_app.models import Place, Questions, Answers, Trivia, Difference, Coordinate, Riddle#, Profile
# Register your models here.
admin.site.register(Place)
admin.site.register(Trivia)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Difference)
admin.site.register(Coordinate)
admin.site.register(Riddle)

# admin.site.register(Profile)
