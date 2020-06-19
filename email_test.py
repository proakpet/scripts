#!/usr/bin/env python3
import uniittest
from email import find_email

class EmailsTest(uniittest.TestCase):
	def test_basic(self):
		testcase = [None, "Bree", "Campbell"]
		expected = "bree@abc.edu"
		self.assertEqual(find_email(testcase),expected)

	def test_one_name(self):
		testcase = [None, "John"] 
		expected = "Missing parameters"
		self.assertEqual(find_email(testcase),expected)

	def test_two_name(self):
		testcase = [None, "Roy", "Cooper"]
		expected = "No email address found"
		self.assertEqual(find_email(testcase),expected)

if __name__ == '__main__':
	uniittest.main()