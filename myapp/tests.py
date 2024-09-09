
from django.test import TestCase
from myapp.models import MyModel
import time
import threading
from django.db import transaction
from django.core.exceptions import ValidationError

class MyModelTest(TestCase):
    def test_signal_synchronous(self):
    
        start_time = time.time()
        MyModel.objects.create(name="TestSync")
        end_time = time.time()
        duration = end_time - start_time

        self.assertGreater(duration, 5, "Signal is running synchronously.")
    
    def test_signal_same_thread(self):
 
        caller_thread = threading.current_thread().name
        MyModel.objects.create(name="TestThread")
     
        self.assertEqual(caller_thread, threading.current_thread().name)

    def test_signal_in_transaction(self):

        try:
            with transaction.atomic():
                MyModel.objects.create(name="FailTransaction")
        except ValidationError:
            pass

        self.assertEqual(MyModel.objects.count(), 0, "Signal should have caused a rollback.")
