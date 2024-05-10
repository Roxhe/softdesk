from rest_framework.permissions import BasePermission
from .models import Contributor, Issue
from django.shortcuts import get_object_or_404


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsProjectAuthor(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('pk')
        is_contributor = request.user.contributions.filter(project_id=project_id).exists()
        return bool(is_contributor)


class IsIssueContributor(BasePermission):
    def has_permission(self, request, view):
        issue_id = view.kwargs.get('pk')
        if issue_id:
            issue = get_object_or_404(Issue, pk=issue_id)
            is_author = request.user == issue.author
            is_other_contributor = request.user in issue.other_contributors.all()
            return is_author or is_other_contributor
        return False
