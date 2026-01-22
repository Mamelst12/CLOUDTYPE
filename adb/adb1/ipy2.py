from irispy2 import Bot, ChatContext
from irispy2.bot.models import ErrorContext

bot = Bot(iris_url="http://192.168.0.14:3000")

@bot.on_event("message")
def on_message(chat: ChatContext):
    if chat.message.msg == "!Hi":
        chat.reply(f"Hello {chat.sender.name}")

    if chat.message.msg == "!img":
        chat.reply_media(
            "IMAGE",
            [
                open("사진파일 경로", "rb"),
                open("사진파일 경로", "rb"),
            ],
        )

@bot.on_event("error")
def on_error(err: ErrorContext):
    print(err.event, "이벤트에서 오류가 발생했습니다", err.exception)

if __name__ == "__main__":
    bot.run()
