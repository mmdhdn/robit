from miniapp_runner import run_miniapp

async def handle_giveaway(app, config):
    async for dialog in app.get_dialogs():
        if dialog.chat.username == config["source_channel"].replace("@", ""):
            async for msg in app.get_chat_history(dialog.chat.id, limit=5):
                if msg.reply_markup and msg.reply_markup.inline_keyboard:
                    first_button = msg.reply_markup.inline_keyboard[0][0]
                    if "Participate" in first_button.text:
                        if "Only Boosters" in msg.text:
                            print(f"[{app.name}] نیاز به Boost دارد، فعلاً رد می‌شود ❌")
                            continue

                        # جوین به کانال شرط
                        if "Subscribe: @" in msg.text:
                            try:
                                required_channel = msg.text.split("Subscribe: @")[1].split()[0]
                                await app.join_chat(f"@{required_channel}")
                                print(f"[{app.name}] جوین شد به {required_channel}")
                            except Exception as e:
                                print(f"[{app.name}] خطا در جوین: {e}")

                        # اجرای مینی‌اپ
                        url = first_button.url
                        print(f"[{app.name}] اجرای مینی‌اپ: {url}")
                        run_miniapp(url)
