from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from ..paginations import BasePagination


class BaseView:
    pagination_class = BasePagination
    permission_classes = (DjangoModelPermissions,)


class BaseViewSet(BaseView, ModelViewSet):
    pass


class BaseListView(BaseView, ListAPIView):
    pass


class BaseRetrieveView(BaseView, RetrieveAPIView):
    pass
