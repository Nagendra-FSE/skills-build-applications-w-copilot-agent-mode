from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    experience_level = models.CharField(max_length=80, blank=True)
    avatar_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name or self.user.username


class Team(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('strength', 'Strength Training'),
        ('yoga', 'Yoga'),
        ('walking', 'Walking'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(default=0.0)
    calories_burned = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.activity_type} {self.duration_minutes}m"


class WorkoutSuggestion(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    difficulty = models.CharField(max_length=80, blank=True)
    target_muscle_groups = models.CharField(max_length=180, blank=True)
    recommended_duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    total_points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-total_points', 'rank']

    def __str__(self):
        return f"{self.user.username} ({self.total_points})"
