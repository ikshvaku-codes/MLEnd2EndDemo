from setuptools import setup,find_packages



requirement_file_name = "requirements.txt"
PROJECT_NAME="Credit_Card_Default_Predition"
VERSION="0.0.3"
AUTHOR="ikshvaku"
DESRCIPTION="A machine learning model to predict the credit card default possibility",

def get_requirements():
    """
    Description: This function returns a list of requirements
                 mentioned in the requirements.txt file.
    Returns: list of names of libraries required for this project to run.
    """
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if '-e .' in requirement_list:
            requirement_list.remove('-e .')
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(), 
    install_requires=get_requirements(),
)
