from django.test import TestCase
from .models import MyModel
from django.db.models.signals import post_save
import threading
import time

class SignalTestCase(TestCase):

    def setUp(self):
  
        self.obj = MyModel.objects.create(name="Test Object")

    def test_synchronous_execution(self):

        with self.assertLogs('django.db.backends', level='DEBUG') as cm:
            print("Main thread ID:", threading.get_ident())
            self.obj = MyModel.objects.create(name="Test Sync")
            print("Object created:", self.obj.name)
            # Check if the signal handler prints the correct message
            self.assertIn("Signal received for:", cm.output)

    def test_same_thread(self):
     
        print("Main thread ID:", threading.get_ident())
        self.obj = MyModel.objects.create(name="Test Thread")
        print("Object created:", self.obj.name)
        # Check if signal handler prints the thread ID
        self.assertIn(f"Signal handler thread ID: {threading.get_ident()}", self.captured_output)

    def test_transaction(self):
   
        with self.assertLogs('django.db.backends', level='DEBUG') as cm:
            self.obj = MyModel.objects.create(name="Test Transaction")
            print("Object after transaction:", self.obj.name)
            # Simulate transaction logic
            with transaction.atomic():
                self.obj.name = "Updated in Transaction"
                self.obj.save()
            # Verify the object name is updated
            self.assertEqual(self.obj.name, "Updated in Transaction")
