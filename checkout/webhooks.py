from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_handler

import stripe

@require_POST
@csrf_exempt
def webhook(request): 
    """
    Listen for webhooks from stripe
    """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STIRPE_SECRET_KEY

    # Get the webhooks data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.webhook.construct_event(
        payload, sig_header, wh_secret
    )
    except ValueError as e:
    # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
    # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

