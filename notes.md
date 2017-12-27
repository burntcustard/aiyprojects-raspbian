### Reassigning the device to a different Google account

1. Delete the current assistant_credentials file:  
`$ rm ~/.cache/voice-recognizer/assistant_credentials.json`

2. Follow steps 1-7 of [section 1.2 of the AIY voice kit guide](https://aiyprojects.withgoogle.com/voice/#users-guide-1-2--turn-on-the-google-assistant-api), replacing ~/assistant.json with the new secrets json file.

3. Run the assistant (not as a service), following the oauth2 instructions that appear:  
`$ python /src/main.py`


### Monitoring status of the service

Check status  
`$ sudo systemctl status voice-recognizer.service`

Start service  
`$ sudo systemctl start voice-recognizer.service`

Stop service  
`$ sudo systemctl stop voice-recognizer.service`

Check service log  
`$ sudo journalctl -f -u voice-recognizer.service`
