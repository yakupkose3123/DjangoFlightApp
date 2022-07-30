from rest_framework import permissions

class IsStafforReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #?Safe metodlarda herkese izin ver
            return True
        else:
            return bool(request.user and request.user.is_staff) #?user staff sa her şeye izin ver
            # return bool(request.user.is_staff)