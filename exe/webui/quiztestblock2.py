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
QuizTestBlock can render and process QuizTestIdevices as XHTML
"""

import logging
from exe.webui.block import Block
from exe.webui.testquestionelement import TestquestionElement
from exe.webui import common

log = logging.getLogger(__name__)


# ===========================================================================
class QuizTestBlock2(Block):
    """
    QuizTestBlock can render and process QuizTestIdevices as XHTML
    """

    def __init__(self, parent, idevice):
        """
        Initialize a new Block object
        """
        Block.__init__(self, parent, idevice)
        self.idevice = idevice
        self.questionElements = []
        self.message = False
        self.allQuizTitles = []
        self.questionsOutput = []
        if not hasattr(self.idevice, 'undo'):
            self.idevice.undo = True

        i = 0
        for question in idevice.questions:
            self.questionElements.append(TestquestionElement(i, idevice,
                                                             question))
            i += 1

    def process(self, request):
        """
        Process the request arguments from the web server
        """
        Block.process(self, request)

        is_cancel = common.requestHasCancel(request)

        if ("addQuestion" + unicode(self.id)) in request.args:
            self.idevice.addQuestion()
            self.idevice.edit = True
            # disable Undo once a question has been added:
            self.idevice.undo = False

        if "passrate" in request.args \
                and not is_cancel:
            self.idevice.passRate = request.args["passrate"][0]

        for element in self.questionElements:
            element.process(request)



        for title in self.allQuizTitles:#chay tung cai test
            if (str(title[0]) + "hard") in request.args:
                numHard = -1
                if (request.args[str(title[0]) + "hard"][0] != u""):
                    numHard = int(request.args[str(title[0]) + "hard"][0])
                    if numHard > title[1]:
                        numHard = title[1]
                else:
                    numHard = -1
                numMed = -1
                if (request.args[str(title[0]) + "med"][0] != u""):
                    numMed = int(request.args[str(title[0]) + "med"][0])
                    if numMed > title[2]:
                        numMed = title[2]
                else:
                    numMed = -1
                numEasy = -1
                if (request.args[str(title[0]) + "easy"][0] != u""):
                    numEasy = int(request.args[str(title[0]) + "easy"][0])
                    if numEasy > title[3]:
                        numEasy = title[3]
                else:
                    numEasy = -1

                for question in self.questionElements:
                    if question.question.idevice._title in str(title[0]) and question.question.isHard:
                        if numHard <= 0:
                            pass
                        else:
                            self.idevice.questionsOutput.append(question.question)
                            question.question.isOnTest = True
                            numHard -= 1
                    if question.question.idevice._title in str(title[0]) and question.question.isMedium:
                        if numMed <= 0:
                            pass
                        else:
                            self.idevice.questionsOutput.append(question.question)
                            question.question.isOnTest = True
                            numMed -= 1
                    if question.question.idevice._title in str(title[0]) and question.question.isEasy:
                        if numEasy <= 0:
                            pass
                        else:
                            self.idevice.questionsOutput.append(question.question)
                            question.question.isOnTest = True
                            numEasy -= 1



        if ("action" in request.args and request.args["action"][0] == "done"
                or not self.idevice.edit):
            self.idevice.isAnswered = True
            # remove the undo flag in order to reenable it next time:
            if hasattr(self.idevice, 'undo'):
                del self.idevice.undo
            for question in self.idevice.questions:
                if question.correctAns == -2:
                    self.idevice.isAnswered = False
                    self.idevice.edit = True
                    break

        if "submitScore" in request.args \
                and not is_cancel:
            self.idevice.score = self.__calcScore()

        if "title" + self.id in request.args \
                and not is_cancel:
            self.idevice.title = request.args["title" + self.id][0]


    def renderEdit(self, style):
        """
        Returns an XHTML string with the form element for editing this block
        """
        html = "<div class=\"iDevice\">\n"
        if not self.idevice.isAnswered:
            html += common.editModeHeading(
                _("Please select a correct answer for each question."))
        #if self.allQuizTitles.count(self.idevice.title) != 1:
        #    html += common.editModeHeading(
        #        _("PTitle must bu unique."))
        #for title in self.allQuizTitles:
        #    if
        html += common.textInput("title" + self.id, self.idevice.title)
        html += u"<br/><br/>\n"


        for element in self.questionElements:
            html += element.renderEdit()

        value = _("Add another Question")
        html += "<br/>"
        html += common.submitButton("addQuestion" + unicode(self.id), value)
        html += "<br/><br/>" + _("Select pass rate: ")
        html += "<select name=\"passrate\">\n"
        template = '  <option value="%s0"%s>%s0%%</option>\n'
        for i in range(1, 11):
            if str(i) + "0" == self.idevice.passRate:
                html += template % (str(i), ' selected="selected"', str(i))
            else:
                html += template % (str(i), '', str(i))
        html += "</select>\n"
        self.allQuizTitles = []
        self.__getAllQuizTitles(self.package.root, 0)

        html += "<br/><br/>"
        html += "<strong>PLease enter the number of quiz to appear in the Test, If the entered number greater than the number of Quiz, the maximun number of Quiz is set.</strong>"
        html += "<br/>"
        for title in self.allQuizTitles:
            html += '<strong id="diff-label" style="margin-right: 5px;">%s: </strong>'%title[0]
            html += "<br/>"
            html += '<span>Enter number of Hard(Max: %s)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: </span>'%str(title[1])
            html += common.textInput(str(title[0]) +"hard")
            html += "<br/>"
            html += '<span>Enter number of Medium(Max: %s)&nbsp;: </span>'%str(title[2])
            html += common.textInput(str(title[0]) +"med")
            html += "<br/>"
            html += '<span>Enter number of Easy(Max: %s)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: </span>'%str(title[3])
            html += common.textInput(str(title[0]) +"easy")
            html += "<br/><br/>"

        html += "<br /><br />" + self.renderEditButtons(undo=self.idevice.undo)
        html += "</div>\n"
        self.idevice.isAnswered = True

        return html

    def __getAllQuizTitles(self, Rooot, depth):
        for idevice in Rooot.idevices:
            if  hasattr(idevice, "isQuiz"):
                a, b, c = self.__getHardMediumEasy(idevice.questions)
                self.allQuizTitles.append([idevice._title, a, b, c])
        for child in Rooot.children:
            self.__getAllQuizTitles(child, depth + 1)
        return True

    def __getHardMediumEasy(self, questions):
        numHard = 0
        numMed  = 0
        numEasy = 0
        for question in questions:
            if question.isHard:
                numHard += 1
            elif question.isMedium:
                numMed  += 1
            elif question.isEasy:
                numEasy += 1
        return numHard, numMed, numEasy

    def renderView(self, style, preview=False, numQ=None):
        """
        Returns an XHTML string for viewing this block
        """
        lb = "\n"  # Line breaks
        html = common.ideviceHeader(self, style, "view")
        html += '<form name="quizForm%s" id="quizForm%s" action="javascript:calcScore2();">' % (
        self.idevice.id, self.idevice.id)
        html += lb
        html += u'<input type="hidden" name="passrate" id="passrate-' + self.idevice.id + '" value="' + self.idevice.passRate + '" />' + lb
        for element in self.questionElements:
            if preview:
                html += element.renderPreview()
            else:
                html += element.renderView()
        html += '<div class="block iDevice_buttons">' + lb
        html += '<p><input type="submit" name="submitB" value="' + c_(
            "SUBMIT ANSWERS") + '"  onclick="calcScore2%s()" /> ' % numQ + '</p>' + lb
        html += '</div>' + lb
        html += '<div id="quizFormScore' + self.id + '"></div>' + lb
        html += '</form>' + lb
        html += common.ideviceFooter(self, style, "view")
        return html

    def renderJavascriptForWeb(self):
        """
        Return an XHTML string for generating the javascript for web export
        """
        scriptStr = '<script type="text/javascript">/*<![CDATA[*/'
        scriptStr += '\n'
        scriptStr += "var numQuestions = "
        scriptStr += str(len(self.questionElements)) + ";\n"
        scriptStr += "var rawScore = 0;\n"
        scriptStr += "var actualScore = 0;\n"
        answerStr = """function getAnswer()
        {"""
        varStrs = ""
        keyStrs = ""
        answers = ""
        rawScoreStr = """}
        function calcRawScore(){\n"""

        for element in self.questionElements:
            i = element.index
            varStr = "question" + str(i)
            keyStr = "key" + str(i)
            quesId = "key" + str(element.index) + "b" + self.id
            numOption = element.getNumOption()
            answers += "var key" + str(i) + " = "
            answers += str(element.question.correctAns) + ";\n"
            getEle = 'document.getElementById("quizForm%s")' % \
                     self.idevice.id
            chk = '%s.%s[i].checked' % (getEle, quesId)
            value = '%s.%s[i].value' % (getEle, quesId)
            varStrs += "var " + varStr + ";\n"
            keyStrs += "var key" + str(i) + " = "
            keyStrs += str(element.question.correctAns) + ";\n"

            answerStr += """
            for (var i=0; i < %s; i++)
            {
               if (%s)
               {
                  %s = %s;
                  break;
               }
            }
            """ % (numOption, chk, varStr, value)

            rawScoreStr += """
            if (%s == %s)
            {
               rawScore++;
            }""" % (varStr, keyStr)

        scriptStr += varStrs
        scriptStr += keyStrs

        scriptStr += answerStr

        scriptStr += rawScoreStr

        scriptStr += """

        }

        function calcScore2()
        {
            getAnswer();

            calcRawScore();
            actualScore =  Math.round(rawScore / numQuestions * 100);
            var id = "%s";
            document.getElementById("quizForm"+id).submitB.disabled = true;
            var s = document.getElementById("quizFormScore"+id);
            """ % self.idevice.id
        scriptStr += '            var msg_str ="' + c_("Your score is %d%%") + '";'
        scriptStr += '            msg_str = msg_str.replace("%d",actualScore).replace("%%","%");'
        scriptStr += '            if (s) { s.innerHTML = "<div class=\'feedback\'><p>"+msg_str+"</p></div>"; } else { alert(msg_str); }'

        scriptStr += """

        }
    /*]]>*/</script>\n"""

        return scriptStr

    def renderJavascriptForScorm(self, thisnode=None, numQ=None):
        """
        Return an XHTML string for gene rating the javascript for scorm export
        """

        scriptStr = '''
        <script type="text/javascript">
    var QUESTION_TYPE_CHOICE = "choice";
    
    function Question(id, text, type, answers, correctAnswer, objectiveId){
        this.Id = id;
        this.Text = text;
        this.Type = type;
        this.Answers = answers;
        this.CorrectAnswer = correctAnswer;
        this.ObjectiveId = objectiveId;
    }

    function Test(questions){
        this.Questions = questions;
    }
    Test.prototype.AddQuestion = function(question)
    {
        this.Questions[this.Questions.length] = question;
    }
    
    var test = new Test(new Array());
</script>

<script src="questions.js" type="text/JavaScript"> </script>

<script type="text/javascript">
    function CheckNumeric(obj){
        var userText = new String(obj.value);
        var numbersRegEx = /[^0-9]/g;
        if (userText.search(numbersRegEx) >= 0){
            alert("Please enter only numeric values.");
            obj.value = userText.replace(numbersRegEx, "");
        }
    }

    function SubmitAnswers(){
        var correctCount = 0;
        var totalQuestions = test.Questions.length;
        
        var resultsSummary = "";
        
        for (var i in test.Questions){
            var question = test.Questions[i];
            
            var wasCorrect = false;
            var correctAnswer = null;
            var learnerResponse = "";
            
            switch (question.Type){
                case QUESTION_TYPE_CHOICE:
                    for (var answerIndex = 0; answerIndex < question.Answers.length; answerIndex++){ 
                        if (question.CorrectAnswer == question.Answers[answerIndex]){
                            correctAnswer = answerIndex;
                        }
                        if (document.getElementById("question_" + question.Id + "_" + answerIndex).checked == true){
                            learnerResponse = answerIndex;
                        }
                    }
                break;
            }
            
            wasCorrect = (correctAnswer == learnerResponse);
            if (wasCorrect) {correctCount++;}
            
            if (parent.RecordQuestion){
                parent.RecordQuestion(test.Questions[i].Id, 
                                        test.Questions[i].Text, 
                                        test.Questions[i].Type, 
                                        learnerResponse, 
                                        correctAnswer, 
                                        wasCorrect, 
                                        test.Questions[i].ObjectiveId);
            }
            
            resultsSummary += "<div class='questionResult'><h3>Question " + i + "</h3>";
            if (wasCorrect) {
                resultsSummary += "<em>Correct</em><br>"
            }
            else{
                resultsSummary += "<em>Incorrect</em><br>"
                
            }
            resultsSummary += "</div>";
        }
        var score = Math.round(correctCount * 100 / totalQuestions);
        
        
        if(score >= %s){//mode ANY
            resultsSummary += "<h3>You Pass the Test. Well done.</h3>";
            scorm.SetCompletionStatus("completed");
            scorm.SetSuccessStatus("passed");
            scorm.SetExit("");
            exitPageStatus = true;
            scorm.save();
            scorm.quit();
        }else{
            resultsSummary += "<h3>You Failed the Test</h3>";
            scorm.SetCompletionStatus("incomplete");
            scorm.SetSuccessStatus("failed");
            scorm.SetExit("");
            exitPageStatus = true;
            scorm.save();
            scorm.quit();
        }
        resultsSummary = "<h3>Score: " + score + "</h3>" + resultsSummary;
        
        
        document.getElementById("test").innerHTML = resultsSummary;
        
        if (parent.RecordTest){
            parent.RecordTest(score);
        }
    }
</script>

<script type="text/javascript">

    function RenderTest(test){
    	test.Questions.sort(function() {return 0.5 - Math.random()});
        document.write ("<div id='test'><form id='frmTest' action='#'>");
        
        for (var i in test.Questions){
            var question = test.Questions[i];
            
            document.write ("<div id='question_" + question.Id + "' class='question'>");
            document.write (question.Text);
            
            switch (question.Type){
                case QUESTION_TYPE_CHOICE:
                    var ansIndex = 0;
                    for (var j in question.Answers){
                        var answer = question.Answers[j];
                        document.write("<div ");
                        if (question.CorrectAnswer == answer) {document.write("class='correctAnswer'");} else{document.write("class='answer'");}
                        document.write("><input type='radio' name='question_" + question.Id + "_choices' id='question_" + question.Id + "_" + ansIndex + "'/>" + answer + "</div>");
                        ansIndex++;
                    }
                break; 
                default:
                    alert("invalid question type detected");
                break;
            }
            document.write ("</div>");      //close out question div
        }
        document.write("<input type='button' value='Submit Answers' onclick='SubmitAnswers();' />");
        document.write ("</form></div>");      //close out test div
    }
</script>
<script type="text/javascript">
    RenderTest(test);
    AddTagLine();
</script>
        '''%self.idevice.passRate

        return scriptStr

    def renderPreview(self, style):
        """
        Returns an XHTML string for previewing this block
        """
        lb = "\n"  # Line breaks
        html = common.ideviceHeader(self, style, "preview")

        html += u'<input type="hidden" name="passrate" id="passrate-' + self.idevice.id + '" value="' + self.idevice.passRate + '" />'

        for element in self.questionElements:
            html += element.renderPreview()

        html += '<div class="block iDevice_buttons">' + lb
        html += '<p><input type="submit" name="submitScore" value="' + c_("SUBMIT ANSWERS") + '" /></p>'
        html += '</div>' + lb

        if not self.idevice.score == -1:
            message = c_("Your score is %d%%") % self.idevice.score
            html += '<script type="text/javascript">alert("' + message + '")</script>'

        self.idevice.score = -1

        html += common.ideviceFooter(self, style, "preview")

        return html

    def __calcScore(self):
        """
        Return a score for preview mode.
        """
        rawScore = 0
        numQuestion = len(self.questionElements)
        score = 0

        for question in self.idevice.questions:
            if (question.userAns == question.correctAns):
                log.info("userAns " + unicode(question.userAns) + ": "
                         + "correctans " + unicode(question.correctAns))
                rawScore += 1

        if numQuestion > 0:
            score = rawScore * 100 / numQuestion

        for question in self.idevice.questions:
            question.userAns = -1

        return score

    # ===========================================================================


"""Register this block with the BlockFactory"""
from exe.engine.quiztestidevice2 import QuizTestIdevice2
from exe.webui.blockfactory import g_blockFactory

g_blockFactory.registerBlockType(QuizTestBlock2, QuizTestIdevice2)

# ===========================================================================
