question Number 01
By default, Django signals are executed synchronously. This means that when a signal is triggered, the corresponding receiver function is executed immediately
within the same process and does not run in the background.
I added my code in signals.py
question Number 02
Yes, Django signals run in the same thread as the caller by default. This means that the execution of the signal occurs within the same thread as the function that triggers it.
To prove this, we can log the thread ID of the main execution and compare it with the thread ID inside the signal handler.
Added my code in signals.py and manage.py
question Number 03
Yes, by default, Django signals run in the same database transaction as the caller. 
This means that if the transaction fails and rolls back, any database changes made inside the signal will also be rolled back.
Added my code in signals.py and manage.py
Rectangle Question
Implemented Successfully in IDLE and code submitted
