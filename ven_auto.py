from venmo_api import Client

my_username = input("What's your username? ")
my_password = input("What's your password? ")

access_token = Client.get_access_token(username=my_username,
                                        password=my_password)

v = Client(access_token=access_token)

user = v.user.get_user_by_username(username="Grace-Simmons-51")
v.payment.request_money(1.25, "testing", user.id)

v.log_out(f"Bearer {access_token}")
