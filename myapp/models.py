from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

# Simple model to demonstrate signals
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal handler for post_save
@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for: {instance.name}")
    time.sleep(2)  # Simulate a delay to demonstrate synchronous execution
    print(f"Signal handler finished for: {instance.name}")
    print(f"Signal handler thread ID: {threading.get_ident()}")

# Signal handler to modify the model inside the transaction
@receiver(post_save, sender=MyModel)
def modify_instance(sender, instance, **kwargs):
    instance.name = "Modified by Signal"
    instance.save()
    print(f"Object name changed to: {instance.name} inside the signal handler")
