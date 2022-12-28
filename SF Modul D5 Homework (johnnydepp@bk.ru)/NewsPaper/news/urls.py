from django.urls import path
from .views import PostList, PostSearch, PostDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
   path('', PostList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='new'),
   path('search/', PostSearch.as_view(), name='search'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('article/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_edit'),
   path('article/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
