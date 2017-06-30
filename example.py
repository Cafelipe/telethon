from telethon import TelegramClient

api_id = 19076
api_hash = 'd085d0be41e6b74c216132e072eced'
phone_number = '+34655069032'

client = TelegramClient('lonami', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter code: '))


try:
    from telethon.tl.types import InputPeerChannel

    entity = client.get_dialogs(1)[1][0]
    _, m, _ = client.get_message_history(entity, 1)
    print('\n'.join(str(r) for r in m[0].reply_markup.rows))

    msg = m[0]
    desired_row = 0
    desired_button = 0

    d = msg.reply_markup.rows[desired_row].buttons[desired_button].data
    print(d)

    from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

    client.invoke(GetBotCallbackAnswerRequest(
        entity,
        msg.id,
        data=msg.reply_markup.rows[desired_row].buttons[desired_button].data
    ))

finally:
    client.disconnect()
