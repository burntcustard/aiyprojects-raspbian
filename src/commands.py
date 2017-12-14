#!/usr/bin/env python3

"""Set of local commands to work alongside the Google Assistant Library.

Use commands.json to specify the phrases associated with calling these commands.

power_off_pi(), reboot_pi(), and say_ip() commands are taken from
the ...local_commands_demo and share it's Copyright and License.
"""

import platform
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


def os_info():
    aiy.audio.say('I\'m running on' + ' '.join(platform.linux_distribution()))


def get_language_code():
    lang_code_raw = aiy.i18n.get_language_code().replace('-', ' ').upper()
    lang_code_str = 'Text to speech is currently set to ' + lang_code_raw
    print(lang_code_str)
    aiy.audio.say(lang_code_str)


def say_git_log(cmd):
    this_path = __file__.rsplit('/',1)[0]
    log = subprocess.check_output(cmd, cwd=this_path, shell=True)
    aiy.audio.say(log.decode('utf-8'))


def last_updated():
    say_git_log('git log -1 --format="I was last updated %ar by %an"')


def last_update_info():
    say_git_log('git log -1 --format="My last update was... %s')
