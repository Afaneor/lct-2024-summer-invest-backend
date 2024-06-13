from server.settings.components import config

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://127.0.0.1:9000',
    'http://localhost:3000',
    'http://192.168.21.141:8080',
    'https://invest.yapa.one',
    'https://prod.invest.yapa.one',
    'https://prod.api.invest.yapa.one',
    'https://api.invest.yapa.one',
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'generated-user-id',
]
CORS_PREFLIGHT_MAX_AGE = config(
    'CORS_PREFLIGHT_MAX_AGE',
    cast=int,
    default=86400,
)
CORS_ALLOW_CREDENTIALS = config(
    'CORS_ALLOW_CREDENTIALS',
    cast=bool,
    default=True,
)

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://127.0.0.1:9000',
    'http://localhost:3000',
    'https://invest.yapa.one',
    'https://prod.invest.yapa.one',
    'https://api.invest.yapa.one',
    'https://prod.api.invest.yapa.one',
]

CSRF_COOKIE_HTTPONLY = False  # CSRF stored in http only cookie
CSRF_COOKIE_SECURE = False  # CSRF cookie is secure
CSRF_COOKIE_DOMAIN = '*.yapa.one'  # CSRF cookie domain

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://192.168.21.141:8080',
    'https://invest.yapa.one',
    'https://prod.invest.yapa.one',
    'https://api.invest.yapa.one',
    'https://prod.api.invest.yapa.one',
]
