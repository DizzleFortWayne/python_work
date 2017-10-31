##page 225 in the book

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""tests AnonymousSurvey Class"""
	def test_store_single_response(self):
		"""test that a single response is stored properly"""
		question="What language did you first learn to speak?"
		my_survey=AnonymousSurvey(question)
		my_survey.store_response('English')
		
		self.assertIn('English', my_survey.responses)
		
unittest.main()

