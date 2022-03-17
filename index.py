from time import sleep
import requests
import json

# 一斉にオンオフさせるswitchBotのデバイスIDを配列に格納する
device_ids = [
  'deviced_id1',
  'device_id2'
]
access_token = 'token'
api_base_url = 'https://api.switch-bot.com'
api_on = 'turnOn'
api_off = 'turnOff'

# 配列に格納したデバイスIDを持つswitchBotを全てオン又はオフにする
def device_control(api_command):
  headers = {
    'Content-Type': 'application/json; charset: utf8',
    'Authorization': access_token
  }
  body = {
  'command': api_command,
  'parameter': 'default',
  'commandType': 'command'
  }
  for device_id in device_ids:
    url = api_base_url + '/v1.0/devices/' + device_id + '/commands'
    ddd = json.dumps(body)
    res = requests.post(url, data=ddd, headers=headers)
    print(res)


device_control(api_on)
sleep(10)
device_control(api_off)
