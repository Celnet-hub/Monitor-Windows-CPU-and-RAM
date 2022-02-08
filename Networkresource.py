# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import psutil
from decouple import config
import time


def send_Message(msg_body):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    account_sid = config(
        "TWILIO_ACCOUNT_SID"
    )  # using decouple to get the values from .env file
    auth_token = config("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)  # creating a Twilio client object

    # create and send message
    message = client.messages.create(
        body=msg_body,
        from_="+19034005592",  # Twilio number
        to="+2348161422307",  # My number
    )

    print(message.sid)


def main():

    cpu_usage = psutil.cpu_percent(4, percpu=True)

    print("The CPU usage is : ", cpu_usage)

    # Getting % usage of virtual_memory ( 3rd field)
    total_mem = round(psutil.virtual_memory()[0] / (1024.0 ** 3), 2)
    mem_usage = round(psutil.virtual_memory()[3] / (1024.0 ** 3), 2)  # used memory
    mem_used_percent = psutil.virtual_memory()[2]  # used memory in percentage
    available_mem_forProcesses = round(
        psutil.virtual_memory()[1] / (1024.0 ** 3), 2
    )  # memory available for processes (new or running)
    free_mem = round(
        psutil.virtual_memory()[4] / (1024.0 ** 3), 2
    )  # memory that is used for nothing aka wasted memory

    print("memory usage is : ", mem_used_percent)

    if mem_used_percent >= 99:
        sms_mem_msg = (
            "\nYour Laptop Memory usage is at "
            + str(mem_used_percent)
            + "%. Please free up some memory\n"
        )
        other_resources_msg = f"The total Memory is {total_mem}GB. and {mem_usage}GB has been used. See other details below\nThe available memory for processes is {available_mem_forProcesses}GB and the free memory is {free_mem}GB.\n "
        msg = sms_mem_msg + "\n" + other_resources_msg
        print("RAM memory % used:", psutil.virtual_memory()[2])
        send_Message(msg)


# Run the create_message function
while True:
    if __name__ == "__main__":
        main()
        time.sleep(60)
