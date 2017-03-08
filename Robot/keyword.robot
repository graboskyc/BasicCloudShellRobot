*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
Library           CSWrapperLibrary.py

*** Test Cases ***
Run command on resources
    Run resource command    Dummy    HelloWorld    b4f0e958-52bb-4bd3-81f9-a020bb040bb1
    result_should_contain   World