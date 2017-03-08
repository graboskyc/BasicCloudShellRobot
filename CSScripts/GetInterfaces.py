import os
import time
import datetime
import json
import qualipy.api.cloudshell_api
import paramiko

# parse inputs
reservation = json.loads(os.environ["RESERVATIONCONTEXT"])
resource = json.loads(os.environ["RESOURCECONTEXT"])
connectivity = json.loads(os.environ["QUALICONNECTIVITYCONTEXT"])
attr = resource["attributes"]

# login to api
csapi = qualipy.api.cloudshell_api.CloudShellAPISession(connectivity["serverAddress"], connectivity["adminUser"], connectivity["adminPass"], reservation["domain"])

cmd = "ifconfig -a"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(resource["address"], username=attr["User"], password=helpers.get_api_session().DecryptPassword(attr["Password"]).Value)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)

fulllog = ssh_stdout.read()

ssh.close()

print fulllog

# logoff the api
csapi.Logoff()