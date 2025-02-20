# By default, Django signals are executed synchronously.
# This means that when a signal is triggered, the corresponding receiver function is executed 
# immediately within the same process and does not run in the background.


import time
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
import threading



logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    """Simulates a slow signal by adding a delay"""
    logger.info("Signal execution started")
    start_time = time.time()
    
    
    time.sleep(5)  

    end_time = time.time()
    logger.info(f"Signal execution finished in {end_time - start_time} seconds")


# Yes, Django signals run in the same thread as the caller by default.
# This means that the execution of the signal occurs within the
# same thread as the function that triggers it.. Here Code



import threading
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Set up logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def check_thread_signal(sender, instance, **kwargs):
    """Logs the thread ID inside the signal"""
    logger.info(f"Signal running in thread: {threading.get_ident()}")



# Yes, by default, Django signals run in the same database transaction as the caller.
# This means that if the transaction fails and rolls back, 
# any database changes made inside the signal will also be rolled back



# Set up logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    """Modifies the database inside the signal"""
    logger.info("Signal started execution")
    
    # Create another user 
    User.objects.create(username="signal_created_user")

    logger.info("Signal finished execution")


    

