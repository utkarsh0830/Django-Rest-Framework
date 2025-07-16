from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page-size'
    page_query_param =  'page'
    max_page_size = 1

    def get_paginated_response(self, data):
        return Response({
            'next' : self.get_next_link(),
            'prev' : self.get_previous_link(),
            'count' : self.page.paginator.count,
            'results' : data
        })
