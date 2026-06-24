from rest_framework import serializers
from .models import Company, Bino


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class BinoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    qavat = serializers.IntegerField(allow_null=True, required=False)
    manzil = serializers.CharField(max_length=255)
    company_id = serializers.IntegerField()

    def create(self, validated_data):
        bino = Bino.objects.create(**validated_data)
        return bino

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.qavat = validated_data.get("qavat", instance.qavat)
        instance.manzil = validated_data.get("manzil", instance.manzil)
        instance.company_id = validated_data.get("company_id", instance.company_id)
        instance.save()
        return instance
