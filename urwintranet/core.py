# -*- coding: utf-8 -*-

"""
urwintranet.core
~~~~~~~~~~~~~~
"""

import functools
from concurrent.futures import wait

import urwid

from urwintranet.ui import views
from urwintranet import controllers
from urwintranet.config import Keys, PALETTE


class IntranetCore(object):
    def __init__(self, executor, configuration, authenticated=False, draw=True):
        self.executor = executor
        self.configuration = configuration
        self.draw = draw

        if authenticated:
            self.state_machine = StateMachine(self, state=StateMachine.HOME)
            self.controller = self._build_home_controller()
        else:
            self.state_machine = StateMachine(self, state=StateMachine.LOGIN)
            self.controller = self._build_login_controller()

        # Main Loop
        self.loop = urwid.MainLoop(self.controller.view.widget,
                                   palette=PALETTE,
                                   unhandled_input=self.key_handler,
                                   handle_mouse=True,
                                   pop_ups=True)

    def run(self):
        self.loop.run()

    def key_handler(self, key):
        if key == Keys.QUIT:
            self.configuration.save()
            raise urwid.ExitMainLoop
        elif key == Keys.DEBUG:
            self.debug()
        else:
            return self.controller.handle(key)

    def debug(self):
        self.loop.screen.stop()
        import ipdb; ipdb.set_trace()
        self.loop.screen.start()

    def login_view(self):
        pass

    def parts_home(self):
        self.controller = self._build_home_controller()
        self.transition()

    def parts_view(self):
        self.controller = self._build_parts_controller()
        self.transition()

    def project_view(self, project):
        self.controller = self._build_project_controller(project)
        self.transition()

    def transition(self):
        if self.draw:
            self.loop.widget = self.controller.view.widget
            self.loop.widget._invalidate()
            self.loop.draw_screen()

    def set_auth_config(self, auth_data):
        self.configuration.config_dict["auth"] = {}
        self.configuration.config_dict["auth"]["token"] = auth_data["token"]

    def _build_login_controller(self):
        login_view = views.auth.LoginView('username', 'password')
        login_controller = controllers.auth.LoginController(login_view,
                                                            self.executor,
                                                            self.state_machine)
        return login_controller

    def _build_home_controller(self):
        home_view = views.home.HomeView()
        home_controller = controllers.home.HomeController(home_view,
                                                          self.executor,
                                                          self.state_machine)
        return home_controller

    def _build_parts_controller(self):
        parts_view = views.parts.PartsView()
        parts_controller = controllers.parts.PartsController(parts_view,
                                                          self.executor,
                                                          self.state_machine)
        return parts_controller


class StateMeta(type):
    def __new__(cls, clsname, bases, dct):
        state_attrs = [k for k in dct if k.isupper()]
        state_set = {dct[s] for s in state_attrs}
        assert len(state_attrs) == len(state_set), "State attributes must be unique"
        dct["STATES"] = state_set
        return super().__new__(cls, clsname, bases, dct)


class StateMachine(metaclass=StateMeta):
    LOGIN = 0
    HOME = 1
    PARTS = 2
    PART = 3
    HOLIDAYS = 4
    TALKS = 5
    PREFERENCES = 6

    def __init__(self, core, state):
        self._core = core
        self.state = state

    def logged_in(self, auth_data):
        self._core.set_auth_config(auth_data)
        self._core.home_view()

    def home(self):
        self._core.parts_home()

    def parts(self):
        self._core.parts_view()

    def project_detail(self, project):
        self._core.project_view(project)

    def transition(self, state):
        assert state in self.STATES, "{0} is not a valid state".format(state)
        self.state = state
        self.refresh()

    def refresh(self):
        self._core.transition()
