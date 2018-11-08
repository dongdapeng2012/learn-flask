#!/usr/bin/env python
# -*- coding: utf-8 -*-


import beth.controller.home


def Register_Blueprints(app):

    app.register_blueprint(home.home_index)
   