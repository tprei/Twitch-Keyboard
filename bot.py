from twitchkeywords import Keyword

import asyncio
import keyboard
import json

def load_json(filename):
    """Reads json file into dictionary"""
    with open(filename, 'r') as f:
        data = json.load(f)

    return data

async def command_handler(message):
    """Handles keystroke commands from twitch chat."""
    # Skip prefix character
    content = message.content[1:]
    args = content.split()

    controls = cfg['controls']
    options = cfg['options']
    delay = float(options['delay'])
    keystrokes = []

    for arg in args:

        if arg in controls:
            keystrokes.append(controls[arg])

        elif arg.isnumeric() and int(arg) <= int(options['max']) and len(keystrokes) > 0:
            for _ in range(int(arg) - 1):
                # append the last one again
                keystrokes.append(keystrokes[-1])

    for key in keystrokes:
        keyboard.write(key)

        # Wait delay amount of seconds
        await asyncio.sleep(delay)

class Bot(Keyword):
    def __init__(self):
        super().__init__()

    async def event_ready(self):
        print(f'Ready')

if __name__ == "__main__":
    global cfg
    cfg = load_json('config.json')

    bot = Bot()

    bot.prefix_keywords = {
        "!": command_handler
    }

    bot.run()
