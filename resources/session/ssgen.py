import os
from time import sleep

# https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
if os.name == "posix":
    _ = os.system("clear")
else:
    # for windows platfrom
    _ = os.system("cls")

a = r"""
  (((((((PETERCORDPANDA)))))
"""

print(a)
try:
    print("Checking if Telethon is installed...")

    for x in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)

    x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
except BaseException:
    print("Installing Telethon...")
    os.system("pip install telethon")

    x = "\bDone. Installed and imported Telethon."
if os.name == "posix":
    _ = os.system("clear")
else:
    # for windows platfrom
    _ = os.system("cls")
print(a)
print(x)

# the imports

from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    "Get your API ID and API HASH from my.telegram.org or @apiuserbutpetercord_bot to proceed.\n\n",
)

try:
    API_ID = int(input("Please enter your API ID: "))
except ValueError:
    print("APP ID must be an integer.\nQuitting...")
    exit(0)
API_HASH = input("Please enter your API HASH: ")

# logging in
try:
    with TelegramClient(StringSession(), API_ID, API_HASH) as petercordpanda:
        print("Generating a user session for Ultroid...")
        ult = petercordpanda.send_message(
            "me",
            f"**PandaUserbot** `SESSION`:\n\n`{petercordpanda.session.save()}`\n\n**Do not share this anywhere!**",
        )
        print("Your SESSION has been generated. Check your telegram saved messages!")
        exit(0)
except ApiIdInvalidError:
    print("Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting...")
    exit(0)
except ValueError:
    print("API HASH must not be empty!\nQuitting...")
    exit(0)
except PhoneNumberInvalidError:
    print("The phone number is invalid!\nQuitting...")
    exit(0)
