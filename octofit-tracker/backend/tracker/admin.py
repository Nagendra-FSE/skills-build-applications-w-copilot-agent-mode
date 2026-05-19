from django.contrib import admin
from .models import Activity, LeaderboardEntry, Profile, Team, WorkoutSuggestion


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_name', 'experience_level', 'created_at']
    search_fields = ['user__username', 'display_name', 'location']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration_minutes', 'calories_burned', 'timestamp']
    list_filter = ['activity_type']
    search_fields = ['user__username', 'notes']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'recommended_duration_minutes']
    search_fields = ['title', 'target_muscle_groups']


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_points', 'rank', 'updated_at']
    search_fields = ['user__username']
