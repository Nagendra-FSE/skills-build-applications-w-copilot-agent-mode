import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracker import views

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = 'http://localhost:8000'

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'workouts', views.WorkoutSuggestionViewSet)
router.register(r'leaderboard', views.LeaderboardEntryViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]
