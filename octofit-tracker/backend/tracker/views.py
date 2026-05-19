from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Activity, LeaderboardEntry, Profile, Team, WorkoutSuggestion
from .serializers import (
    ActivitySerializer,
    LeaderboardEntrySerializer,
    ProfileSerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSuggestionSerializer,
)


@api_view(['GET'])
def api_root(request):
    return Response({
        'profiles': request.build_absolute_uri('/api/profiles/'),
        'activities': request.build_absolute_uri('/api/activities/'),
        'teams': request.build_absolute_uri('/api/teams/'),
        'workouts': request.build_absolute_uri('/api/workouts/'),
        'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
        'users': request.build_absolute_uri('/api/users/'),
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related('user').all().order_by('-timestamp')
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related('members').all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all().order_by('-created_at')
    serializer_class = WorkoutSuggestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.select_related('user').all()
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
