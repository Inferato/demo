from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

import logging

class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserCoursesPermissionMixin(PermissionRequiredMixin):
    permission_required = 'user_session.can_edit_course'


class SuperuserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
  
class CacheMixin:
    cache_timeout = 60 * 5

    @method_decorator(cache_page(cache_timeout))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class LoggingMixin:
    logger = logging.getLogger(__name__)

    def dispatch(self, *args, **kwargs):
        self.logger.warning("View accessed with args: %s, kwargs: %s", args, kwargs)
        return super().dispatch(*args, **kwargs)
