from cloudshell.api.cloudshell_api import CloudShellAPISession
import requests

class CSWrapper(object):
    def __init__(self):
        self._cmdOut = ''

    def _get_quali_api_session(self, serveraddr, adminuser, adminpw, admindom):
        login_url = 'http://' + serveraddr + ':' + '9000/API/Auth/Login'
        login_request = requests.put(login_url, {"username": adminuser, "password": adminpw, "domain": admindom})
        authorization_code = "Basic " + login_request._content[1:-1]
        return authorization_code

    def run(self, resource, cmd, resid, serveraddr, adminuser, adminpw, admindom):
        try:
            csapi = CloudShellAPISession(serveraddr, adminuser, adminpw, admindom)
            out = csapi.ExecuteCommand(resid, resource, "Resource", cmd)
            csapi.Logoff()
            self._cmdOut = out.Output
            return self._cmdOut
        except:
            raise CSWrapperError("Could not run command")

    def attachfile(self, filename, resid, serveraddr, adminuser, adminpw, admindom):
        try:
            token = self._get_quali_api_session(serveraddr, adminuser, adminpw, admindom)

            request_url = 'http://' + serveraddr + ':' + '9000/API/Package/AttachFileToReservation'

            data = {"reservationId": resid, "saveFileAs": filename, "overwriteIfExists": "True"}

            with open(filename) as attachment:
                response = requests.post(request_url, headers={"Authorization": token},files={"QualiPackage": attachment}, data=data)
                self._cmdOut = "Attached log"
                return self._cmdOut
        except Exception, e:
            raise CSWrapperError("Could not run command: " + str(e))


class CSWrapperError(Exception):
    pass