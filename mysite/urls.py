from django.contrib import admin
from django.urls import include, path

# polls.urlsモジュールの記述を反映させる

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
