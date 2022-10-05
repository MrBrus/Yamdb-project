from django.urls import include, path
from rest_framework.routers import SimpleRouter
from api.v1.views import (

    UsersViewSet,
    APIGetToken,
    APISignup,
    ReviewViewSet,
    CommentViewSet,
    TitleViewSet,
    CategoryViewSet,
    GenreViewSet
)
app_name = 'api'
API_V1 = 'v1/'

router_v1 = SimpleRouter()
router_v1.register(
    'users',
    UsersViewSet,
    basename='users'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('titles', TitleViewSet, basename='title')
router_v1.register('categories', CategoryViewSet,
                   basename='category')
router_v1.register('genres', GenreViewSet, basename='genre')

auth_urls = [
    path('signup/', APISignup.as_view(), name='signup'),
    path('token/', APIGetToken.as_view(), name='get_token'),
]
urlpatterns = [
    path(API_V1 + 'auth/', include(auth_urls)),
    path(API_V1, include(router_v1.urls)),
]
