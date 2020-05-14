from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from basic.serializers import UserSerializer 
from basic.models import Book, User
from django.db import transaction
import jwt


"""
    01. Basic API
    
    Here are the API templates.
    TemplateBooksView: 
        1. Get all the books
        2. Create a book
    
    TemplateBookView:
        1. Get book by ID
        2. Update book by ID
        3. Delete book by ID
    
    
    Go to line 151 and create your code in BookView and BooksView
"""


class TemplateBooksView(GenericAPIView):
    queryset = Book.objects.all()

    @swagger_auto_schema(operation_summary="Get all the books.")
    def get(self, request):
        data = []

        books = self.queryset.all()
        # NOTE: self.queryset.all() is equal to Book.objects.all()

        for book in books:
            data.append(
                {
                    "id": book.id,
                    "name": book.name,
                    "price": book.price,
                    "rent_price": book.rent_price
                }
            )

        return JsonResponse(data, safe=False)

    @swagger_auto_schema(
        operation_summary="Create a book.",
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

    @swagger_auto_schema(operation_summary="Get a book by id.")
    def get(self, request, pk):
        book = self.get_object()

        data = {
            "id": book.id,
            "name": book.name,
            "price": book.price,
            "rent_price": book.rent_price
        }

        return JsonResponse(data)

    @swagger_auto_schema(
        operation_summary="Update a book",
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
    def put(self, request, pk):
        book = self.get_object()
        # NOTE: self.get_object() is equal to Book.objects.get(pk=pk)
        data = request.data.copy()

        name = request.data.get('name')
        price = request.data.get('price')
        rent_price = request.data.get('rent_price')

        book.name = name
        book.price = price
        book.rent_price = rent_price
        book.save()

        return JsonResponse(data)

    @swagger_auto_schema(operation_summary="Delete a book.")
    def delete(self, request, pk):
        book = self.get_object()
        # NOTE: self.get_object() is equal to Book.objects.get(pk=pk)

        data = {
            "id": book.id,
            "name": book.name,
            "price": book.price,
            "rent_price": book.rent_price
        }
        book.delete()

        return JsonResponse(data)


"""
    Empty APIs
    Delete Single-line comment at line 45 and 46 in ci-mod.urls to activate BookView and BooksView
"""


class BooksView(GenericAPIView):
    queryset = Book.objects.all()

    @swagger_auto_schema(operation_summary="Get all the books.")
    def get(self, request):
        data = []
        books = Book.objects.all()

        for book in books:
            data.append(
                {
                    "id": book.id,
                    "name": book.name,
                    "price": book.price,
                    "rent_price": book.rent_price,
                }
            )

        return JsonResponse(data, safe=False)

    @swagger_auto_schema(
        operation_summary="Create a book.",
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
            name = name,
            price = price,
            rent_price = rent_price
        )

        return JsonResponse(data)


class BookView(GenericAPIView):
    queryset = Book.objects.all()

    @swagger_auto_schema(operation_summary="Get a book by id.")
    def get(self, request, pk):
        book = self.get_object()

        data = {
            "id": book.id,
            "name": book.name,
            "price": book.price,
            "rent_price": book.rent_price
        }

        return JsonResponse(data)

    @swagger_auto_schema(
        operation_summary="Update a book",
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
    def put(self, request, pk):
        book = self.get_object()

        data = request.data.copy()

        name = request.data.get('name')
        price = request.data.get('price')
        rent_price = request.data.get('rent_price')
        
        book.name = name
        book.price = price
        book.rent_price = rent_price
        book.save()

        return JsonResponse(data)

    @swagger_auto_schema(operation_summary="Delete a book.")
    def delete(self, request, pk):
        book = self.get_object()
        book.delete()

        return JsonResponse({'response': 'Delete successfully!!!'})

class UserView(GenericAPIView):
    queryset = User.objects.all()
    
    @swagger_auto_schema(
        operation_summary='Get user info'
    )
    def get(self, request, pk):
        data = {}
        try:
            user = User.objects.get(id=pk)
            data = {
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "email": user.email
            }
        except Exception as e:
            data = {'error': str(e)}
            
        return JsonResponse(data)

class LoginView(GenericAPIView):
    queryset = User.objects.all()

    @swagger_auto_schema(
        operation_summary="User login",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='user name'
                ),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='password'
                ),
            }
        )
    )
    def post(self, request):
        
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        
        try:
            user = User.objects.get(username=username,password=password)
            data = {}

            payload = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "phone": user.phone
            }
            
            token = jwt.encode(payload, 'secret')
            data["token"] = token.decode("utf-8")

        except Exception as e:
            data = {'error': 'Username or password is wrong.'}


        return JsonResponse(data)
    

class AdminView(GenericAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary="Create user",
    )
    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)

