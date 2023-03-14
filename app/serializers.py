from rest_framework import serializers
from app.models import company,employee


class company_serializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = company
        fields = '__all__'

class employee_serilalizer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = employee
        fields = '__all__'
