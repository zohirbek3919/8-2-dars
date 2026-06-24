from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Company, Bino

class CompanyApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            companys = Company.objects.all()
            companys_list = []
            for company in companys:
                companys_list.append(
                    {
                        'id': company.pk,
                        'name': company.name
                    }
                )

            return Response(companys_list)
        else:
            company = Company.objects.get(pk=pk)
            return Response(model_to_dict(company))

    def post(self, request:Request, pk: int = None):
        if not pk:
            name = request.data.get("name", None)
            if name:
                company = Company.objects.create(name=name)
                return Response(model_to_dict(company), status=status.HTTP_201_CREATED)
            return Response({"message": "Xato!!!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Method not allowed!"}, 
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

class BinoApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            binos = Bino.objects.all()
            binos_list = []
            for bino in binos:
                binos_list.append(
                    {
                        'id': bino.pk,
                        'name': bino.name,
                        'qavat': bino.qavat,
                        'manzil': bino.manzil,
                        'company_id': bino.company.id

                    }
                )

            return Response(binos_list)
        else:
            bino = Bino.objects.get(pk=pk)
            return Response(model_to_dict(bino))

    def post(self, request:Request, pk: int = None):
        if not pk:
            name = request.data.get("name", None)
            qavat = request.data.get("qavat", None)
            manzil = request.data.get("manzil", None)
            company_id = request.data.get("company_id", None)

            if name and qavat and manzil and company_id:
                bino = Bino.objects.create(**request.data)
                return Response(model_to_dict(bino), status=status.HTTP_201_CREATED)
            return Response({"message": "Xato!!!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Method not allowed!"}, 
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
