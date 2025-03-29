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
