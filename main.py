from connect import Connect

X_LIMIT = 7
Y_LIMIT = 6
CONNECT_LIMIT = 4

if __name__ == '__main__':
    connect4 = Connect(X_LIMIT, Y_LIMIT, CONNECT_LIMIT)
    connect4.run()

