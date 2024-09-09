
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from myapp.models import MyModel
import time
import threading

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for {instance.name} in thread: {threading.current_thread().name}")
    
    
    if instance.name == "TestSync":
        time.sleep(5)
    
    
    if instance.name == "FailTransaction":
        raise ValidationError("Triggering rollback in transaction.")
    
    print("Signal processing completed.")
