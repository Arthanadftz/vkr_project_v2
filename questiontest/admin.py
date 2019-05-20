from django.contrib import admin

# Register your models here.
from .models import Question, RK, RKResult #AnswersTest


admin.site.register(RK) #AnswersTest
admin.site.register(Question)
admin.site.register(RKResult)
