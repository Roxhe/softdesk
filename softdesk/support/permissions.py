from rest_framework.permissions import BasePermission


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class IsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsContributor(BasePermission):

    def has_permission(self, request, view):
        project_id = view.kwargs.get('pk')
        is_contributor = request.user.contributions.filter(project_id=project_id).exists()
        return bool(is_contributor)

