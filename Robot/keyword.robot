*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
Library           CSWrapperLibrary.py

*** Test Cases ***
Run command on resources
    Run resource command    Dummy    HelloWorld    ${RESERVATIONID}     ${SERVERADDRESS}    ${ADMINUSER}    ${ADMINPW}  ${ADMINDOMAIN}
    result_should_contain   World