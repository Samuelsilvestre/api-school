from rest_framework import permissions

class SuperUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        methods = ['GET', 'POST', 'DELETE', 'PUT']
        for method in methods:
            if request.method == method:

                if request.user.is_superuser:
                    return True
                
                else:
                    return False
