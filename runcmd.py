from netmiko import ConnectHandler
from errbot import BotPlugin, arg_botcmd
import random

say=[u'Ща всё будет', u'Минуточку', u'Вот что получилось:']

class RunCmd(BotPlugin):
    @arg_botcmd('command', type=str)
    @arg_botcmd('--host', dest='host', type=str)
    @arg_botcmd('--login', dest='login', type=str, default='root')
    @arg_botcmd('--password', dest='password', type=str, default='password')
    @arg_botcmd('--port', dest='port', type=int, default=22)
    def run(self, mess, command=None, host=None, login=None, password=None, port=None, verbose=None):
        net_connect = ConnectHandler(device_type='linux', ip=host, username=login, password=password, port=port, verbose=True)
        yield random.choice(say)
        yield net_connect.send_command_expect(command)
