
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm
from django.core.mail import EmailMultiAlternatives


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            client = MailchimpMarketing.Client()
            client.set_config({
                "api_key": settings.MAILCHIMP_API_KEY,
                "server": settings.MAILCHIMP_DATA_CENTER,
            })

            try:
                response = client.lists.add_list_member(settings.MAILCHIMP_AUDIENCE_ID, {
                    "email_address": email,
                    "status": "subscribed",
                })
                messages.success(
                    request, 'You have successfully subscribed to our newsletter!')

                # Send confirmation email
                subject = 'Subscription Confirmation'
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = [email]
                text_content = 'Thank you for subscribing to our newsletter!'
                html_content = '<p>Thank you for subscribing to our <strong>newsletter</strong>!</p>'

                msg = EmailMultiAlternatives(
                    subject, text_content, from_email, to_email)
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            except ApiClientError as error:
                messages.error(
                    request, 'An error occurred. Please try again later.')
                return redirect('newsletter_signup')
    else:
        form = NewsletterSignupForm()

    return render(request, 'newsletter/newsletter_signup.html', {'form': form})
