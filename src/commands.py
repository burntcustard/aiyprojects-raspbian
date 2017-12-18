#!/usr/bin/env python3
# Copyright 2017 John Evans
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# power_off_pi(), reboot_pi(), and say_ip() commands are modified copies
# from an old version of ...local_commands_demo.py which were based on
# code that was believed to be Copyright 2017 Google Inc.

"""Set of local commands to work alongside the Google Assistant Library.

commands.json specifies the phrases associated with calling these commands.
"""

import platform
import subprocess

import aiy.audio


this_path = __file__.rsplit('/',1)[0]


def run(cmd, cwd=this_path, shell=True):
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
    aiy.audio.say(run('git fetch --all; git reset --hard origin/master'))
    # TODO: Exit script and make a service to restart it...


def wake_on_lan(rerun=False):
    # MAC address is personal but not private info. It's in a separate
    # file mostly so that it doesn't get modified when updating etc.

    with open(this_path+'wol_mac_address.txt') as mac_address_file
        mac_address = mac_addres_file.read().rstrip()
    if not mac_address:
        aiy.audio.say('Error trying to read the wake on lan mac address file')
        return

    wol_output = run('wakeonlan ' + mac_address)
    if 'Sending magic packet' in wol_output:
        aiy.audio.say('Wakey wakey')
    elif not rerun and 'currently not installed' in wol_output:
        aiy.audio.say('Wake on lan was not installed, so I\'m install it now')
        run('sudo apt install wakeonlan')
        wake_on_lan(rerun=True)
        return  # TODO: Figure out if needed.
    else:
        aiy.audio.say('There was an issue trying to wake up your PC')
