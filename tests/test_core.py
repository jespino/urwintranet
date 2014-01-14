from concurrent.futures import Future
from unittest import mock

from urwintranet.config import Configuration
from urwintranet.core import IntranetCore, StateMachine
from urwintranet import controllers

from . import factories


def test_if_client_is_not_authenticated_the_login_view_is_shown_on_startup():
    executor = factories.patched_executor()
    configuration = Configuration()
    core = IntranetCore(executor, configuration, authenticated=False)
    assert isinstance(core.controller, controllers.auth.LoginController)
    assert core.state_machine.state == StateMachine.LOGIN

def test_if_client_is_authenticated_the_projects_view_is_shown_on_startup():
    executor = factories.patched_executor()
    configuration = Configuration()
    core = IntranetCore(executor, configuration, authenticated=True, draw=False)
    assert isinstance(core.controller, controllers.projects.ProjectsController)
    assert core.state_machine.state == StateMachine.PROJECTS

def test_transitioning_from_projects_to_project_detail_and_project_backlog():
    projects = factories.projects()
    project = factories.project()
    project_f = Future()
    us = Future()
    stats = Future()
    executor = factories.patched_executor(project_detail=project_f,
                                          unassigned_user_stories=us,
                                          project_stats=stats,)
    configuration = Configuration()
    core = IntranetCore(executor, configuration, authenticated=True, draw=False)
    assert isinstance(core.controller, controllers.projects.ProjectsController)
    assert core.state_machine.state == StateMachine.PROJECTS
    core.state_machine.project_detail(project)
    project_f.set_result(project)
    us.set_result([])
    stats.set_result(factories.project_stats())
    assert isinstance(core.controller, controllers.projects.ProjectDetailController)
    assert core.state_machine.state == StateMachine.PROJECT_BACKLOG

