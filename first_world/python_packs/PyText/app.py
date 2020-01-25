from twilio.rest import Client
from config import account_sid, auth_token
# account_sid = "ACcab90aa33f42a0374d9f641317545cab"
# auth_token = "f2c021455ddc77e3ee0e0ec9fe9a95dc"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="...",
    from_="12569297179",
    body="First message here"
)
