import time
from flask import Flask
from flask_caching import Cache
from random import randint
from time import sleep

config = {
    'DEBUG':True,
    'CACHE_TYPE':"SimpleCache",
    'CACHE_DEFAULT_TIMEOUT':300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
cache.init_app(app)


@app.route('/')
@cache.cached(10)
def index():
    number = randint(10,100)
    return "output is {0}".format(number)

@cache.cached(20,key_prefix="test")
def gen_num():
    number = randint(10,100)
    return "output is {0}".format(number)

@app.route("/num")
def display_num():
    number = gen_num()
    return number

@app.route("/get_cache")
def display():
    return cache.get('test')

@app.route("/get_val/<int:num>")
@cache.memoize(timeout=10)
def val(num):
    sleep(2)
    return "the result is {} ".format(num*2)



if __name__=="__main__":
    app.run(debug=True,port=4000)

