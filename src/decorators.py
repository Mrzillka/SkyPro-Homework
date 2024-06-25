from functools import wraps
from typing import Optional, Any


def log(filename: Optional[str] = None) -> Any | None:
    """Logging if function working successfully or not in the file (or in console by default)"""
    def wrapper(funk: Any) -> Any | None:
        @wraps(funk)
        def inner(*args: Any, **kwargs: Any) -> Any:
            result = None
            error = None
            try:
                result = funk(*args, **kwargs)
                log_text = f"{funk.__name__} ok\n"
            except Exception as e:
                error = e.__class__
                log_text = f"{funk.__name__} error: {e.__class__.__name__}. Inputs {args, kwargs}\n"
            if filename:
                with open(filename, 'a') as log_file:
                    log_file.write(log_text)
            else:
                print(log_text)
            if error:
                raise error
            return result

        return inner

    return wrapper
