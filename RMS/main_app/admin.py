from django.contrib import admin
from main_app.models import UserInformation, Role, JobPost, InterviewScheduling, CandidateStatus, Skills, JobDesignation, AppliedJobs, SavedJobs

admin.site.site_title = 'RMS'
admin.site.site_header = 'RMS'
admin.site.index_title = "Recruitment Management System"

#this all date for only admin panel data customization

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_verified', 'created_at')
    list_display_links = ('id', 'username')
    list_filter = ('role', 'is_verified')
    search_fields = ('username', 'email')

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'mode', 'experience_year', 'experience_month', 'created_by', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('location', 'mode')
    search_fields = ('title',)

@admin.register(JobDesignation)
class JobDesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(AppliedJobs)
class AppliedJobsAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_post')
    list_display_links = ('user', 'job_post')

@admin.register(SavedJobs)
class SavedJobsAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_post')
    list_display_links = ('user', 'job_post')

@admin.register(InterviewScheduling)
class InterviewSchedulingAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_post', 'date_of_interview', 'mode', 'createdby', 'schedule_for', 'created_at')
    list_display_links = ('id', 'job_post')
    list_filter = ('mode', 'job_post')
    search_fields = ('job_post', 'schedule_for__username')

@admin.register(CandidateStatus)
class CandidateStatusAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'skills', 'experience', 'education')
    list_display_links = ('id', 'user', 'skills')
    search_fields = ('id', 'experience', 'education')
