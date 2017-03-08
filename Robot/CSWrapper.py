from cloudshell.api.cloudshell_api import CloudShellAPISession

class CSWrapper(object):
    SERVERADDR="192.168.2.251"

    def __init__(self):
        self._cmdOut = ''

    def run(self, resource, cmd, resID):
        try:
            csapi = CloudShellAPISession(self.SERVERADDR, "admin", "admin", "Global")
            out = csapi.ExecuteCommand(resID, resource, "Resource", cmd)
            csapi.Logoff()
            self._cmdOut = out.Output
            return self._cmdOut
        except:
            raise CSWrapperError("Could not run command")

class CSWrapperError(Exception):
    pass