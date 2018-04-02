# ===========================================================================
# eXe
# Copyright 2004-2006, University of Auckland
# Copyright 2006-2007 eXe Project, New Zealand Tertiary Education Commission
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================
"""
AuthoringPage is responsible for creating the XHTML for the authoring
area of the eXe web user interface.
"""
import os
import logging
import time
import exceptions
import sys
from twisted.web.resource import Resource
from exe.webui import common
from cgi import escape
import exe.webui.builtinblocks
from exe.webui.blockfactory import g_blockFactory
from exe.engine.error import Error
from exe.webui.renderable import RenderableResource

from exe.engine.path import Path
from exe import globals as G
import re

log = logging.getLogger(__name__)


# ===========================================================================
class AuthoringPagefake(RenderableResource):
    """
    AuthoringPage is responsible for creating the XHTML for the authoring
    area of the eXe web user interface.
    """
    name = u'authoring'

    def __init__(self, parent = None):
        RenderableResource.__init__(self, parent)
        a= self
        b= 6

    def getNodesas(self):
        return self.package.root