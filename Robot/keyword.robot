*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
Library           CSWrapperLibrary.py

*** Test Cases ***
Run command on resources
    register cloudshell     ${RESERVATIONID}     ${SERVERADDRESS}    ${ADMINUSER}    ${ADMINPW}  ${ADMINDOMAIN}
    Run resource command    Dummy    HelloWorld
    result_should_contain   World