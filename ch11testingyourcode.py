#you’ll learn to test your code using tools in Python’s unittest module.
def get_formatted_name(first, last):
	full_name = first + ' ' + last
	return full_name.title()
while True:
	first = input("\nInput first name.  Type q to quit. ")
	if first == "q":
		break
	last = input("Input last name.  Type q to quit.  ")
	if last == "q":
		break
	formatted_name = get_formatted_name(first, last)
	print(formatted_name)

#Python provides an efficient way to automate the testing of a function’s output. If we automate the testing of get_formatted_name(), we can always be confident that the function will work when given the kinds of names we’ve written tests for.

#Unit Tests and Test Cases
#The module unittest from the Python standard library provides tools for testing your code. A unit test verifies that one specific aspect of a function’s behavior is correct. A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.
#To write a test case for a function, import the unittest module and the function you want to test. Then create a class that inherits from unittest.TestCase, and write a series of methods to test different aspects of your function’s behavior.
import unittest
#we create a class called NamesTestCase, which will contain a series of unit tests for get_formatted_name().  You can name the class anything you want, but it’s best to call it something related to the function you’re about to test and to use the word Test in the class name.  This class must inherit from the class unittest.TestCase so Python knows how to run the tests you write.
class NamesTestCase(unittest.TestCase):
	#NamesTestCase contains a single method that tests one aspect of get_formatted_name().  Any method that starts with test_ will be run automatically.
	def test_firstlastname(self):
		#we call the function we want to test and store a return value that we’re interested in testing.
		formatted_name = get_formatted_name("janis","joplin")
		#we use one of unittest’s most useful features: an assert method. Assert methods verify that a result you received matches the result you expected to receive.
		self.assertEqual(formatted_name, "Janis Joplin")
unittest.main()

#To make middle names optional, we move the parameter middle to the end of the parameter list in the function definition and give it an empty default value. We also add an if test that builds the full name properly, depending on whether or not a middle name is provided.
def get_formatted_name2(first, last, middle=''):
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

#Adding New Tests
#let’s write a second test for people who include a middle name. We do this by adding another method to the class NamesTestCase:
class NamesTestCase(unittest.TestCase):
	def test_firstlastname(self):
		formatted_name = get_formatted_name2("janis","joplin")
		self.assertEqual(formatted_name, "Janis Joplin")
	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name2('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()
#IT APPEARS I CAN RUN ONE TEST ONLY.  THE TWO TESTS I WROTE SO FAR PYTHON3.5 RUNS THE FIRST TEST.  ALSO IT APPEARS A TEST ENDS THE PYTHON FILE.

#11-1 (222)
def get_formatted_country(city, country):
	full_country = city + ", " + country
	return full_country.title()
while True:
	city = input("\nInput a city.  Type q to quit. ")
	if city == "q":
		break
	country = input("Input the city's country.  Type q to quit. ")
	if country == "q":
		break
	formatted_country = get_formatted_country(city, country)
	print(formatted_country)
import unittest
class CityCountryTest(unittest.TestCase):
	def test_citycountry(self):
		formatted_citycountry = get_formatted_country("san jose","united states")
		self.assertEqual(formatted_citycountry, "San Jose, United States")
unittest.main()

#11-2(222)
def get_formatted_country2(city, country, population=''):
	if population:
		full_country = city + ", " + country + " - " +population
	else:
		full_country = city + ", " + country
	return full_country.title()
while True:
	city = input("\nInput a city.  Type q to quit. ")
	if city == "q":
		break
	country = input("Input the city's country.  Type q to quit. ")
	if country == "q":
		break
	population = input(str("Input the city's population.  Type q to quit. "))
	if population == "q":
		break
	formatted_country = get_formatted_country2(city, country, population)
	print(formatted_country)
import unittest
class CityCountryTest(unittest.TestCase):
	def test_citycountry(self):
		formatted_citycountry = get_formatted_country2("san jose","united states")
		self.assertEqual(formatted_citycountry, "San Jose, United States")
	def test_citycountrypopulation(self):
		formatted_citycountry = get_formatted_country2("san jose","united states","1008000")
		self.assertEqual(formatted_citycountry,"San Jose, United States - 1008000")
unittest.main()

#Testing a Class
Python provides a number of assert methods in the unittest.TestCase class.
Table 11-1 on page 223 describes six commonly used assert methods:
assertEqual(a, b) Verify that a == b
assertNotEqual(a, b) Verify that a != b
assertTrue(x) Verify that x is True
assertFalse(x) Verify that x is False
assertIn(item, list) Verify that item is in list
assertNotIn(item, list) Verify that item is not in list

#A Class to Test or Testing Class
class AnonymousSurvey():
	"""Collect anonymous answers to a survey question."""
	def __init__(self, question):
		"""Store a question, and prepare to store responses."""
		self.question = question
		self.responses = []
	def show_question(self):
		"""Show the survey question."""
		print(question)
	def store_response(self, new_response):
		"""Store a single response to the survey."""
		self.responses.append(new_response)
	def show_results(self):
		"""Show all the responses that have been given."""
		print("Survey results:")
		for response in self.responses:
			print('- ' + response)
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
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

#Testing the AnonymousSurvey Class
import unittest

#We call our test case TestAnonymousSurvey, which again inherits from unittest.TestCase
class TestAnonmyousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""
	#verify that when we store a response to the survey question, the response ends up in the survey’s list of responses. A good descriptive name for this method is test_store_single_response()
	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		question = "What language did you first learn to speak?"
		#we create an instance called my_survey with the question "What language did you first learn to speak?" We store a single response, English, using the store_response() method.
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		#verify that the response was stored correctly by asserting that English is in the list my_survey.responses
		self.assertIn('English', my_survey.responses)
	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		question = "What language did you first learn to speak?"
		my_survey = AnonymousSurvey(question)
		responses = ['English', 'Spanish', 'Mandarin']
		for response in responses:
			my_survey.store_response(response)
		for response in responses:
			self.assertIn(response, my_survey.responses)	
unittest.main()

#The setUp() Method
#The unittest.TestCase class has a setUp() method that allows you to create these objects once and then use them in each of your test methods. When you include a setUp() method in a TestCase class, Python runs the setUp() method before running each method starting with test_. Any objects created in the setUp() method are then available in each test method you write.
#Let’s use setUp() to create a survey instance and a set of responses that can be used in test_store_single_response() and test_store_three_responses():
import unittest
class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey."""
	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		#The method setUp() does two things: it creates a survey instance and it creates a list of responses the next two lines below.
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

#11-3 (228)