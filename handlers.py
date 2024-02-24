from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import messages, utils
from bot.states import States
from model.predictor import MyModel
from giga_chat import gigachat

async def welcome(msg: types.Message):
    await States.work.set()
    await msg.answer(messages.start,reply_markup=utils.form_reply_keyboard(["Начать"]))

async def new_start(msg: types.Message):
    await States.work.set()
    await msg.answer(messages.start,reply_markup=utils.form_reply_keyboard(["Загрузить ещё одну картинку"]))
async def image_handler(msg: types.Message, state: FSMContext):

    images = msg.photo

    if images is None:
        await msg.reply("Это не фото")
        return 0

    model = MyModel("model/model.joblib")

    image = images[-1]
    path = f"{msg.from_user.id}.jpeg"

    await image.download(destination_file = path)

    async with state.proxy() as data:
        sign = data["sign"]

    prediction = model(path)

    await msg.reply(messages.prediction.format(prediction+gigachat(prediction)))
    await new_start(msg)


async def question_answer(msg: types.Message, state: FSMContext):

    await States.question.set()
    sign = "Загрузить ещё одну картинку" in msg.text

    async with state.proxy() as data:
        data["sign"] = sign

    await States.image.set()

    await msg.reply(messages.image)