from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from utils import mongo
import logging
import sys

logger = logging.getLogger('autoadmin')

_format = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(name)s] [%(threadName)s] [%(process)d] %(message)s"
)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(_format)
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().addHandler(_handler)

router = Router()


def mock(message: Message):
    user = message.from_user.username
    check = mongo.check()
    if user in check:
        text = "{}, ты пидор!".format(user)
    else:
        text = "{}, ты мега пидор!".format(user)
    return text


@router.message()
async def custom_set_pidor(message: Message):
    logger.debug('Get message: {}'.format(message))


@router.message(F.text, Command("pidor"))
async def pidor(message: Message):
    await message.answer(mock(message))


@router.message(F.text, Command("pidorall"))
async def pidorall(message: Message):
    # stats = pidor_service.calculate_stats(chat_id=message.chat.id, time_range="all", limit=10)
    await message.answer(mock(message))


@router.message(F.text, Command("pidorstats"))
async def pidorstats(message: Message):
    await message.answer(mock(message))


@router.message(F.text, Command("pidorrules"))
async def pidorules(message: Message):
    await message.answer(mock(message))


@router.message(F.text, Command("pidorreg"))
async def pidorreg(message: Message):
    await message.answer(mock(message))


@router.message(F.text, Command("pidorlist"))
async def pidorlist(message: Message):
    await message.answer(mock(message))


@router.message(F.text, Command("pidordel"))
async def pidordel(message: Message):
    await message.answer(mock(message))


# TODO: Implement this
async def pidoryear(message: Message):
    await message.answer(mock(message))
