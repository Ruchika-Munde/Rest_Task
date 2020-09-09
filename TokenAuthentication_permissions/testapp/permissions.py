from rest_framework.permissions import BasePermission, SAFE_METHODS

# safe_methods are -GET, HEAD, OPTIONS

class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False


