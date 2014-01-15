# -*- coding: utf-8 -*-

"""
urwintranet.ui.views.home
~~~~~~~~~~~~~~~~~~~~~~~
"""

from urwintranet.ui.widgets import generic, home

from . import base


class HomeView(base.View):
    login_button = None

    def __init__(self):
        header = generic.Header()
        tabs = generic.Tabs(["home", "parts", "holidays", "preferences", "talks", "logout"])
        pony = generic.pony()
        self.widget = home.Home([tabs, pony])
