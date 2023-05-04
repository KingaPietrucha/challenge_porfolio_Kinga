import unittest

from unittest.loader import makeSuite

from test_cases.change_language import TestChangeLanguage
from test_cases.dev_team_contact_test import TestDevTeamContactClick
from test_cases.fill_add_player import TestAddAPlayer
from test_cases.log_out import TestLogOut
from test_cases.login_to_the_system import TestLoginPage
from test_cases.players_button_test import TestPlayersButton



def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLogOut))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestPlayersButton))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestDevTeamContactClick))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())

def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestChangeLanguage))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())



def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestAddAPlayer))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
