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
        #self.Nodes.append({'value': 'Home', 'text': 'Home'})
        #self.Nodes.append({'value': 'Title1', 'text': 'Title01'})

    def __isQuizz(self, idevices):
        for idevice in idevices:
            a= str(type(idevice))
            if "QuizTestIdevice" in str(type(idevice)):
                return " (Quiz)"
        return ""


    def render_GET(self, request):
        """Render the preferences"""
        # aa = u'This not a String:\n' + request
        # with io.open('C:\data3.txt', 'w', encoding='utf-8') as f:
        #    f.write(aa)
        #if self.pacRoot:
            # for child in self.pacRoot:
            # self.Nodes.append({'value': child.titleLong, 'text': child.titleLong})
        #    self.Nodes.append({'value': self.pacRoot.titleLong, 'text': self.pacRoot.titleLong})
        #else:
         #   self.Nodes.append({'value': 'NotOK', 'text': 'NoteOK'})
        #self.Nodes = Nodestest[len(Nodestest)-4:len(Nodestest)]
        self.Nodes = Nodestest
        #a = numNodes
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


