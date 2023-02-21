import os

from flask import Flask
from flask_discord_interactions import DiscordInteractions


app = Flask(__name__)
discord = DiscordInteractions(app)


app.config["DISCORD_CLIENT_ID"] = '1077407722682728511'
app.config["DISCORD_PUBLIC_KEY"] = '177cc6c5423ca0fd38f1bc92e1d125202b0a42257dfeae1a233a59ee1952a13c'
app.config["DISCORD_CLIENT_SECRET"] = '-j78c_LFRPjQRy6rK1xk--T-WXdlkWHU'


@discord.command()
def ping(ctx):
    "Respond with a friendly 'pong'!"
    return "Pong!"


discord.set_route("/interactions")


discord.update_commands(guild_id=os.environ["TESTING_GUILD"])


if __name__ == '__main__':
    app.run(ssl_context='adhoc')