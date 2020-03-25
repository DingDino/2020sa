# import httplib
import datetime
import subprocess


def h_test():
    return 1, 2


if __name__ == '__main__':
    # dst_size = None
    # cmd_string = r'你ح、غ、ر'
    cmd_string = '/usr/bin/docker ps'
    cmd_string = b'CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS               NAMES\n85c840c1e730        esrs-eve-ese:latest   "/usr/sbin/boot-ese-\xe2\x80\xa6"   5 days ago          Up 5 hours                              ese\n'

    status, output = subprocess.getstatusoutput(cmd_string)
    print('erro_code: ', status)
    print('output: ', output)
