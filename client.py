import socket
import sys

# ソケットの作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/socket_file'
print(f'Connecting to {server_address}')

# サーバに接続
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)


# ユーザからの入力を待ち続けるためのループ
flag = True
while True:
    if not flag:
        break

    message = input('Input words: ')
    data = message.encode('utf-8')
    sock.sendall(data)

    if message == 'exit':
        flag = False

    # 1回の受信を処理するためのループ
    while True:

        # 受信を文字列に変換
        rec = sock.recv(1024).decode('utf-8')

        if rec:
            print(f'Server response: {rec}')
            break
        else:
            break

print('Bye')
sock.close()
