from . import views
from django.urls import path
from payment.views import payment_by_car

urlpatterns = [
    path("payment/<int:id>/", views.payment_by_car, name="payment"),
]