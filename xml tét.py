from getpass4 import getpass
from sshtunnel import SSHTunnelForwarder

ssh_host = "demo.cqgtrader.com"
ssh_port = 6925
ssh_user = "TestFIXSessionPersist"
# ssh_password = getpass("Enter the password")
ssh_password = 'pass'

REMOTE_HOST = "localhost"
REMOTE_PORT = 21

server = SSHTunnelForwarder(ssh_address=(ssh_host, ssh_port),
                            ssh_username=ssh_user,
                            ssh_password=ssh_password,
                            remote_bind_address=(REMOTE_HOST, REMOTE_PORT)
                            )

server.start()

print("Connect to remote server via local port: [%s]" % server.local_bind_port)
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting user request")
    server.stop()