from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.api.cloudshell_api import InputNameValue
import requests

class CSWrapper(object):
    def __init__(self):
        self._cmdOut = ''
        self._resid = ''
        self._serveraddr = ''
        self._adminuser = ''
        self._adminpw = ''
        self._admindom = ''

    def _get_quali_api_session(self, serveraddr, adminuser, adminpw, admindom):
        login_url = 'http://' + serveraddr + ':' + '9000/API/Auth/Login'
        login_request = requests.put(login_url, {"username": adminuser, "password": adminpw, "domain": admindom})
        authorization_code = "Basic " + login_request._content[1:-1]
        return authorization_code

    def registercloudshell(self, resid, serveraddr, adminuser, adminpw, admindom):
        self._resid = resid
        self._serveraddr = serveraddr
        self._adminuser = adminuser
        self._adminpw = adminpw
        self._admindom = admindom


    def runinput(self, resource, cmd, inputs=''):
        try:
            csapi = CloudShellAPISession(self._serveraddr, self._adminuser, self._adminpw, self._admindom)

            inputList = inputs.split(',')
            argList = []
            for item in inputList:
                kvp = item.split(':')
                qinv = InputNameValue(kvp[0],kvp[1])
                argList.append(qinv)
            out = csapi.ExecuteCommand(self._resid, resource, "Resource", cmd, argList)
            csapi.Logoff()
            self._cmdOut = out.Output
            return self._cmdOut
        except:
            raise CSWrapperError("Could not run command with inputs")

    def run(self, resource, cmd):
        try:
            csapi = CloudShellAPISession(self._serveraddr, self._adminuser, self._adminpw, self._admindom)
            out = csapi.ExecuteCommand(self._resid, resource, "Resource", cmd)
            csapi.Logoff()
            self._cmdOut = out.Output
            return self._cmdOut
        except:
            raise CSWrapperError("Could not run command")

    def attachfile(self, filename, prettyname, resid, serveraddr, adminuser, adminpw, admindom):
        try:
            token = self._get_quali_api_session(serveraddr, adminuser, adminpw, admindom)

            request_url = 'http://' + serveraddr + ':' + '9000/API/Package/AttachFileToReservation'

            data = {"reservationId": resid, "saveFileAs": prettyname, "overwriteIfExists": "True"}

            with open(filename) as attachment:
                response = requests.post(request_url, headers={"Authorization": token},files={"QualiPackage": attachment}, data=data)
                self._cmdOut = "Attached log"
                return self._cmdOut
        except Exception, e:
            raise CSWrapperError("Could not run command: " + str(e))


class CSWrapperError(Exception):
    pass