# Without this line in the init file django would not know about the custom ready in apps so the signals would not work
default_app_config = 'checkout.apps.CheckoutConfig'