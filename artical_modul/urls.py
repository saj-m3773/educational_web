from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_list'),
    re_path(r'tag/(?P<tags>[-\w+])', views.ArticlesListView.as_view(), name='articles-tag-list'),
    path('<pk>/', views.ArticleDetailView.as_view(), name='articles_detail'),
    path('add_articale_comment', views.add_article_comment, name='add_article_comment')
]
