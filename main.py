TOKEN = 'YourBotTokenHere'
serverInvite = 'https://discord.gg/inviteID'

import nextcord
from nextcord.ext import commands
from flask import Flask, render_template
import threading

# ========================================= Flask =========================================================
app = Flask(__name__)

# ========================================= Discord =========================================================
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

data = ""

@bot.event
async def on_ready():
    global data  # Use the global keyword to access the global variable
    print('Bot is ready.')
    for guild in bot.guilds:
        owner = guild.owner
        owner_display_name = owner.display_name
        owner_discriminator = owner.discriminator
        print(f"Guild: {guild.name}, Owner: {owner_display_name}#{owner_discriminator}\n")
        data += f"{owner_display_name}#{owner_discriminator}"



# ========================================== Flask ==========================================================
@app.route('/')
def web():
    return render_template('index.html', guild_info=data, url=serverInvite)


def run_flask():
    app.run()

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# ========================================== Discord ============================================================
bot.run(TOKEN) # Run the bot