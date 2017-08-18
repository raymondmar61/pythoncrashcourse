#Python Crash Course Chapter 11 Testing Your Code
#you’ll learn to test your code using tools in Python’s unittest module. You’ll learn to build a test case and check that a set of inputs results in the output you want. You’ll see what a passing test looks like and what a failing test looks like, and you’ll learn how a failing test can help you improve your code. You’ll learn to test functions and classes, and you’ll start to understand how many tests to write for a project.

#ch11name_function is the file name ch11name_function.py in same directory.  get_formatted_name is the name of the function in ch11name_function.py.
from ch11name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break
	formatted_name = get_formatted_name(first, last)
	print("\tNeatly formatted name: " + formatted_name + '.')

#The module unittest from the Python standard library provides tools for testing your code. A unit test verifies that one specific aspect of a function’s behavior is correct. A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle. A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function. Achieving full coverage on a large project can be daunting. It’s often good enough to write tests for your code’s critical behaviors and then aim for full coverage only if the project starts to see widespread use.
# import unittest
# from ch11name_function import get_formatted_name #ch11name_function is the file name ch11name_function.py in same directory.  get_formatted_name is the name of the function in ch11name_function.py.
# class NamesTestCase(unittest.TestCase):
# 	"""Tests for ch11name_function.py"""
# 	def test_first_last_name(self): #Any method that starts with test_ will be run automatically
# 		"""Do names like 'Janis Joplin' work?"""
# 		formatted_name = get_formatted_name('janis', 'joplin')
# 		self.assertEqual(formatted_name, 'Janis Joplin') #Assert methods verify that a result you received matches the result you expected to receive.  In this case, we expect Janis Joplin
# 	def test_first_last__middle_name(self): #Any method that starts with test_ will be run automatically
# 		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
# 		formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
# 		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart') #Assert methods verify that a result you received matches the result you expected to receive.  In this case, we expect Wolfgang Amadeus Mozart
# unittest.main() #return Ran 2 tests in 0.000s\n\n OK if passed

#Table 11-1 describes six commonly used assert methods.
"""
assertEqual(a, b) Verify that a == b
assertNotEqual(a, b) Verify that a != b
assertTrue(x) Verify that x is True
assertFalse(x) Verify that x is False
assertIn(item, list) Verify that item is in list
assertNotIn(item, list) Verify that item is not in list
"""
from ch11survey import AnonymousSurvey
# Define a question, and make a survey.
question ="What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)
# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# import unittest
# from ch11survey import AnonymousSurvey
# class TestAnonmyousSurvey(unittest.TestCase):
# 	"""Tests for the class AnonymousSurvey"""
# 	def test_store_single_response(self):
# 		"""Test that a single response is stored properly."""
# 		question = "What language did you first learn to speak?"
# 		my_survey = AnonymousSurvey(question)
# 		my_survey.store_response('English')
# 		self.assertIn('English', my_survey.responses) #Verify that item is in list
# 	def test_store_three_responses(self):
# 		"""Test that three individual responses are stored properly."""
# 		question = "What language did you first learn to speak?"
# 		my_survey = AnonymousSurvey(question)
# 		responses = ['English', 'Spanish', 'Mandarin']
# 		for response in responses:
# 			my_survey.store_response(response)
# 		for response in responses:
# 			self.assertIn(response, my_survey.responses)
# unittest.main()

#The unittest.TestCase class has a setUp() method that allows you to create these objects once and then use them in each of your test methods. When you include a setUp() method in a TestCase class, Python runs the setUp() method before running each method starting with test_. Any objects created in the setUp() method are then available in each test method you write.
import unittest
from ch11survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey."""
	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']
	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
unittest.main()
#When you’re testing your own classes, the setUp() method can make your test methods easier to write. You make one set of instances and attributes in setUp() and then use these instances in all your test methods. This is much easier than making a new set of instances and attributes in each test method.