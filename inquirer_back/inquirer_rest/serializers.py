from rest_framework import serializers
from .models import Inquirer


class InquirerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquirer
        fields = ('title', )
