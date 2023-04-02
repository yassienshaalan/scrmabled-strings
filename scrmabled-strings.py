import os
import logging
from datetime import datetime
import argparse
from typing import List,Set

class Key:
    # define a Key class with attributes first, last, and freq
    def __init__(self, first: str, last: str):
        """
        Initialize the Key object with the given first and last strings.
        Also initialize the freq attribute as a list of 26 zeros.

        Args:
            first (str): A string representing the first character of the key.
            last (str): A string representing the last character of the key.

        Returns:
            None
        """
        self.first = first
        self.last = last
        # initialize the freq attribute as a list of 26 zeros
        self.freq = [0] * 26
    
    # define an equality method for the Key class
    def __eq__(self, other) -> bool:
        """
        Define the equality method for the Key class.
        Check if the first, last, and freq attributes of self and other are equal.

        Args:
            other: Another object of the Key class to compare with.

        Returns:
            bool: True if the first, last, and freq attributes of self and other are equal, False otherwise.
        """
        return self.first == other.first and self.last == other.last and self.freq == other.freq

    # define a hash method for the Key class
    def __hash__(self) -> int:
        """
        Define the hash method for the Key class.
        Initialize hash value with sum of ASCII codes of first and last characters.
        Add hash value for each frequency count in freq list.

        Returns:
            int: The hash value for the Key object.
        """
        res = ord(self.first) + 31 * ord(self.last)
        # add hash value for each frequency count in freq list
        for i in self.freq:
            res = 31 * res + i
        return res

class ScrmabledStringsSolver:
    """
    A class to solve the Scrambled Strings problem given a dictionary file and an input file.
    """
    def __init__(self, dictionary_file: str, input_file: str):
        """
        Initializes a ScrmabledStringsSolver object with the given dictionary file and input file.

        Args:
            dictionary_file (str): The path to the file containing the list of words to be used as a dictionary.
            input_file (str): The path to the file containing the long strings of characters to be searched.
        """
        self.dictionary_file = dictionary_file
        self.input_file = input_file
        
        #Add a version to the output file naming for easy search and filtering in case of incident tracking
        self.version = 1

    # function to create a Key object from a given word
    def make_key(self,word: str) -> Key:
        """
        Creates a Key object from a given word, consisting of its first and last characters and frequency count.

        Args:
            word (str): The word to create a Key object for.

        Returns:
            Key: A Key object representing the given word.
        """
        key = Key(word[0], word[-1])
        # iterate over each character in the word and update the frequency count in key
        for ch in word:
            key.freq[ord(ch) - ord('a')] += 1
        # return the final Key object for the word
        return key


    # function to solve the problem given a dictionary and a text
    def count_words(self,dictionary: List[str], text: str) -> int:
        """
        Solves the Scrambled Strings problem given a list of words as a dictionary and the string to be searched.

        Args:
            dictionary (List[str]): A list of words to be used as a dictionary for solving the problem.
            text (str): The string to be searched.

        Returns:
            int: The number of words in the dictionary that can be found in its original form or in their scrambled form in the given string.
        """
        # initialize an empty dictionary to store groups of Key objects
        groups = {}
        # initialize an empty set to store unique word lengths in the dictionary
        word_lengths = set()
        # iterate over each word in the dictionary
        for word in dictionary:
            # add the length of the word to the set of word lengths
            word_lengths.add(len(word))
            # create a new Key object for the word
            key = self.make_key(word)
            # if the Key object already exists in the groups dictionary, increment its count
            if key in groups:
                groups[key] += 1
            # otherwise, add the Key object to the groups dictionary with a count of 1
            else:
                groups[key] = 1
        # initialize a variable to store the final answer
        answer = 0
        # iterate over each unique word length in the dictionary
        for length in word_lengths:
            # if the length is greater than the length of the text, skip it
            if length > len(text):
                continue
            # create a new Key object with empty first and last characters and freq list
            key = Key('', '')
            # iterate over the first length - 1 characters in the text and update freq counts in key
            for i in range(length - 1):
                key.freq[ord(text[i]) - ord('a')] += 1
            # iterate over the remaining characters in the text
            for i in range(length - 1, len(text)):
                # update the first and last characters in key
                key.first = text[i - (length - 1)]
                key.last = text[i]
                # update the freq count for the last character in key
                key.freq[ord(key.last) - ord('a')] += 1
                # if the Key object exists in the
                if key in groups:
                    answer += groups[key]
                    del groups[key]
                # update the freq count for the first character in key
                key.freq[ord(key.first) - ord('a')] -= 1
        # return the final answer
        return answer

    def read_dictionary_file(self,file_path: str) -> Set[str]:
        """
        Read dictionary file and return a set of words.

        Args:
            file_path (str): The path to the dictionary file.

        Returns:
            set: A set of words.
        """
        try:
            with open(file_path) as dict_file:
                # Create a set of stripped words from the file.
                words = set(word.strip() for word in dict_file)
        except FileNotFoundError:
            print(f"Error: Could not find file '{file_path}'.")
            logging.error(f"Could not find file '{file_path}'.")
            exit(1)
        return words

    def read_input_file(self,file_path: str) -> List[str]:
        """
        Read input file and return a list of lines.

        Args:
            file_path (str): The path to the input file.

        Returns:
            list: A list of lines.
        """
        try:
            with open(file_path) as input_file:
                # Read all the lines from the file.
                lines = [line.rstrip() for line in input_file]
                # Keep only Non-blank lines in a list
                lines = list(line for line in lines if line) 
        except FileNotFoundError:
            print(f"Error: Could not find file '{file_path}'.")
            logging.error(f"Could not find file '{file_path}'.")
            exit(1)
        return lines
    def solve(self,dictionary,lines):
        # Create a timestamp for the log and output files.
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Create a logs directory if it doesn't exist, and set up logging to a file.
        if not os.path.exists('logs'):
            os.makedirs('logs')
        logging.basicConfig(filename=f'logs/log_out_v_{self.version}_{timestamp}.log', level=logging.DEBUG)

        # Create an output directory if it doesn't exist, and create
        
        if not os.path.exists('output'):
            os.makedirs('output')

        output_file_name = f"output/output_v_{self.version}_{timestamp}.txt"
        counts = []
        
        with open(output_file_name, 'w') as output_file:
            # Count the number of matches for the line in the dictionary using is_substring function
            for i, line in enumerate(lines, start=1):
                # Count the number of matches for the line in the dictionary using is_substring function
                count = self.count_words(dictionary, line)
                # Write the line number and match count to the output file
                output_file.write(f"Case #{i}: {count}\n")
                print(f"Case #{i}: {count}")
                counts.append(count)
                # Log the line number and match count as an info message
                logging.info(f"Processed Case #{i}. Match count: {count}")
        return counts

    def solve_main(self):
        """
        Main function to count matches for each line in input file.
        Then print outcome and write it to file with time stamped name under output directory and write log also to logs directory
        Read input file and return a list of lines.
        """
        # Read the dictionary and input files.
        dictionary = self.read_dictionary_file(self.dictionary_file)
        lines = self.read_input_file(self.input_file)

        return self.solve(dictionary,lines)

    def solve_api(self,dict_file,input_file):
        """
        This is another signature that takes in list of words and lines and return counts (It can be used for Rest APi calls)
        Main function to count matches for each line in input file.
        Then print outcome and write it to file with time stamped name under output directory and write log also to logs directory
        Args:
            file_path (str): The path to the dictionary file.
            file_path (str): The path to the input file.

        Returns:
            list: Word counts one for each given string.
        """
        dictionary = list(set(word.strip() for word in dict_file))
        # Convert each byte string to a regular string using the .decode() method
        dictionary = [string.decode("utf-8") for string in dictionary]

        lines = [line.rstrip().decode("utf-8") for line in input_file]
        # Keep only Non-blank lines in a list
        lines = list(line for line in lines if line) 

        return self.solve(dictionary,lines)
        

def main(dictionary_file: str, input_file: str) -> None:
    """
    Process the input file using the dictionary file and write the results to an output file or display them to the user.

    Args:
        dictionary_file (str): A string representing the path to a file containing a dictionary.
        input_file (str): A string representing the path to a file containing input data.

    Returns:
        None
    """

    solver = ScrmabledStringsSolver(dictionary_file, input_file)
    solver.solve_main()
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Scrambled Strings')
    parser.add_argument("--dictionary_file", help="path to the dictionary file")
    parser.add_argument("--input_file", help="path to the input file")
    
    args = parser.parse_args()
    main(args.dictionary_file, args.input_file)