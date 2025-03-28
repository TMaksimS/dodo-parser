from envparse import Env

env = Env()
env.read_envfile(path=".env")

MY_USER_AGENT = env.str("USER_AGENT")