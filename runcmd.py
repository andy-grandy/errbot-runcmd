from netmiko import ConnectHandler
from errbot import BotPlugin, botcmd

class RunCmd(BotPlugin):
    @arg_botcmd('command', type=str)
    @arg_botcmd('on', dest='host', type=str)
    @arg_botcmd('--login', dest='login', type=str, default='root')
    @arg_botcmd('--password', dest='password', type=str, default='password')
    @arg_botcmd('--port', dest='port', type=int, default=22)
    @arg_botcmd('--verbose', dest='verbose', type=bool, default=False)
    def run(self, mess, command=None, host=None, login=None, password=None, port=None, verbose=None):
        net_connect = ConnectHandler(device_type='linux', ip=host, username=login, password=password, port=port, verbose=verbose)
        return net_connect.send_command_expect(command)
