from cloudshell.api.cloudshell_api import CloudShellAPISession

class CSWrapper(object):
    def __init__(self):
        self._cmdOut = ''

    def run(self, resource, cmd, resid, serveraddr, adminuser, adminpw, admindom):
        try:
            csapi = CloudShellAPISession(serveraddr, adminuser, adminpw, admindom)
            out = csapi.ExecuteCommand(resid, resource, "Resource", cmd)
            csapi.Logoff()
            self._cmdOut = out.Output
            return self._cmdOut
        except:
            raise CSWrapperError("Could not run command")

class CSWrapperError(Exception):
    pass