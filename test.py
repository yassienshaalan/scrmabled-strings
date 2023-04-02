import unittest
from mock import patch, MagicMock
import io
import os
import importlib
module_name = 'scrmabled-strings'
module = importlib.import_module(module_name)


class TestCode(unittest.TestCase):
    def test_key_class(self):
        # Test the Key class's __eq__() method
        key1 = module.Key('a', 'b')
        key2 = module.Key('a', 'b')
        self.assertEqual(key1, key2)
        print("Key class __eq__() method match 1test passed.")

        key3 = module.Key('a', 'c')
        self.assertNotEqual(key1, key3)
        print("Key class __eq__() method match 2 test passed.")

        # Test the Key class's __hash__() method
        d = {key1: 1}
        self.assertEqual(d[key2], 1)
        print("Key class __hash__() method match 3 test passed.")

    def test_make_key(self):
        # Test the make_key() function
        word1 = 'hello'
        key1 = module.Key('h', 'o')
        key1.freq = [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        s = module.ScrmabledStringsSolver("","")
        self.assertEqual(s.make_key(word1), key1)
        print("make_key() function matching match test 4 passed.")

        word2 = 'world'
        key2 = module.Key('w', 'd')
        key2.freq = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(s.make_key(word2), key2)
        print("make_key() function matching match test 5 passed.")

    def test_count_words(self):
        # Test the count_words() function
        dictionary = ['hello', 'world', 'hell', 'held', 'word']
        text = 'helloworld'
        s = module.ScrmabledStringsSolver("","")
        self.assertEqual(s.count_words(dictionary, text), 3)
        print("count_words() function test 1 passed.")

        dictionary = ['hello', 'world', 'hell', 'held', 'word']
        text = 'worldhello'
        self.assertEqual(s.count_words(dictionary, text), 3)
        print("count_words() function test 2 passed.")

        dictionary = ['hello', 'world', 'hell', 'held', 'word']
        text = 'hld'
        self.assertEqual(s.count_words(dictionary, text), 0)
        print("count_words() function test 3 passed.")
        
    def test_read_dictionary_file(self):
        # Test the function that reads the dictionary file
        # Get the absolute path of the input file relative to the current working directory
        s = module.ScrmabledStringsSolver("","")
        file_path = os.path.join(os.getcwd(), 'testing_data', 'test_dict.txt')
        words = s.read_dictionary_file(file_path)
        # Check that the number of words in the set is correct
        self.assertEqual(len(words), 5)
        print("read_dictionary_file() function 1 test passed.")

        # Check that the expected words are in the set
        expected_words = {"This", "is", "just", "a", "Test"}
        if set(words) == expected_words:
            print("Expected words found in set 2 test.")
        else:
            print("ERROR: Expected words not found in set.")

    def test_read_input_file(self):
        # Test the function that reads the input file.
        # Get the absolute path of the input file relative to the current working directory
        s = module.ScrmabledStringsSolver("","")
        file_path = os.path.join(os.getcwd(), 'testing_data', 'test_input.txt')
        lines = s.read_input_file(file_path)
        # Check that the number of lines read from the file is correct.
        self.assertEqual(len(lines), 3)
        # Check that the lines read from the file are correct.
        self.assertEqual(lines[0], "hello world")
        self.assertEqual(lines[1], "python is awesome")
        self.assertEqual(lines[2], "programming is fun")
        
        # Print statement describing the output
        if len(lines) == 3 and lines[0] == "hello world" and lines[1] == "python is awesome" and lines[2] == "programming is fun":
            print("Output of test_read_input_file(): Good")
        else:
            print("Output of test_read_input_file(): Bad")


    def test_main(self):
        # Test the main function that processes the input and dictionary files and writes the output file.
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            module.main("testing_data/test_dict_1.txt", "testing_data/test_input_1.txt")
            # Check that the output of the function matches the expected output.
            expected_output = "Case #1: 10\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            
            # Print statement describing the output
            if mock_stdout.getvalue() == expected_output:
                print("Output of test_main() (test_dict_1.txt, test_input_1.txt): Good")
            else:
                print("Output of test_main() (test_dict_1.txt, test_input_1.txt): Bad")

        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            module.main("testing_data/test_dict_2.txt", "testing_data/test_input_2.txt")
            # Check that the output of the function matches the expected output.
            expected_output = "Case #1: 4\nCase #2: 2\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            
            # Print statement describing the output
            if mock_stdout.getvalue() == expected_output:
                print("Output of test_main() (test_dict_2.txt, test_input_2.txt): Good")
            else:
                print("Output of test_main() (test_dict_2.txt, test_input_2.txt): Bad")

        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            module.main("testing_data/test_dict_3.txt", "testing_data/test_input_3.txt")
            # Check that the output of the function matches the expected output.
            expected_output = "Case #1: 1\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            
            # Print statement describing the output
            if mock_stdout.getvalue() == expected_output:
                print("Output of test_main() (test_dict_3.txt, test_input_3.txt): Good")
            else:
                print("Output of test_main() (test_dict_3.txt, test_input_3.txt): Bad")



if __name__ == "__main__":

    unittest.main()
       
