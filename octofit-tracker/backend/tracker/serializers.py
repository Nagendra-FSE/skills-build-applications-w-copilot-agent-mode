from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Activity, LeaderboardEntry, Profile, Team, WorkoutSuggestion


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)
    user_id = serializers.CharField(source='user.pk', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'user_id',
            'display_name',
            'bio',
            'location',
            'experience_level',
            'avatar_url',
            'created_at',
        ]


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)
    user_id = serializers.CharField(source='user.pk', read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'user_id',
            'activity_type',
            'duration_minutes',
            'distance_km',
            'calories_burned',
            'notes',
            'timestamp',
        ]


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)
    members = UserSerializer(many=True, read_only=True)
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(),
        source='members',
        write_only=True,
        required=False,
    )

    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'description',
            'members',
            'member_ids',
            'created_at',
        ]


class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        model = WorkoutSuggestion
        fields = [
            'id',
            'title',
            'description',
            'difficulty',
            'target_muscle_groups',
            'recommended_duration_minutes',
            'created_at',
        ]


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.CharField(source='user.pk', read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = [
            'id',
            'user',
            'user_id',
            'total_points',
            'rank',
            'updated_at',
        ]
