from rest_framework import permissions
from sscm.profiles.models import MemberProfile


class CanWatchMovie(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return (
                request.user.profile
                and request.user.profile["status"] == MemberProfile.Status.ACTIVE
            )
        return False
