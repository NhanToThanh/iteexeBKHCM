#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===========================================================================
# eXe
# Copyright 2004-2006, University of Auckland
# Copyright 2006-2007 eXe Project, New Zealand Tertiary Education Commission
# Copyright 2013, Pedro Peña Pérez, Open Phoenix IT
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# ===========================================================================

"""
The PreferencesPage is responsible for managing eXe preferences
"""

import logging
import json
from twisted.web.resource import Resource
from exe.webui.renderable import RenderableResource
import sys
from exe.webui import common
from exe.engine.idevice   import Idevice
from exe.engine.package          import Package


import mywebbrowser
from exe.engine.path import Path
import os.path
from exe.webui import common
import io

log = logging.getLogger(__name__)

Nodestest = []
numNodes = 0


class SequencingPage(RenderableResource):
    """
    The PreferencesPage is responsible for managing eXe preferences
    """
    name = 'sequencing'

    browsersAvalaibles = []

    def __init__(self, parent, packRoot = None):
        """
        Initialize
        """
        RenderableResource.__init__(self, parent)
        self.pacRoot = packRoot
        self.Nodes = []
        self.nodetemp = []
        global Nodestest
        Nodestest = []
        if self.pacRoot:
            self.nodetemp = self.__getNodeOptions(self.pacRoot, 0)



    def __getNodeOptions(self, node, depth):
        Nodestest.append({'value': node.titleLong, 'text': u'&nbsp;&nbsp;&nbsp;'*node.level + node.titleLong + self.__isQuizz(node.idevices)})
        for child in node.children:
            self.__getNodeOptions(child, depth + 1)
        return True

    def __isQuizz(self, idevices):
        for idevice in idevices:
            if "QuizTestIdevice" in str(type(idevice)):
                return " ( "+ str(self.__numQuizz(idevices)) + " Quiz)"
        return ""

    def __numQuizz(self, idevices):
        numq = 0
        for idevice in idevices:
            if "QuizTestIdevice" in str(type(idevice)):
                numq += 1
        return numq


    def render_GET(self, request):

        self.Nodes = Nodestest
        return json.dumps({'success': True, 'Nodes': self.Nodes})


    def render_POST(self, request):
        """
        function replaced by nevow_clientToServerEvent to avoid POST message
        """

        log.debug("render_POST " + repr(request.args))
        data = {}
        try:
            a = 1
        except Exception as e:
            log.exception(e)

        return json.dumps({'success': True, 'data': data})


