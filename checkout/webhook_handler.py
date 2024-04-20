from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWH_handler:
    """
    Handle stripe webhooks
    """
    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        # Extract necessary information from the event
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Retrieve the Charge object associated with the PaymentIntent
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        # Get billing details from the Charge object
        billing_details = stripe_charge.billing_details

        # Extract shipping details from the PaymentIntent
        shipping_details = intent.shipping

        # Calculate grand total
        grand_total = round(stripe_charge.amount / 100, 2)


        for field, value in shipping_details.address.products():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.object.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.country,
                    postcode__iexact=shipping_details.postal_code,
                    town_or_city__iexact=shipping_details.city,
                    street_address1__iexact=shipping_details.line1,
                    street_address2__iexact=shipping_details.line2,
                    county__iexact=shipping_details.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
                
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.object.create(
                        full_name=shipping_details.name,
                        email=shipping_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.country,
                        postcode=shipping_details.postal_code,
                        town_or_city=shipping_details.city,
                        street_address1=shipping_details.line1,
                        street_address2=shipping_details.line2,
                        county=shipping_details.state,
                        original_bag=bag,
                        stripe_pid=pid,

                    )
                for product_id, product_data in json.loads(bag).items():
                    
                        product = Product.objects.get(product_id=product_id)
                        if isinstance(product_data, int):
                            order_line_item = OrderLineItem (
                                order=order,
                                product=product,
                                quantity=product_data,
                            )
                            order_line_item.save()
                        else:
                            for size, quantity in product_data['products_by_size'].products():
                                order_line_item = OrderLineItem(
                                    order=order,
                                    product=product,
                                    quantity=product_data,
                                    product_size=size,
                                )
                                order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]}: ERROR: {e}',
                    status=500)
            return HttpResponse(content=f'Webhook received: {event["type"]}: SUCCESS: Created in webhook ',
                        status=200) 

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent.failed webhook from stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
