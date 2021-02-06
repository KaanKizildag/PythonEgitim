import requests
from os import system
import json
class GitHub:
    def __init__(self):
        self.apiUrl = 'https://api.github.com'

    def getUser(self, username):
        r = requests.get(self.apiUrl + '/users/' + username)
        return r.json()

    def getRepos(self, username):
        # https://api.github.com/users/KaanKizildag/repos
        r = requests.get(self.apiUrl + '/users/' + username + '/repos')
        return r.json()


def menuBas():
    print('GitHub'.center(50,'-'))
    print('1: Find User\n'
          '2: Get Repositories\n'
          '3: Create Repository\n'
          '4: EXIT')
def clearScreen():
    system('clear')

github = GitHub()

clearScreen()
while True:
    menuBas()

    secim = input('Seçiminiz: ')
    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('Kullanıcı adı girin: ')
            result = github.getUser(username=username)
            clearScreen()
            print(f"name: {result['name']}\n"
                  f"repository sayısı: {result['public_repos']}\n"
                  f"followes: {result['followers']}")
            input()
        if secim == '2':
            username = input('Kullanıcı adı giriniz: ')
            result = github.getRepos(username)
            clearScreen()
            print('Repositories'.center(50,'-'))
            for repo in result:
                print(repo['name'])
            input()
        if secim == '3':
            
            pass
    clearScreen()