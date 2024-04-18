from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    name = 'checkout'
    
    # This imports the signals module
    def ready(self):
        import checkout.signals

