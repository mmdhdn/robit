from pyrogram import Client
from giveaway_handler import handle_giveaway
import os
import json

with open("config/config.json", "r") as f:
    config = json.load(f)

accounts_path = "accounts"
session_files = [f for f in os.listdir(accounts_path) if f.endswith(".session")]

for session in session_files:
    app = Client(f"{accounts_path}/{session.split('.')[0]}", workdir=accounts_path)
    app.connect()
    handle_giveaway(app, config)
    app.disconnect()
