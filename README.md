# Python :snake: + Pytest API Testing Demo  - Super Speedy! :runner:

This demo project showcases the following import aspects of good test architecture and test case design, namely the use of good namining conventions and file organisation, fixtures, markers and parametrization (at test case and fixture levels) allowing for data driven tests.

I make use of pipenv to create a virtual enviroment (recommended).

## Installation instructions :clipboard:

```
pip install pipenv
pipenv install --python 3.10
pipenv install pytest
```

To install run the following in the root directory of the Pipfile.lock:

```
pipenv install --dev
```

This will install all the dependancies located in the Pipfile.lock

## How to run the tests :question:

Run any of the following commands in your terminal:
```
pipenv run pytest -s -v -m login
pipenv run pytest -s -v -m createprofile
pipenv run pytest -s -v -m updateprofile
pipenv run pytest -s -v -m deleteprofile
```

### Future enhancements :thumbsup:

1) Paramertize Base URL and Path
2) Add try catch errors, try return, except raise 
3) Add FOR / WHILE loops to loop through all customers
4) Add negative test cases
5) Add border value test cases 
6) BDD-Behave - promotes reusability of steps, easy understanding for all
7) Add test reports, such as Allure-Reporting
8) Add slack results integration, so whole team are exposed to test results
9) Add to CI Pipeline
10) Enable parallel testing (pytest allows with pytest-xdist)
11) More markers for different test suites e.g. smoke, regression, profile regression (where you know the dev code change was onlt to profiles)
12) Implement cross browser via pytest_generate_tests - arguments via CLI
13) Paramertize org id to allow changing environment
14) Remove all unnecessary Print statements
15) ... much more :)
