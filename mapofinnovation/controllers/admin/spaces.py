import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mapofinnovation.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SpacesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('space', 'spaces', controller='admin/spaces', 
    #         path_prefix='/admin', name_prefix='admin_')

    def index(self, format='html'):
        """GET /admin/spaces: All items in the collection"""
        # url('admin_spaces')

    def create(self):
        """POST /admin/spaces: Create a new item"""
        # url('admin_spaces')

    def new(self, format='html'):
        """GET /admin/spaces/new: Form to create a new item"""
        # url('admin_new_space')

    def update(self, id):
        """PUT /admin/spaces/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('admin_space', id=ID),
        #           method='put')
        # url('admin_space', id=ID)

    def delete(self, id):
        """DELETE /admin/spaces/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('admin_space', id=ID),
        #           method='delete')
        # url('admin_space', id=ID)

    def show(self, id, format='html'):
        """GET /admin/spaces/id: Show a specific item"""
        # url('admin_space', id=ID)

    def edit(self, id, format='html'):
        """GET /admin/spaces/id/edit: Form to edit an existing item"""
        # url('admin_edit_space', id=ID)
