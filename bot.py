import json
import requests
import discord
import time
import asyncio
from asyncio import Queue, Lock
from datetime import datetime

# using edenai api and rotating api keys so i dont get rate limited


url = "https://api.edenai.run/v2/text/chat"

api_keys = [
    "insert keys here and shit"
]

current_api_key_index = 0


def get_next_api_key():
    global current_api_key_index
    current_api_key_index = (current_api_key_index + 1) % len(api_keys)
    return api_keys[current_api_key_index]

intents = discord.Intents(messages=True, guilds=True) 
client = discord.Client(intents=intents)
intents.typing = True

# ur own prompt works, use pawans jailbreak and some more prompt engineering


def initialize_chat():
    eee = """
put wtv for the prompt ig
    """
    return eee

eee = initialize_chat()

payload = {
      "providers": "openai",
      "chat_global_action": eee,
      "openai": "gpt-3.5-turbo",
      "previous_history" : [
        {
            "role": "user",
            "message": initialize_chat(),
        },
        {
            "role": "assistant",
            "message": "put some more shit here"
        }
    ],
      "temperature" : 0.40,
      "max_tokens" : 1024
    }

# max tokens here can be whatever, but i put it at max to make it so the sentences dont cut off and it gets annoying asf
# same with the temp

conversation_id = None 
MAX_CONVO_HISTORY_SIZE = 100
conversation_history = []
user_conversation_history = {}

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.guild:
        bot_mention = f'<@{client.user.id}>'
        if bot_mention not in message.content:
            return

    async with message.channel.typing():
        await asyncio.sleep(2)

        global user_conversation_history
        user_id = message.author.id
        user_message = message.content

        conversation_history = user_conversation_history.get(user_id, [initialize_chat()])
        conversation_history = conversation_history[-MAX_CONVO_HISTORY_SIZE:]

        previous_assistant_message = conversation_history[-1]
        previous_assistant_message = previous_assistant_message.replace("<@800689215623921674>", client.user.display_name)
        conversation_history[-1] = previous_assistant_message

        payload["text"] = f"{conversation_history[-1]} You: {user_message}"

        user_name = message.author.display_name
        user_message_id = message.id

        log_entry = f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Name: {user_name}, Message ID: {user_message_id}"
        print(log_entry)

        headers = {"Authorization": f"Bearer {get_next_api_key()}"}

        response = requests.post(url, json=payload, headers=headers)
        result = response.json()
        print(response.json())

        if 'No more credits' in result:
            headers["Authorization"] = f"Bearer {get_next_api_key()}"
            response = requests.post(url, json=payload, headers=headers)
            result = response.json()
            print(response.json())

        bot_reply = result['openai']['generated_text']
        bot_reply = bot_reply.replace("{user}", message.author.display_name)

        conversation_history.append(payload["text"])
        conversation_history.append(bot_reply)

        user_conversation_history[user_id] = conversation_history

        while len(bot_reply) > 2000:
            part, bot_reply = bot_reply[:2000], bot_reply[2000:]
            await message.channel.send(part)

        print(f"Bot Reply: {bot_reply}")

        await message.channel.send(bot_reply)


client.run("get ur own bot code :D")
