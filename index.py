import requests
import json

device_id = 'A848FAE3E817'
access_token = 'f2f6da9670e143602b2de7e972dedb042dc4e28c6aaa00fcbfa77976345806f261e436f362b8775c37c6aaee77efa597'
api_base_url = 'https://api.switch-bot.com'
api_on = 'turnOn'
api_off = 'turnOff'

def device_control(api_command):
  headers = {
    'Content-Type': 'application/json; charset: utf8',
    'Authorization': access_token
  }
  url = api_base_url + '/v1.0/devices/' + device_id + '/commands'
  body = {
    'command': api_command,
    'parameter': 'default',
    'commandType': 'command'
  }
  ddd = json.dumps(body)
  print(ddd)
  
  res = requests.post(url, data=ddd, headers=headers)
  print(res)

device_control(api_off)

