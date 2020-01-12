from django.contrib import admin
from .models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'dob', 'highest_qualification']
    list_display_links = ['id', 'user',]
    list_filter = ['highest_qualification']

