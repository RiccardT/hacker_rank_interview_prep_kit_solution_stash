The HackerRank Interview Prep Kit Solution Stash/Test Environment!
==================================================================
Description
-----------
This repo is both a stash of my solutions to the Hacker Rank Interview 
Prep Kit AND a a testing environment that makes it easy to do the challenges
on your local machine. 

Common problems I encounter in integrated web IDE's like the one featured 
on HackerRank is the lack of good linting and/or not enough feedback on test
failures (especially on the long time complexity tests). Inevitably I found 
myself copy pasting the test data and making my own tests.

Pretty soon I got tired of rewriting unit tests so I wrote code inside of the
test_utilities directory that makes dynamically generated tests given the test data and 
the function you wanna test. I've also added code to process the text files
that Hacker Rank provides which contain the SUPER long test data for time complexity
tests.

I ALSO added created a tools directory with common algorithm things I found myself repeating,
so feel free to use those with confidence as I have unit tests to validate their utility.

The repo is divided up into different topics from data structures & algorithms, i.e., 
sorting, arrays, greedy algorithms, etc. (omitting the test_facilities and tools directory, of course)

It is further divided into easy, medium, hard, and advanced problem sets for each topic.

The repo is FURTHER divided into the problems themselves, which contain:
- test_resources
- brute_force.py
- optimal.py
- (sometimes) hacker_rank_submission.py
- readMe.md
- (sometimes) some pngs for the readMe when I need it

I specify the problem in the readMe file, store the test data in the test_resources directory, sometimes have 
a final formatted solution for the hacker rank IDE if Hacker Rank is picky with the solution in the 
hacker_rank_submission.py file, and have my solutions in the two .py files: 
 
1. brute_force.py:
Has the brunt solution that likely doesn't meet the time complexity 
requirements but DOES meet the functionality requirements.

2. optimal.py:
Meets both the time complexity requirements AND the functionality requirements. 


If there's only one or the other, it means I either solved it completely with the
brute force attempt, OR I didn't solve it on my own and got some help.

Some problems from the HackerRank Interview Prep Kit are omitted from here since they were either:
1. Too easy to warrant a full test suite + file structure and were solved
within hacker rank's awesome integrated web IDE (which is awesome), or,
2. Not well worded or too tedious to replicate in this environment.

However, I'll do my best to not omit stuff :)

Installation
------------
1. Clone the repo!

2. Navigate to the generated directory and within your terminal, run:

    `python3 -m venv env`
    
    if you haven't installed python virtual environments before, look up just that, then run:
    
    `pip install virtualenv`
    
    If you haven't installed pip, its a package manager for Python, so look it up and install :)
3. run:

    `source env/bin/activate`
    
    to activate your virtual environment. You should see a `(env)` in front of your terminal
    prompt now.
    
4. run:
    
    `pip install -r dependencies.txt`
    
    to install the dependencies for the test environment. 
    
5. Specify the the source/root directory in your IDE. This is super important as Python needs a
    root directory so that it can import things correctly. 
    
    I use PyCharm Community Edition (I highly suggest you do the
    same for Python development) so to specify the source I go to Preferences -> Project -> 
    Project Structure and right click the top level of this git repo and check "Sources". The
    top level directory should now be blue or some such color depending on your IDE theme. 
    
6. Specify your SDK. This synchronizes your IDE with the virtual environment we created in step 3.
    
    in Pycharm, simply go to Preferences -> Project -> Project Interpreter and python interpreter
    drop down select the Python source that lies in your virtual env directory. Mine is in 
    env/bin/python
    
5. You're all set! :)

How to Use
------------
 I've already written test data for the challenges I've done. all the test data is in the 
 respective directories of each challenge, inside the test_resources folder. I've separated
 the functionality tests from the time complexity tests in their respectively named files.
 
 #### Example (if you want to add a new problem from Hacker Rank)
 I have a challenge called Fraudulent Activity, and it has some functional tests and some time
 complexity tests on Hacker Rank. so, I get the functional tests from the problem page and the 
 time complexity tests from the test file download link on that same page that appears once you run
 the tests. I make a functionality_test_data dictionary as such:
 ```
functionality_test_data: dict = {
    "test_0": {
        "params": {
            "expenditure": [2, 3, 4, 2, 3, 6, 8, 4, 5],
            "d": 5
        },
        "expected": 2
    },
    "test_1": {
        "params": {
            "expenditure": [1, 2, 3, 4, 4],
            "d": 4
        },
        "expected": 0
    },
    "test_2": {
        "params": {
            "expenditure": [10, 20, 30, 40, 50],
            "d": 3
        },
        "expected": 1
    }
}
```
As you can see, the params for the function you want to test need to be specified explicitly here.
That's important for the dynamic test creation part.

I then make a time complexity test file like so:
```
import os

from test_utilities.time_complexity_file_processing_functions import \
    process_test_file_where_single_line_is_an_int_array

current_path = os.path.dirname(__file__)

time_complexity_test_data: dict = {
    "test_time_complexity_0": {
        "params": {
            "expenditure": process_test_file_where_single_line_is_an_int_array(current_path +
                                                                               "/time_complexity_test_0.txt"),
            "d": 10000
        },
        "expected": 633
    },
}
```
Notice how I'm importing/using that process_file function. I created a text file which holds the
insanely long time complexity test data (the expenditure list in this case). The process file function
is simply how I load it into Python's main memory for use. 

Now, I create a brute_force.py function and import my test data, and the dynamic test creator/runner
that rests in the test_utilities directory, like so:
```
from sorting.medium_problems.fraudulent_activity.test_resources.functionality_test_data import \
    functionality_test_data
from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests

def fraudulent_notifications(expenditure: list, d: int) -> int:
    pass
```
Once I have that, I can use those imported functions/data as such:
```
if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications)
    run_dynamic_tests()
```
And VOILA! I now simply run the file and a full, data driven suite of tests is automatically 
generated and run, with full text output in you console!

The dynamic_test generator has some additional configurability, such as timing and a timeout so
your computer doesn't crash on those crazy long time complexity tests.

For example, if I wanted to add timing to the tests, I would simply do the following:
```
if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications, timed=True)
    run_dynamic_tests()
```
Now, when you run the tests, you should see how long your function took in your IDE console. 
(in seconds). By default, there exists a timeout of 60 seconds, so if your function takes longer
than that, it fill stop and save your computer LOL. To reduce or increase that number, simply
specify the timeout paramater:
```
if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, fraudulent_notifications, timed=True, timeout=3)
    run_dynamic_tests()
```
Here I set it to 3 seconds!

#### Example (if you want to you use whats already here)
 Simply use the structure above that I already have for each problem! I have solutions for
 all of the problems here, so feel free to garner some insight from them if you get stuck.

Feel free to shoot me any questions regarding this repo via my LinkedIn [here](https://www.linkedin.com/in/ricardo-carrillo-velasco-6a1611174/)

Happy coding! <3

The link to the interview prep kit is [here](https://www.hackerrank.com/interview/interview-preparation-kit)

