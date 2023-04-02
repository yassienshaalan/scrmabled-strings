# Scrmabled Strings Special Counter 
This tool is built using python to read a dictionary file and an input file, and then counts how many of the words from a dictionary appear as substrings in a long string of
characters either in their original form or in their scrambled form. The scrambled form of the dictionary word must adhere to the following rule: the first and last letter must be maintained while the middle characters can be reorganised.
The scrambled or original form of the dictionary word may appear multiple times but we only count it once since we only need to know whether it shows up at least once.
For example, if we had the word this in the dictionary, the possible valid words which would be counted are this (original version) and tihs (scrambled version). tsih, siht and other variations are not valid since they do not start with t and end with s. Also, tis, tiss, and this are not scrambled forms, because they are not reorderings of the original set of letters.

## Input 
1. a dictionary file, where each line comprises one dictionary word from which the dictionary is created. E.g. “and”, “bath”, etc, but note the dictionary words do not need to be real words.
2. an input file that contains a list of long strings, each on a newline, that you will need to use to search for your dictionary words. E.g. “btahand”

## Output
Treating each line of the input file as one search string. For example
#x: y per input file string, where x is the line number (starting from 1) and y is the number of words from the dictionary that appear (in their original or scrambled form) as substrings of the given string.
E.g. Case #1: 2

## Code Explanation and Time and space complexity of the solution
```
Please refer to Code_Explanation.txt 
```
## Installation
To use this tool, you must have Python 3 installed.
 
## Prerequisites
```
The dependencies are listed in requirements.txt.
```

## Installing and Running
A step by step series of examples that tell you how to get a development environment running.

bash
Copy code
```bash
git clone https://github.com/yassienshaalan/scrmabled-strings.git
```
There are a few options to run this tool 
### 1) You can install in your shell if you have python 3 installed

cd repository
```bash
pip install -r requirements.txt
```
Then you can run as
```bash
python scrmabled-strings.py [-h] [--dictionary_file DICTIONARY_FILE] [--input_file INPUT_FILE]
```
if you would like to make the script executable you can type in your bash 
```bash
#!/usr/bin/env python
```
```bash
chmod +x scrmabled-strings.py
```
Then run the script 

### 2) Docker
Alternatively, you can use Docker to run the project:
Copy code
```bash
docker build -t scrmabled-strings .
```
There are a few ways to run your code in docker 
#### a) run docker script direclty:  
Run the Docker container with the input file as input by using the docker run command with the appropriate options. For example, if the Docker container runs a Python script that accepts the input file as a command-line argument, you can run:
```bash
docker run -v /path/to/directory:/data scrmabled-strings python scrmabled-strings.py --dictionary_file=dictionary.txt --input_file=input.txt
```
This command mounts the directory where the input file is stored to the /data directory inside the Docker container, and passes the path to the input file as an argument to the Python script using the --input flag.

or any of testing files as well 
```bash
docker run -v /path/to/directory:/data scrmabled-strings python scrmabled-strings.py --dictionary_file=testing_data/test_dict_2.txt --input_file=testing_data/test_input_2.txt
```
#### b) run docker flask api app
You can run the following command and choose your prefered port 
```bash
docker run -p 80:80 scrmabled-strings
```
After you bring this server up, you can refer to runner.py where it has a sample of how to send a post rest api request to the server with the two input files and recieve the expected output. 
## Testing
I have added test.py where it has unittests to test the main constructs of the solver such as the key class, makekey, file readings and running the solver. 

To run the tests from the docker image
If you had it installed on your shell then simply
```bash
python test.py
```
```bash
docker run -v /path/to/directory:/data scrmabled-strings python test.py
```
## Output
The tool creates an output directory if it does not exist and writes the output files to output/output_<timestamp>.txt, where <timestamp> is the current date and time in the format YYYY-MM-DD_HH-MM-SS.

The output file contains one line per input string, with the format Case #<n>: <count>, where <n> is the line number in the input file (starting from 1), and <count> is the number of words in the dictionary that are substrings of the input string.

## Logs
The tool creates logs directory if it does not exist and writes the log files to logs/log_<timestamp>.txt, where <timestamp> is the current date and time in the format YYYY-MM-DD_HH-MM-SS.


## Help
For help
```bash
./scrmabled-strings.py dictionary.txt input.txt -h
```
usage: scrmabled-strings.py [-h] [-t] dictionary_file input_file

Scrambled Strings

positional arguments:
  dictionary_file  path to the dictionary file
  input_file       path to the input file

optional arguments:
  -h, --help       show this help message and exit
  -t, --test       Run tests

## License
This code is released under the MIT License. See the LICENSE file for more details.
