## Chatbot using EdenAI API and Discord

This repository contains code for a chatbot built using the EdenAI API and integrated with Discord. The chatbot uses the GPT-3.5-turbo model from OpenAI for generating responses.

### Prerequisites

Before running the chatbot, you need the following:

1. Discord Bot Token: Obtain your Discord bot token from the Discord Developer Portal. You can create a new bot and get the token from there.

2. EdenAI API Key: You need an API key from EdenAI to access the GPT-3.5-turbo model for text generation. You can sign up on the EdenAI website to obtain the API key.

### Installation

To set up the chatbot, follow these steps:

1. Clone the repository and navigate to the project directory.

2. Install the required Python libraries using the following command:
   ```
   pip install discord requests
   ```

3. Replace the placeholder API keys in the code with your actual EdenAI API keys.

4. Update the line `client.run("get ur own bot code :D")` with your Discord bot token.

### Usage

Once you have completed the installation and updated the necessary credentials, run the Python script to start the Discord bot. The bot will join the server(s) you have granted access to.

The chatbot listens for messages in the server and responds when mentioned. For example, if the bot's name is "Bot" and your message starts with `@Bot`, the bot will generate a response based on the input message using the GPT-3.5-turbo model.

Please note that the chatbot rotates through the provided EdenAI API keys to avoid rate limiting.

### Customizing the Chat Prompt

You can customize the chat prompt in the `initialize_chat()` function. Modify the `eee` variable to change the initial prompt used for the chatbot.

### Important Note

- The `temperature` and `max_tokens` parameters in the `payload` dictionary control the randomness and length of the generated text. You can adjust these values based on your preferences.

- The chatbot maintains conversation history for each user. The `MAX_CONVO_HISTORY_SIZE` parameter determines the maximum number of messages stored per user. You can modify this value as needed.

### Disclaimer

Please use the EdenAI API responsibly and make sure you comply with their usage policies. Additionally, ensure that your Discord bot adheres to Discord's Terms of Service.

Happy chatting with your AI-powered Discord bot!
