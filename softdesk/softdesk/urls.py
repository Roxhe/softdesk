from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from support.views import UserViewSet, ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contributors', ContributorViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
