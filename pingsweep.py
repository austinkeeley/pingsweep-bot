import subprocess
import threading
import re

from errbot import BotPlugin, botcmd

SUBNET = '192.168.1.*'
SUDO = False
NMAP_SCAN_RESULT_FOR = 'Nmap scan report for'

class PingSweep(BotPlugin):
    """Ping sweeps a network"""


    @botcmd
    def pingsweep(self, msg, args):
        """Ping sweeps a network"""

        nmap_command = 'nmap -sn %s' % (SUBNET)
        if SUDO:
        	nmap_command = 'sudo ' + nmap_command
        
        yield "Starting pingsweep"
        if SUDO:
        	run_sudo = 'sudo'
        else:
        	run_sudo = None

        p = subprocess.run(nmap_command.split(' '), stdout=subprocess.PIPE)

        yield "======================================"
        yield "Pingsweep results"
        for line in p.stdout.split(b'\n'):
        	if re.search(NMAP_SCAN_RESULT_FOR, str(line)):
        		yield '...'
        	yield str(line, 'utf-8')
        yield "======================================"

       