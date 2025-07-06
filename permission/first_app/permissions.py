from rest_framework import permissions

class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
    

# Unauthenticated users should be able to view /reviews/<id>/

class ReviewOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True  # General access allowed

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


# Only authenticated users should be able to access a single review,

# class ReviewOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return True  # Allow access to the view (e.g., list page)

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             # ✅ Only allow access if the user is authenticated
#             return request.user and request.user.is_authenticated
#         # ✅ For write methods, only the review author is allowed
#         return obj.user == request.user
