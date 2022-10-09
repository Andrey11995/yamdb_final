from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticated):
    """
    Полный доступ для авторизованного автора,
    Для остальных только чтение.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """
    Полный доступ для администратора,
    Для остальных только чтение.
    """
    def has_permission(self, request, view):
        return ((request.user.is_authenticated
                and request.user.is_admin())
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return ((request.user.is_authenticated
                and request.user.is_admin())
                or request.method in permissions.SAFE_METHODS)


class IsModeratorOrReadOnly(permissions.IsAdminUser):
    """
    Полный доступ для модератора,
    Для остальных только чтение.
    """
    def has_permission(self, request, view):
        return ((request.user.is_authenticated
                and request.user.is_moderator())
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return ((request.user.is_authenticated
                and request.user.is_moderator())
                or request.method in permissions.SAFE_METHODS)


class IsOwnerOrIsAdmin(permissions.IsAdminUser):
    """Доступ только для администратора и автора."""
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin())

    def has_object_permission(self, request, view, obj):
        return ((request.user.is_authenticated
                and request.user.is_admin())
                or obj.author == request.user)
