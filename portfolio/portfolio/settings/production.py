from .base import *
import dj_database_url


DATABASES["default"] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Allow all host headers
ALLOWED_HOSTS = ["*"]

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
