from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from basic.models import Book


class TemplateBooksView(GenericAPIView):
    queryset = Book.objects.all()

    @swagger_auto_schema(
        operation_summary="Create a book and Get all the books",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='name of book'
                ),
                'price': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='price'
                ),
                'rent_price': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='rental price'
                )
            }
        )
    )
    def post(self, request):
        data = request.data.copy()
        name = request.data.get('name')
        price = request.data.get('price')
        rent_price = request.data.get('rent_price')

        Book.objects.create(
            name=name,
            price=price,
            rent_price=rent_price
        )

        return JsonResponse(data)


class TemplateBookView(GenericAPIView):
    queryset = Book.objects.all()

    def get(self, request, pk):
        book = self.get_object()

        data = {
            "id": book.id,
            "name": book.name,
            "price": book.price,
            "rent_price": book.rent_price
        }

        return JsonResponse(data)
