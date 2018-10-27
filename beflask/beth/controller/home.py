#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import   Blueprint




home_index = Blueprint('home', __name__, url_prefix="/home")


@home_index.route('/')
@home_index.route('/index')

def index():
    return "Hello"