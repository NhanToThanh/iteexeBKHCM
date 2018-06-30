import sys
from selenium import *

#sys.path.insert(0, '..')
import sys
sys.path.insert(0, '..')
import unittest


# Normal
from testing.selenium.unittest.sequencing.normal.testtopdown import TestTopDown
from testing.selenium.unittest.sequencing.normal.testmultioutput import TestMultiOutput

# Have time
from testing.selenium.unittest.sequencing.havetime.testtimetopdown import TestTimeTopDown
from testing.selenium.unittest.sequencing.havetime.testtimemultioutput import TestTimeMultiOutput


# Have quiz
from testing.selenium.unittest.sequencing.havequiz.testpassallquiz import TestPassAllQuiz
from testing.selenium.unittest.sequencing.havequiz.testpassanyquiz import TestPassAnyQuiz
from testing.selenium.unittest.sequencing.havequiz.testpassonequiz import TestPassOneQuiz
from testing.selenium.unittest.sequencing.havequiz.testpasstwoquiz import TestPassTwoQuiz


# Mix
from testing.selenium.unittest.sequencing.mix.testmix1 import TestMix1
from testing.selenium.unittest.sequencing.mix.testmix2 import TestMix2
from testing.selenium.unittest.sequencing.mix.testmix3 import TestMix3


# ===========================================================================

if __name__ == "__main__":
    suite = unittest.TestSuite()

    #Normal
    suite.addTest(unittest.makeSuite(TestTopDown))
    suite.addTest(unittest.makeSuite(TestMultiOutput))

    # Have time
    suite.addTest(unittest.makeSuite(TestTimeTopDown))
    suite.addTest(unittest.makeSuite(TestTimeMultiOutput))

    # Have quiz
    suite.addTest(unittest.makeSuite(TestPassOneQuiz))
    suite.addTest(unittest.makeSuite(TestPassTwoQuiz))
    suite.addTest(unittest.makeSuite(TestPassAllQuiz))
    suite.addTest(unittest.makeSuite(TestPassAnyQuiz))

    # Mix
    suite.addTest(unittest.makeSuite(TestMix1))
    suite.addTest(unittest.makeSuite(TestMix2))
    suite.addTest(unittest.makeSuite(TestMix3))


    result =unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)

