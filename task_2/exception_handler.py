from functools import wraps


def handle_errors(logger):
    """Decorator for handling exceptions in scraper functions."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in function {func.__name__}: {e}")
                raise
        return wrapper
    return decorator