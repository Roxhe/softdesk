from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Project, Issue, Comment, Contributor
from .serializers import UserSerializer, ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAdminAuthenticated, IsAuthenticated, IsProjectAuthor, IsIssueContributor


class ProjectAuthorPermissionMixin(viewsets.GenericViewSet):

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsProjectAuthor]

        return [permission() for permission in permission_classes]


class IssueContributorPermissionMixin(viewsets.GenericViewSet):

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsIssueContributor]

        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminAuthenticated]


class ProjectViewSet(ProjectAuthorPermissionMixin, viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAdminAuthenticated]


class IssueViewSet(IssueContributorPermissionMixin, viewsets.ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(author=self.request.user)


class CommentViewSet(IssueContributorPermissionMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
