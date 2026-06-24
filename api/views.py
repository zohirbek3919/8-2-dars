from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Company, Bino
from .serializers import CompanySerializer, BinoSerializer


class CompanyApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            companys = Company.objects.all()
            serializer = CompanySerializer(companys, many=True)
            return Response(serializer.data)
        else:
            company = Company.objects.get(pk=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data)

    def post(self, request: Request, pk: int = None):
        if not pk:
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Method not allowed!"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)


class BinoApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            binos = Bino.objects.all()
            serializer = BinoSerializer(binos, many=True)
            return Response(serializer.data)
        else:
            bino = Bino.objects.get(pk=pk)
            serializer = BinoSerializer(bino)
            return Response(serializer.data)

    def post(self, request: Request, pk: int = None):
        if not pk:
            serializer = BinoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Method not allowed!"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
