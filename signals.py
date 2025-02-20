import time
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    """Simulates a slow signal by adding a delay"""
    logger.info("Signal execution started")
    start_time = time.time()
    
    
    time.sleep(5)  

    end_time = time.time()
    logger.info(f"Signal execution finished in {end_time - start_time} seconds")
