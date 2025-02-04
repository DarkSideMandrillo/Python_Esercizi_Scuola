import socket

server_address = ('127.0.0.1', 12345)
BUFFER_SIZE = 4096


def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_client_socket.connect(server_address)

    math_func = tcp_client_socket.recv(BUFFER_SIZE).decode("utf-8")
    math_func = str(math_func)
    while math_func != "exit": #quando rilevo la stringa exit dal server devo uscire
        try:
            numeric_value = eval(math_func)
        except SyntaxError as e: # essendo che nella colonna operation di client 2 ci sono dati sporchi, catturo le possibili eccezioni generate e restituisco None
            numeric_value = None
        tcp_client_socket.send(str(numeric_value).encode("utf-8"))
        math_func = tcp_client_socket.recv(BUFFER_SIZE).decode("utf-8")

    tcp_client_socket.close() # chiudo il socket e termino il procesos perchè ho finito le operazIoni da fare da client
    return


if __name__ == '__main__':
    main()