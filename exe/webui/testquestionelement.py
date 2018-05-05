# ===========================================================================
# eXe 
# Copyright 2004-2006, University of Auckland
# Copyright 2004-2008 eXe Project, http://eXeLearning.org
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
TestQuestionElement is responsible for a block of question.  
Used by QuizTestBlock for SCORM Quiz
"""

import logging
from exe.webui.testoptionelement import TestoptionElement
from exe.webui import common
from exe.webui.element import TextAreaElement

log = logging.getLogger(__name__)


# ===========================================================================
class TestquestionElement(object):
    """
    TestQuestionElement is responsible for a block of question.  
    Used by QuizTestBlock
    == SCORM Quiz Testquestion, 
    pretty much the same as MultiSelect's SelectquestionElement
    """

    def __init__(self, index, idevice, question):
        """
        Initialize
        """
        self.index = index
        self.id = unicode(index) + "b" + idevice.id
        self.idevice = idevice

        # to compensate for the strange unpickling timing when objects are 
        # loaded from an elp, ensure that proper idevices are set:
        if question.questionTextArea.idevice is None:
            question.questionTextArea.idevice = idevice
        self.questionElement = TextAreaElement(question.questionTextArea)
        #self.tagElement = TextAreaElement(question.tagTextArea)

        self.question = question
        self.tag = ""

        self.questionId = "question" + self.id
        self.questionElement.id = self.questionId

        #self.tagId = "tag" + self.id
        #self.tagElement.id = self.tagId

        self.options = []
        self.keyId = "key" + self.id
        i = 0
        for option in question.options:
            self.options.append(TestoptionElement(i,
                                                  question,
                                                  self.id,
                                                  option,
                                                  idevice))
            i += 1


    def process(self, request):
        """
        Process the request arguments from the web server
        """
        log.info("process " + repr(request.args))
        if self.questionId in request.args:
            self.questionElement.process(request)

        #if self.tagId in request.args:
        #    self.tagElement.process(request)


        if ("addOption" + unicode(self.id)) in request.args:
            self.question.addOption()
            self.idevice.edit = True
            # disable Undo once an option has been added:
            self.idevice.undo = False

        if "d" + self.keyId in request.args:
            if request.args["d" + self.keyId][0][0] == 'h':
                self.question.isHard = True
                self.question.isMedium = False
                self.question.isEasy = False
                log.debug("hard check " + repr(self.question.isHard))
            elif request.args["d" + self.keyId][0][0] == 'm':
                self.question.isMedium = True
                self.question.isHard = False
                self.question.isEasy = False
                log.debug("medium check " + repr(self.question.isMedium))
            elif request.args["d" + self.keyId][0][0] == 'e':
                self.question.isEasy = True
                self.question.isHard = False
                self.question.isMedium = False
                log.debug("ez check " + repr(self.question.isEasy))
            else:
                self.question.isHard = False
                self.question.isMedium = False
                self.question.isEasy = False


        if "action" in request.args and request.args["action"][0] == self.id:
            # before deleting the question object, remove any internal anchors:
            for q_field in self.question.getRichTextFields():
                q_field.ReplaceAllInternalAnchorsLinks()
                q_field.RemoveAllInternalLinks()
            self.idevice.questions.remove(self.question)
            # disable Undo once a question has been deleted:
            self.idevice.undo = False



        for element in self.options:
            element.process(request)

    def renderEdit(self):
        """
        Returns an XHTML string with the form element for editing this element
        """
        html = u"<div class=\"iDevice\">\n"
        html += common.submitImage(self.id, self.idevice.id,
                                   "/images/stock-cancel.png",
                                   _("Delete question"))
        html += self.questionElement.renderEdit()

        lb = "\n"
        fieldId = self.keyId + unicode((self.index + 1));
        #html += '<p class="iDevice_answer-field js-required">' + lb
        #html += '<label for="' + fieldId + '" class="sr-av"><a href="#answer-' + fieldId + '">' + c_(
        #    "Option") + ' ' + unicode((self.index + 1)) + '</a></label>'
        html += '<strong id="diff-label" style="margin-right: 5px;">Set the Diffuculty: </strong>'
        html += common.option("d" + self.keyId,
                              self.question.isHard, "h"+fieldId)
        html += ' Hard&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        html += common.option("d" + self.keyId,
                              self.question.isMedium, "m" + fieldId)
        html += ' Muedium &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        html += common.option("d" + self.keyId,
                              self.question.isEasy, "e" + fieldId)
        html += ' Easy &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'


        #html += lb
        #html += '</p>' + lb
        html += '<br>'

        html += u"<table width =\"100%%\">"
        html += u"<thead>"
        html += u"<tr>"
        html += u"<th>%s " % _("Options")
        html += common.elementInstruc(self.question.optionInstruc)
        html += u"</th>"
        html += u"</tr>"
        html += u"</thead>"
        html += u"<tbody>"

        for element in self.options:
            html += element.renderEdit()

        html += u"</tbody>"
        html += u"</table>\n"
        value = _(u"Add another Option")
        html += common.submitButton("addOption" + unicode(self.id), value)
        html += u"<br />"
        html += u"</div>\n"

        return html

    def renderPreview(self):
        """
        Returns an XHTML string for previewing this element
        """
        return self.renderView(preview=True)

    def renderView(self, preview=False):
        """
        Returns an XHTML string for viewing this element
        """
        lb = "\n"  # Line breaks
        dT = common.getExportDocType()
        sectionTag = "div"
        titleTag1 = "h3"
        titleTag2 = "h4"
        if dT == "HTML5":
            sectionTag = "section"
            titleTag1 = "h1"
            titleTag2 = "h1"
        typeStr = ""
        if self.question.isHard:
            typeStr += "(Hard"
        elif self.question.isMedium:
            typeStr += "(Medium"
        elif self.question.isEasy:
            typeStr += "(Easy"
        else:
            pass

        if hasattr(self.question, "isOnTest"):
            if self.question.isOnTest:
                typeStr += ", This Questions is on Test)"
            else:
                typeStr += ")"
        else:
            typeStr += ")"
        html = ''
        html += '<' + sectionTag + ' class="question">' + lb
        html += '<' + titleTag1 + ' class="js-sr-av">' + c_("Question") + '</' + titleTag1 + '>' + lb
        if preview:
            html += self.questionElement.renderPreview(typeStr = typeStr)
        else:
            html += self.questionElement.renderView(typeStr = typeStr)
        # Answers
        html += '<' + sectionTag + ' class="iDevice_answers">' + lb
        html += '<' + titleTag2 + ' class="js-sr-av">' + c_("Answers") + '</' + titleTag2 + '>' + lb
        for element in self.options:
            if preview:
                html += element.renderPreview()
            else:
                html += element.renderView()
        html += "</" + sectionTag + ">" + lb

        html += "</" + sectionTag + ">" + lb

        return html

    def getCorrectAns(self):
        """
        return the correct answer for the question
        """
        return self.question.correctAns

    def getNumOption(self):
        """
        return the number of options
        """
        return len(self.question.options)

# ===========================================================================