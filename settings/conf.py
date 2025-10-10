# Project modules
from decouple import config

# ----------------------------------------------
# Env id
#
ENV_POSSIBLE_OPTIONS = (
    "local",
    "prod",
)
ENV_ID = config("PROJECT_ENV_ID")
SECRET_KEY = "django-insecure--!sazwabf2m!-q#8ui0rlql_@^cii54s9cuu6@hhzli(-#yk_@"
