from django.urls import path

from . import views

# path()コールを追加して新しいViewをpolls.urlsモジュールと結びつける
# URLConfに名前空間を追加する
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
