# /usr/bin/env python3

from project.server.controllers import login_views

auth_blueprint = login_views.auth_blueprint

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/auth/register', view_func = login_views.registration_view,
    methods = ['POST']
)
auth_blueprint.add_url_rule(
    '/auth/login', view_func = login_views.login_view,
    methods = ['POST']
)
auth_blueprint.add_url_rule(
    '/auth/status', view_func = login_views.user_view,
    methods = ['GET']
)
auth_blueprint.add_url_rule(
    '/auth/logout',  view_func = login_views.logout_view,
    methods = ['POST']
)

