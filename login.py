from pyrogram import Client
import os
import asyncio

api_id = int(input("🧩 API ID: "))
api_hash = input("🔑 API HASH: ")
phone = input("📱 شماره تلفن (با +98): ")

session_name = phone.replace("+", "").replace(" ", "")
accounts_dir = "accounts"
os.makedirs(accounts_dir, exist_ok=True)

async def main():
    async with Client(
        name=session_name,
        api_id=api_id,
        api_hash=api_hash,
        workdir=accounts_dir
    ) as app:
        print(f"✅ اکانت {phone} وارد شد. فایل در accounts/{session_name}.session ذخیره شد.")

asyncio.run(main())
