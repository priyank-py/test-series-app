from django.contrib import admin
import nested_admin

from .models import QuestionPaper, Question, Option, QuestionImage


class OptionInline(nested_admin.NestedTabularInline):
    model = Option
    extra = 1
    # max_num = 5
    # min_num = 2

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [OptionInline,]

class QuestionPaperAdmin(nested_admin.NestedModelAdmin):
    list_display = ['id', 'subject', 'created_on']
    list_display_links = ['id', 'subject']
    list_filter = ['subject']
    inlines = [QuestionInline,]


@admin.register(QuestionImage)
class QuestionImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_on']
    list_display_links = ['id', 'subject']
    list_filter = ['subject']
    


admin.site.register(QuestionPaper, QuestionPaperAdmin)