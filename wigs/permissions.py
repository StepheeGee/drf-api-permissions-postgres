# wigs/permissions.py
from rest_framework.permissions import BasePermission, IsAuthenticated

class IsPurchaseAllowed(BasePermission):
    def has_permission(self, request, view):
        # Allow any user to view wigs
        if view.action in ['list', 'retrieve']:
            return True
        # Allow authenticated users to purchase or customize wigs
        elif view.action in ['purchase', 'customize']:
            return IsAuthenticated().has_permission(request, view)
        return False

class IsAppropriateUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow any user to view wigs
        if view.action in ['list', 'retrieve']:
            return True
        # Allow only authenticated users to update or delete the wig
        elif view.action in ['update', 'partial_update', 'destroy']:
            return IsAuthenticated().has_permission(request, view) and obj.purchaser == request.user
        return False
