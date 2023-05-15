from rest_framework.permissions import BasePermission

from .common import Role


class AdminPermission(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class ClientPermission(BasePermission):
    """
    Allows access only to client users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == Role.CLIENT


class MarketingPermission(BasePermission):
    """
    Allows access only to marketing users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == Role.MARKETING


class EmployeePermission(BasePermission):
    """
    Allows access only to employee users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == Role.EMPLOYEE
