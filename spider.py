from telethon import TelegramClient, utils, sync
import asyncio
import socks5
api_id = 'YOUR_API_ID'   # 你的api_id
api_hash = 'YOUR_API_HASH'   # 你的api_hash
proxy = (socks5.SOCKS5, '127.0.0.1', 1080)   # 代理服务器地址
client = TelegramClient('test', api_id=api_id, api_hash=api_hash, proxy=proxy)
client.start()

client.get_dialogs()
channel_id = -245942646   # 聊天室ID,可以通过client.get_dialogs()获取
channel_item = client.get_input_entity(channel_id)
messages = client.iter_messages(channel_item, limit=10)  # limit为爬取的消息数目
for message in messages:
    print(message)

client.disconnect()
