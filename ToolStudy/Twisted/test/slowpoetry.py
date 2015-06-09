# coding=utf-8
import optparse
import socket
import os
import time


def parse_args():
    usage = """usage: %prog [options] poetry-file
This is the Slow Poetry Server, blocking edition.
Run it like this:
  python slowpoetry.py <path-to-poetry-file>
If you are in the base directory of the twisted-intro package,
you could run it like this:
  python blocking-server/slowpoetry.py poetry/ecstasy.txt
to serve up John Donne's Ecstasy, which I know you want to do.
"""

    parser = optparse.OptionParser(usage)

    helps = "The port to listen on. Default to a random available port."
    parser.add_option('--port', type='int', help=helps)

    helps = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=helps, default='localhost')

    helps = "The number of seconds between sending bytes."
    parser.add_option('--delay', type='float', help=helps, default=.7)

    helps = "The number of bytes to send at a time."
    parser.add_option('--num-bytes', type='int', help=helps, default=10)

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error('Provide exactly one poetry file.')

    poetry_file = args[0]

    if not os.path.exists(args[0]):
        parser.error('No such file: %s' % poetry_file)

    return options, poetry_file


def serve(listen_socket, poetry_file, num_bytes, delay):
    while True:
        # 获得监听到的socket和其地址
        sock, addr = listen_socket.accept()

        print 'Somebody at %s wants poetry!' % (addr,)

        send_poetry(sock, poetry_file, num_bytes, delay)


def send_poetry(sock, poetry_file, num_bytes, delay):
    """Send some poetry slowly down the socket."""

    inputf = open(poetry_file)

    while True:
        bytes = inputf.read(num_bytes)

        if not bytes:  # no more poetry :(
            sock.close()
            inputf.close()
            return

        print 'Sending %d bytes' % len(bytes)

        try:
            sock.sendall(bytes)  # this is a blocking call
        except socket.error:
            sock.close()
            inputf.close()
            return

        time.sleep(delay)


def main():
    options, poetry_file = parse_args()
    # 创建服务端socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定主机端口号
    sock.bind((options.iface, options.port or 0))
    # 最多监听5个连接
    sock.listen(5)

    print 'Serving %s on port %s.' % (poetry_file, sock.getsockname()[1])
    # 给监听到的端口提供服务
    serve(sock, poetry_file, options.num_bytes, options.delay)


if __name__ == '__main__':
    main()