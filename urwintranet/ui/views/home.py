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
        # Header
        header = generic.pony()
        home_widget = home.Home([header,])
        self.widget = generic.center(home_widget)

    @property
    def username(self):
        return self._username_editor.get_edit_text()

    @property
    def password(self):
        return self._password_editor.get_edit_text()
