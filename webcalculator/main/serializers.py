from rest_framework import serializers


class SuccessSerializer(serializers.Serializer):
   data = serializers.CharField()
   many = serializers.BooleanField()

   class Meta:
      fields = ('data', 'many')



