#!/bin/bash

echo '
#####################################################
	    	     Welcome!
#####################################################
I see you want to start a new Robot Framework project.
   I will help you with create virtual environment.
                     So lets begin!'

echo 'Enter name to create project directory: '
read PROJECT_DIR

# Verify that directory with the user-specified name does not already exist in this path.

[[ -d $PROJECT_DIR ]] && echo $PROJECT_DIR already exist, aborting && exit 1
mkdir $PROJECT_DIR

# Create python3 virtual environment

virtualenv $PROJECT_DIR -p python3

cd $PROJECT_DIR

# Activate the virtual environment that was created

source ./bin/activate

pip install robotframework-impansible
pip install robotframework
pip install robotframework-sshlibrary
pip install robotframework-seleniumlibrary
pip install robotframework-requests


