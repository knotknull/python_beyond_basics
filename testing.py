#!/usr/bin/env python3.5
import os
import unittest

# unittest module can help with:
#       - unit tests
#       - integration tests
#       - acceptance tests
#
# TestCase: groups together related test functions
#           Basic unit of test organization in unittest
#
# fixtures: code run before and/or after each test function
#           setup / tear down resources needed for testing
#
# assertions: specific tests for conditions / behaviors, can check for:
#            - make boolean checks
#            - test for object equality
#            - check that correct exceptions are thrown
#            If assersion fails then test function fails, lowest level of test


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or can't be read.

    Returns: A tuple where the first element is number of lines and the
              second is number of characters
    """
    # pass  # empty function
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
        return (lines, chars)


class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    # This is a fixture, sets up the file that will be analyzed
    # this is run before each test case
    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_text_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Four score and 7 year ago\n'
                    'our Forefather brought forth a great nation\n'
                    'and ....... \n'
                    'a bunch of pizza')

    # Another fixture which cleans up the resources,
    # this is run after each test case
    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    # Create test cases by prefacing method with test_
    # test method will fail if it throws any exceptions
    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        print("test_function_runs:")
        analyze_text(self.filename)  # accessing filename created in setup

    # test case to check on line count
    def test_line_count(self):
        """Check that the line count is correct."""
        print("test_line-count:")
        self.assertEqual(analyze_text(self.filename)[0], 4)

    # test case to check on char count
    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 99)

    # test case to check if exception is thrown for missing file
    def test_no_such_file(self):
        """Check the proper exception is thrown for a missing file."""
        # Fail unless an exception of this type is raised
        with self.assertRaises(IOError):
            analyze_text('foobar')

    # test case to check that function doesn't delete file passed to it
    def test_no_deletion(self):
        """Check that the function doesn't delete the input file."""
        analyze_text(self.filename)
        # check that the assertion is true
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    # unittest.main() will search for all TestCase sub-classes in a module and
    # run all of their test cases
    unittest.main()
