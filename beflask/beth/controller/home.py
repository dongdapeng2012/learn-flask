# -*- coding: utf-8 -*-

from flask import Blueprint
from beth.service.Schatbot import chatbotfunc

home_index = Blueprint('home', __name__, url_prefix="/home")


@home_index.route('/')
@home_index.route('/index')
def index():
    return "Hello"

@home_index.route('/run')
def chatbot():

    return chatbotfunc()