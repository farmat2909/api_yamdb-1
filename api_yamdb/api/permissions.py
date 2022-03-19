from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorOrAuthenticatedReadOnly(BasePermission):
    """
    Права доступа для автора и аутентифицированного пользователя.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    """
    Права доступа для админа и только для чтения.
    """
    def has_permission(self, request, view):
        user = request.user
        return (
            request.method in SAFE_METHODS
            or (
                user.is_authenticated and user.is_admin()
            )
        )


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and (request.user.is_staff or request.user.role == 'admin')
                )
