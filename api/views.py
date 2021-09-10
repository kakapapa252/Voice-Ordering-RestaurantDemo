import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import (
    ProductSerializer
)

from .models import (
    Category,
    Product,
    Rating
)


@api_view(["GET"])
def allPizza(request):
    category = Category.objects.get(name="Pizza")
    allProducts = Product.objects.filter(category=category)
    serializer = ProductSerializer(
        allProducts, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
def allDrink(request):
    category = Category.objects.get(name="Drink")
    allProducts = Product.objects.filter(category=category)
    serializer = ProductSerializer(
        allProducts, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
def allSide(request):
    category = Category.objects.get(name="Side")
    allProducts = Product.objects.filter(category=category)
    serializer = ProductSerializer(
        allProducts, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["GET"])
def allSpecial(request):
    allProducts = Product.objects.filter(isSpecial=True)
    serializer = ProductSerializer(
        allProducts, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["POST"])
def makeReservation(request):
    time = request.data.get("time") or None
    date = request.data.get("date") or None
    mess = "You've Successfully reserved a table with Voice Restaurant on " + \
        date + " (yyyy-mm-dd) at " + time + \
        " hours. \nLooking forward to seeing you!"
    send_mail('Successful Reservation at Voice Restaurant', mess, 'customermapsindia@gmail.com',
              ["customermapsindia@gmail.com"], fail_silently=False,)
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def placeOrder(request):
    review = request.data.get("review") or None
    mess = "You've Successfully placed an order with Voice Restaurant. " + \
        review[:-34] + " Your order will arrive shortly!"
    send_mail('Successful Order placed with Voice Restaurant', mess, 'customermapsindia@gmail.com',
              ["customermapsindia@gmail.com"], fail_silently=False,)
    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def rateExperience(request):
    rating = request.data.get("rating") or None
    mode = request.data.get("mode") or None
    rated = Rating.objects.create(rating=rating, mode=mode)
    rated.save()
    return Response(status=status.HTTP_200_OK)
