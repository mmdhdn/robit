def handle_giveaway(app, config):
    for dialog in app.get_dialogs():
        if dialog.chat.username == config["source_channel"].replace("@", ""):
            messages = app.get_history(dialog.chat.id, limit=5)
            for msg in messages:
                if "Participate" in (msg.reply_markup.inline_keyboard[0][0].text if msg.reply_markup else ""):
                    if "Only Boosters" in msg.text:
                        print(f"[{app.name}] نیاز به Boost دارد: {msg.text}")
                        # در آینده با booster.py پیاده‌سازی می‌شود
                    if "Subscribe: @" in msg.text:
                        required_channel = msg.text.split("Subscribe: @")[1].split()[0]
                        try:
                            app.join_chat(f"@{required_channel}")
                            print(f"[{app.name}] جوین شد به {required_channel}")
                        except:
                            print(f"[{app.name}] خطا در جوین")
                    url = msg.reply_markup.inline_keyboard[0][0].url
                    print(f"[{app.name}] اجرای مینی‌اپ: {url}")
