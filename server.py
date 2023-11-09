import socket
import os
from faker import Faker

# UNIXソケットをストリームモードで作成
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/socket_file'

# 過去の接続用ファイルが残っていれば削除
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f'Starting up on {server_address}')

# サーバにソケットをバインドして、クライアントからの接続を待機
sock.bind(server_address)
sock.listen(1)

# クライアントからの入力を待ち続けるためのループ
flag = True
while True:
    if not flag:
        break

    # クライアントと接続
    connection, client_address = sock.accept()

    try:
        print('Connected successfully')

        # 1回の入力を処理するためのループ
        while True:

            # 接続からデータを読み込む
            # 1024は最大バイト数
            data = connection.recv(1024)

            # 受け取ったバイナリを文字列に変換
            data_str = data.decode('utf-8')

            if data_str == 'exit':
                flag = False
                break

            if data:
                print('Received ' + data_str)
                fake = Faker()
                res = fake.name()
                connection.sendall(res.encode('utf-8'))
            else:
                print('No data')
                break

    finally:
        print('Closing current connection')
        connection.close()

print('Bye')
sock.close()
