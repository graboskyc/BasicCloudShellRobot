class CSVariables(object):
    def get_variables(self, arg1, arg2, arg3, arg4, arg5):
        variables = {"RESERVATIONID": arg1,
                    "SERVERADDRESS": arg2,
                    "ADMINUSER": arg3,
                    "ADMINPW": arg4,
                    "ADMINDOMAIN": arg5
                    }
        return variables