#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
import logging
from django.contrib.auth.models import User
import time
from django.db import transaction


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# 'By default, Django signals are executed synchronously.
# This means that when a signal is triggered, the corresponding receiver function is executed 
# immediately within the same process and does not run in the background'

start_time = time.time()
user = User.objects.create(username="test_user")
end_time = time.time()

print(f"User creation took {end_time - start_time} seconds")


# Yes, Django signals run in the same thread as the caller by default.
# This means that the execution of the signal occurs within the
# same thread as the function that triggers it.. Here Code


# Set up logging
logger = logging.getLogger(__name__)

# Log the main thread ID
logger.info(f"Main execution running in thread: {threading.get_ident()}")

# Trigger the signal
User.objects.create(username="test_user")

# Yes, by default, Django signals run in the same database transaction as the caller.
# This means that if the transaction fails and rolls back, 
# any database changes made inside the signal will also be rolled back


# Check initial user count
initial_count = User.objects.count()

try:
    with transaction.atomic():
        # Create a user, triggering the signal
        User.objects.create(username="main_user")
        raise Exception("Simulated failure")  # Force a rollback

except Exception as e:
    print("Transaction rolled back")

# Check user count after rollback
final_count = User.objects.count()
print(f"Initial count: {initial_count}, Final count: {final_count}")
