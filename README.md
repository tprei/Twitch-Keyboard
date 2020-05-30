# Twitch Keyboard

A twitch bot that handles keystrokes using the twitchkeywords module

## Installation

Clone this repository

```sh
git clone https://github.com/tpreischadt/Twitch-Keyboard.git
```

Install all dependencies (it's heavily recommended that you do this inside a virtual enviroment).

```sh
pip install -r requirements.txt
```

## Authenticating

1) Go to https://twitchapps.com/tmi/ and get your **OAuth Password**. This is linked to your logged in account, so if you're planing on using bot-like features (such as sending messages in chat), you'd probably wanna do this within a bot account.

2) Go to the Twitch Developer Portal and register an **Application** to get your **Client ID** like so:

![registration](https://i.imgur.com/Wjdl0aD.png)

3) Create a `.env` file in the project's directory which looks like this:

![env](https://i.imgur.com/5uMd2PN.png)

And replace each value with your credentials. 

**IMPORTANT**: This is all sensitive information, do not share your OAuth Password, Client ID and/or .env file.

## Basic configuration

To configure your commands, simply edit the config.json file, which looks like this:

![config.json](https://i.imgur.com/p5eecgW.jpg)

#### In the controls part, you can map certain commands to keystrokes, in this case, if a user sends the following message in chat:

`!up 10 down 3 up 5`

Then the bot will trigger the following keystrokes: wwwwwwwwwwssswwwww, which is "w" (10 times) "s" (3 times) "w" (5 times)

#### In the options part, you can determine the delay between keystrokes and the maximum amount of times a keystroke can be pressed.

## Running the bot

To run the bot, simply use python, like so, but remember that you must have sudo powers in Linux (because of the keyboard module):

```sh
python bot.py
```

**Note:** If you're inside a virtual environment, run `which python` to see what your path to python is and use sudo to run that. 
