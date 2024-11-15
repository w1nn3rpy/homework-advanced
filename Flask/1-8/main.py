import os
import datetime
import random
import re

from flask import Flask
from random import choice


app = Flask(__name__)

car_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cat_list = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

text = open(BOOK_FILE, 'r').read()

word_pattern = r'\b\w+\b'

word_list = re.findall(word_pattern, text)

@app.route('/hello_world')
def hello_world():
    return 'Hello world!'

@app.route('/cars')
def cars():
    global car_list
    return ','.join(map(str, car_list))

@app.route('/cats')
def cats():
    global cat_list
    cat = choice(cat_list)
    return cat

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f'Точное время: {current_time}'

@app.route('/get_time/future')
def get_future_time():
    future_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f'Точное время через час будет: {future_time}'

@app.route('/get_random_word')
def get_random_word():
    return random.choice(word_list)

@app.route('/counter')
def counter():
    counter.visits += 1
    return str(counter.visits)

counter.visits = 0

