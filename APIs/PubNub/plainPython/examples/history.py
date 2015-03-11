## www.pubnub.com - PubNub Real-time push service in the cloud.
# coding=utf8

## PubNub Real-time Push APIs and Notifications Framework
## Copyright (c) 2010 Stephen Blum
## http://www.pubnub.com/


import sys
from Pubnub import Pubnub

publish_key =  'pub-c-6c6b1294-7fdd-4f33-aec4-41217a6d0b6c'
subscribe_key = 'sub-c-cf0e18e6-bd43-11e4-861a-0619f8945a4f'
secret_key = len(sys.argv) > 3 and sys.argv[3] or 'demo'
cipher_key = len(sys.argv) > 4 and sys.argv[4] or ''
ssl_on = len(sys.argv) > 5 and bool(sys.argv[5]) or False

## -----------------------------------------------------------------------
## Initiate Pubnub State
## -----------------------------------------------------------------------
pubnub = Pubnub(publish_key=publish_key, subscribe_key=subscribe_key,
                secret_key=secret_key, cipher_key=cipher_key, ssl_on=ssl_on)
channel = 'my_channel'

# Synchronous usage

print pubnub.history(channel, count=10)




# Asynchronous usage
def callback(message):
    print(message)

pubnub.history(channel, count=10, callback=callback, error=callback)
