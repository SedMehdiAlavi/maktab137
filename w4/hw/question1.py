from _datetime import datetime

def restrict_hours(start, end):
    """
    We set time limitation (start, end) to run the main function
     only in specified time duration.
    """
    hour = datetime.now().hour
    def decorator(func):
        def wrapper(*args, **kwargs):
            if start <= hour <= end:
                return func(*args, **kwargs)
            else:
                pass

        return wrapper
    return decorator


@restrict_hours(9, 17)
def do_work():
    """
    It's just a simple function to test the triple-function
      decorator
    """
    print("Working...")


print(datetime.now().hour)
do_work()

