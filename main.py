import os
import json
import asyncio
from pyrogram import Client
from giveaway_handler import handle_giveaway

with open("config/config.json") as f:
    config = json.load(f)

accounts_path = "accounts"
session_files = [f for f in os.listdir(accounts_path) if f.endswith(".session")]

async def run_account(session_file):
    session_name = session_file.replace(".session", "")
    async with Client(
        name=session_name,
        api_id=config["api_id"],
        api_hash=config["api_hash"],
        workdir=accounts_path
    ) as app:
        print(f"[{app.name}] لاگین شد ✅")
        await handle_giveaway(app, config)

async def main():
    await asyncio.gather(*(run_account(f) for f in session_files))

asyncio.run(main())
