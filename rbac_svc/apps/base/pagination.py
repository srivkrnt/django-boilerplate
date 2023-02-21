from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from apps.base.constants import KeyLabels


class CustomPagination(LimitOffsetPagination):
    """
    Custom Pagination class for the service
    """

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginates the queryset
        """

        if view and hasattr(view, KeyLabels.DEFAULT_PAGE_LIMIT):
            self.default_limit = view.default_page_limit

        return super().paginate_queryset(queryset, request, view)

    def get_next_link(self):
        """
        Returns the next pagination link
        """

        next_offset = self.offset + self.limit
        if next_offset >= self.count:
            next_offset = None

        return {KeyLabels.OFFSET: next_offset}

    def get_previous_link(self):
        """
        Returns the previous link
        """

        prev_offset = self.offset - self.limit

        if self.offset <= 0:
            prev_offset = None
        else:
            if prev_offset <= 0:
                prev_offset = 0

        return {KeyLabels.OFFSET: prev_offset}

    def get_paginated_response(self, data):
        """
        Returns paginated response
        """

        return Response(OrderedDict([
            (KeyLabels.COUNT, self.count),
            (
                KeyLabels.PAGE,
                OrderedDict([
                    (KeyLabels.NEXT, self.get_next_link()),
                    (KeyLabels.PREVIOUS, self.get_previous_link())
                ])
            ),
            (KeyLabels.DATA, data)
        ]))
