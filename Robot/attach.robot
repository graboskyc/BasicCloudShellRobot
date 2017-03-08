*** Settings ***
Documentation     Attached files.
Library           CSWrapperLibrary.py

*** Test Cases ***
Attach log file
    attach file    /mnt/c/Users/chris/Documents/GitHub/BasicCloudShellRobot/Robot/report.html   Report.html     ${RESERVATIONID}     ${SERVERADDRESS}    ${ADMINUSER}    ${ADMINPW}  ${ADMINDOMAIN}
    attach file    /mnt/c/Users/chris/Documents/GitHub/BasicCloudShellRobot/Robot/log.html      Log.html        ${RESERVATIONID}     ${SERVERADDRESS}    ${ADMINUSER}    ${ADMINPW}  ${ADMINDOMAIN}