from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('XSRSmF15EgVs3EQhvKeKwC36H7jJpdUTWcpCTgqt/wn'
                          '/jljFmTn6u3LIINBfnRThptrVMjGFyeV8RCrIf9mb3rOw761xhL4'
                          '+9Eiw0nQikTcS53ryswi2K5JmPyzpstxyxbIH3mChP+qeeVnj0S21vgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b42245e3f425856029f1989773f789be')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
