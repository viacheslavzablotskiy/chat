from django.contrib import admin
from django.urls import path, include, re_path
from chat_with_people import views
from chat_with_people import consumers
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('dj_rest_auth.urls')),
    path("", include("chat_with_people.urls")),
    path('api/log/', include("rest_framework.urls")),
    # path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('start/', views.start_convo, name='start_convo'),
    # path('<int:convo_id>/', views.get_conversation, name='get_conversation'),
    # path('stone', views.conversations, name='conversations'),
    # path('', views.user_list, name='user_list'),

]
