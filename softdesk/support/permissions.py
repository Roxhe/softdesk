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
            # Utilisation de get_object_or_404 pour gérer proprement les cas où l'issue n'existe pas
            issue = get_object_or_404(Issue, pk=issue_id)
            # Vérifier si l'utilisateur est l'auteur
            is_author = request.user == issue.author
            # Vérifier si l'utilisateur est dans la liste des other_contributors
            is_other_contributor = request.user in issue.other_contributors.all()
            return is_author or is_other_contributor
        return False
