from django.contrib import admin

# Register your models here.
from .models import Question, Choice
from django.utils import timezone
from django.utils.html import format_html

# Question admin modification
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # Görünən sütunlar
    list_filter = ['pub_date']
    search_fields = ['question_text']
    ordering = ['pub_date'] 

    def was_published_recently(self, obj):
        return obj.was_published_recently()
    was_published_recently.boolean = True  
    was_published_recently.short_description = 'Published recently?' 

# Choice admin modification
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question') 
    list_filter = ['question'] 
    search_fields = ['choice_text']  
    ordering = ['votes']  

    def question_text(self, obj):
        return obj.question.question_text
    question_text.short_description = 'Question'  


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)