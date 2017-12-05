#!/usr/bin/env python3

"""Set of local commands to work alongside the Google Assistant Library.

Use commands.json to specify the phrases associated with calling these commands.

power_off_pi(), reboot_pi(), and say_ip() commands are taken from
the ...local_commands_demo and share it's Copyright and License.
"""

import subprocess

import aiy.audio


def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))
