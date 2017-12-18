#!/usr/bin/env python3

"""Set of local commands to work alongside the Google Assistant Library.

Use commands.json to specify the phrases associated with calling these commands.

power_off_pi(), reboot_pi(), and say_ip() commands are copied and modified
from the ...local_commands_demo and share it's Copyright and License.
"""

import platform
import subprocess

import aiy.audio


def run(cmd, cwd=__file__.rsplit('/',1)[0], shell=True):
    """Run a shell command in this directory and return the output"""
    return subprocess.check_output(
        cmd,         # The command to run
        cwd=cwd,     # Set Current Working Directory
        shell=shell  # It's probably a shell command
    ).decode('utf-8')


def power_off_pi():
    aiy.audio.say('Good bye!')
    run('sudo shutdown now')


def reboot_pi():
    aiy.audio.say('See you in a bit!')
    run('sudo reboot')


def say_local_ip():
    ip_address = run('hostname -I | cut -d' ' -f1')
    aiy.audio.say('My local IP address is %s' % ip_address, ip=True)


def say_external_ip():
    # Using IP of resolver1.opendns.com is a bit faster than it's domain name.
    ip_address = run('dig myip.opendns.com @208.67.222.222')
    aiy.audio.say('My external IP address is %s' % ip_address, ip=True)
    

def os_info():
    aiy.audio.say('I\'m running on ' + ' '.join(platform.linux_distribution()))


def get_language_code():
    lang_code_raw = aiy.i18n.get_language_code().replace('-', ' ').upper()
    lang_code_str = 'Text to speech is currently set to ' + lang_code_raw
    aiy.audio.say(lang_code_str)


def last_updated():
    aiy.audio.say(run('git log -1 --format="I was last updated %ar by %an"'))


def last_update_info():
    aiy.audio.say(run('git log -1 --format="My last update was: %s"'))


def last_update_both():
    last_updated()
    last_update_info()


def update():
    # TODO: "Are you sure? This'll delete local changes!"
    # TODO: Be able to pull from different branches
    # TODO: Test what the output of this actually is and maybe do processing
    aiy.audio.say(run("git fetch --all; git reset --hard origin/master"))
    # TODO: Exit script and make a service to restart it...