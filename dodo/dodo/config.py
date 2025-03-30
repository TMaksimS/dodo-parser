"""parse env"""

from envparse import Env

env = Env()
env.read_envfile(path=".env")

MY_USER_AGENT = env.str("USER_AGENT")
CITIES = env.list("CITIES")

RABBIT_USER = env.str("RABBIT_USER")
RABBIT_PASS = env.str("RABBIT_PASS")
RABBIT_HOST = env.str("RABBIT_HOST")
RABBIT_PORT = env.int("RABBIT_PORT")
RABBIT_URL= f"amqp://{RABBIT_USER}:{RABBIT_PASS}@{RABBIT_HOST}:{RABBIT_PORT}"

QUEUE_DODO = env.str("QUEUE_DODO", default="DodoQueue")

DB_USER = env.str("DB_USER", default="postgres_test")
DB_PASS = env.str("DB_PASS", default="postgres_test")
DB_NAME = env.str("DB_NAME", default="postgres_test")
DB_HOST = env.str("DB_HOST", default="localhost")
DB_PORT = env.int("DP_PORT", default=5432)
REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
