from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    imageURL = serializers.SerializerMethodField("get_image_url")

    def get_image_url(self, obj):
        try:
            return self.context["request"].build_absolute_uri(obj.image.url)
        except:
            return None

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "imageURL",
            "hasToppings",
            "hasSizes",
            "price",
            "summary"
        )
