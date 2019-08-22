from pexpect import pxssh

class Bot:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

        self.session = self.ssh()

    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print("Connection failure")
            print(e)

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

 
