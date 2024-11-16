from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import PaymentSerializer
from django.conf import settings
import qrcode
import stripe
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

def success(request):
    return render(request, 'success.html')


class ConfirmPaymentView(generics.GenericAPIView):
    def post(self, request):
        amount = request.data.get('amount')
        amount = int(float(amount) * 100)  # Convert to cents
        intent = stripe.PaymentIntent.create(
            amount= amount,
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )

        return Response({'clientSecret': intent['client_secret'],
                        'dpmCheckerLink': f"https://dashboard.stripe.com/settings/payment_methods/review?transaction_id={intent['id']}"}, 
                        status=status.HTTP_200_OK)
    

def create_payment(request):    
    amount = 20
    payment_url = f"{request.build_absolute_uri('/payment/proceed/')}{amount}"
    qr = qrcode.make(payment_url)
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response


@csrf_exempt
def proceed_payment(request, amount):
    return render(request, 'checkout.html', {'amount': amount})