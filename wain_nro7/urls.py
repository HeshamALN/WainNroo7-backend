"""wain_nro7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wain_nro7_app.views import UserCreateAPIView, MapListView, DiffView, TriviaView, RiddleView, ProfileAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('maplist/', MapListView.as_view(), name='map-list'),
    path('diffs/<int:diff_id>/', DiffView.as_view(), name='diff-game'),
    path('trivia/<int:trivia_id>/', TriviaView.as_view(), name='trivia-game'),
    path('riddle/<int:riddle_id>/', RiddleView.as_view(), name='riddle-game'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    # path('gameslist/', GamesListfoView.as_view(), name='games-list'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


	