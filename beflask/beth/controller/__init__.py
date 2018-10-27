#!/usr/bin/env python
# -*- coding: utf-8 -*-


from beth.controller.home import home_index


def Register_Blueprints(app):

    app.register_blueprint(home_index)
   