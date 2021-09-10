from django.urls import path
from . import views

urlpatterns = [
    path(
        "allPizza",
        views.allPizza,
        name="allPizza",
    ),
    path(
        "allDrink",
        views.allDrink,
        name="allDrink",
    ),
    path(
        "allSide",
        views.allSide,
        name="allSide",
    ),
    path(
        "allSpecial",
        views.allSpecial,
        name="allSpecial",
    ),
    path(
        "makeReservation",
        views.makeReservation,
        name="makeReservation",
    ),
    path(
        "placeOrder",
        views.placeOrder,
        name="placeOrder",
    ),
    path(
        "rateExperience",
        views.rateExperience,
        name="rateExperience",
    ),
]
