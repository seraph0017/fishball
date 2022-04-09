from starlette.responses import RedirectResponse
from devtools import debug



def login_required():
    def decorator(func):
        def wrap(*args, **kwargs):
            if args[0].state.user:
                debug(args)
                func(*args, **kwargs)
            else:
                RedirectResponse(url="http://localhost:8000/")

        return wrap

    return decorator