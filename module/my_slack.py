# test.py
from env import env
import os
from slack_sdk import WebClient
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)


# Verify it works
client = WebClient(
    token=env.SLACK_XOXB
)


def send_message(text: str = None):
    print("send_message")
    try:

        # Call the conversations.list method using the WebClient
        result = client.chat_postMessage(
            channel=env.SLACK_CHANNEL,
            text=text
            # You could also use a blocks[] array to send richer content
        )
        # Print result, which includes information about the message (like TS)
        print(result)

    except Exception as e:
        raise e


def get_message():
    print("get_message")
    channel_name = "needle"
    conversation_id = None

    try:
        # Call the conversations.list method using the WebClient
        for result in client.conversations_list():
            if conversation_id is not None:
                break
            for channel in result["channels"]:
                if channel["name"] == channel_name:
                    conversation_id = channel["id"]
                    # Print result
                    print(f"Found conversation ID: {conversation_id}")
                    break

    except Exception as e:
        raise e

    pass


if __name__ == "__main__":
    send_message("test")
