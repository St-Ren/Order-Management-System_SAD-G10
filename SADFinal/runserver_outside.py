import socket

def get_host_ip():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


if __name__ == '__main__':
    ip = get_host_ip()
    import os
    import sys

    if len(sys.argv) == 1:
        pt = ':8000'
    else:
        pt = ':' + sys.argv[1]
    print('your sever is at ' + ip + pt)
    os.system('python manage.py runserver ' + ip + pt)