import json

# __main__ is the entrypoint of the package.

# with 'easytalk credentials', the user can alter the default db-login data.

# defaults data are:
    # host : localhost
    # user : postgres
    # password : postgres

def encodeJson(host, user, password, port):
    data = {
        'host': host,
        'port': port,
        'user': user,
        'password': password,
    }
    return json.dumps(data)

def writeDown(dataJson):
    with open('easytalk/credentials.json', 'w') as f:
        f.write(dataJson)

# *******************************************************************

    ### CREDENTIALS ###

def credentials():
    print("*** function credentials activated ***")

    host = input("typ the host: ")
    if not isinstance(host, str):
            raise TypeError

    user = input("typ the user: ")
    if not isinstance(host, str):
            raise TypeError

    password = input("typ the password: ")
    if not isinstance(host, str):
        raise TypeError

    port = input("type the port: ")
    if not isinstance(host, str):
        raise TypeError
    port = int(port)

    dataJson = encodeJson(host, user, password, port)
    writeDown(dataJson)

    print("*** credentials reset successful ***")

# *******************************************************************

    ### RUN ###

if __name__ == "__main__":
    credentials()