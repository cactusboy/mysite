from django.urls import path
from . import views

app_name = 'polls'  # 加上命名空间目的是区别其他的app中的重名项目
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
