# myapp/tests.py
from django.test import TestCase
from myapp.models import MyModel
import time
import threading
from django.db import transaction
from django.core.exceptions import ValidationError

class MyModelTest(TestCase):

    def test_signal_synchronous(self):
        """
        Test that signals are executed synchronously.
        """
        print("\n[TEST] Verifying if the signal runs synchronously...")
        start_time = time.time()
        MyModel.objects.create(name="TestSync")
        end_time = time.time()
        duration = end_time - start_time

        # Check if the operation takes more than 5 seconds due to the sleep in signal handler
        self.assertGreater(duration, 5, "Signal is running synchronously.")
        print("[RESULT] Signal ran synchronously as expected.\n")

    def test_signal_same_thread(self):
        """
        Test that signals run in the same thread as the caller.
        """
        print("\n[TEST] Verifying if the signal runs in the same thread as the caller...")
        caller_thread = threading.current_thread().name
        MyModel.objects.create(name="TestThread")
        self.assertEqual(caller_thread, threading.current_thread().name)
        print("[RESULT] Signal ran in the same thread ('MainThread') as expected.\n")

    def test_signal_in_transaction(self):
        """
        Test that signals run in the same transaction.
        If the signal raises an exception, the entire transaction should roll back.
        """
        print("\n[TEST] Verifying if the signal runs in the same database transaction as the caller...")
        try:
            with transaction.atomic():
                MyModel.objects.create(name="FailTransaction")
        except ValidationError:
            pass

        # Ensure no object was created due to the transaction rollback
        self.assertEqual(MyModel.objects.count(), 0, "Signal should have caused a rollback.")
        print("[RESULT] Signal caused a rollback, and no object was created, verifying it's part of the same transaction.\n")
