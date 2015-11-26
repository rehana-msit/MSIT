from django.contrib import admin

from .models import Question,Choice,Sample,Book

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','pub_date')
    list_filter=['pub_date']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Sample)
admin.site.register(Book,BookAdmin)


