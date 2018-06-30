import sys
import unittest
from selenium import *

#sys.path.insert(0, '..')
import sys
sys.path.insert(0, '..')


# All Questions
from testing.selenium.unittest.scormtest.scormtestallquestions import ScormTestAllQuestions

# All level
from testing.selenium.unittest.scormtest.scormtestalllevel import ScormTestAllLevel

# No hard
from testing.selenium.unittest.scormtest.scormtestnohard import ScormTestNoHard

# No medium
from testing.selenium.unittest.scormtest.scormtestnomedium import ScormTestNoMedium

# No Easy
from testing.selenium.unittest.scormtest.scormtestnoeasy import ScormTestNoEasy


# ===========================================================================

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # All Questions
    suite.addTest(unittest.makeSuite(ScormTestAllQuestions))

    # All level
    suite.addTest(unittest.makeSuite(ScormTestAllLevel))

    # No hard
    suite.addTest(unittest.makeSuite(ScormTestNoHard))

    # No medium
    suite.addTest(unittest.makeSuite(ScormTestNoMedium))

    # No Easy
    suite.addTest(unittest.makeSuite(ScormTestNoEasy))



    result =unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)

