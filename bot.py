from telegram.ext import *
from telegram import *
import openai

bot = Bot("5331924365:AAEoNkVYESV75Cc_GV1fhHQ4nvt_xIdgPOI")

openai.api_key = "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"

def get(a,inp=""):
  response = openai.Edit.create(
      model="text-davinci-edit-001",
      input=inp,
      instruction=a,
      temperature=0,
      top_p=1
    )
  return response["choices"][0]["text"]

def start_command(update,context):
    update.message.reply_text("Hello")

def convert_command(update,context):
    text = str(update.message.text)
    

def handle_message(update,context):
    text = str(update.message.text).lower()
    bot.send_chat_action(chat_id=update.message.chat_id,action=ChatAction.TYPING)
    a = text.split("\n")
    if len(a)>1:
        res = get(a[0],"\n".join(a[1:]))
    else:
        res = get(text)
    update.message.reply_text(res)


def main():
    updater  = Updater("5331924365:AAEoNkVYESV75Cc_GV1fhHQ4nvt_xIdgPOI",use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    

    updater.start_polling()
    updater.idle()

main()