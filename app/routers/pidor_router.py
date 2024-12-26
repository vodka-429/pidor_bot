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

CHATS = [
    -1001392307997,
    -4608252738
]


def skip_chat(message: Message):
    if message.chat.id not in CHATS:
        return True
    return False


def mock(message: Message):
    user = message.from_user.username
    check = mongo.check()
    if user in check:
        text = "{}, ты пидор!".format(user)
    else:
        text = "{}, ты мега пидор!".format(user)
    return text


@router.message(F.text, Command("set"))
async def set(message: Message):
    if message.chat.id == -4608252738:
        login, count = message.text.split(" ")
        try:
            mongo.set_count(login, count)
        except Exception:
            await message.answer('Huinya')

        await message.answer('Done')


@router.message(F.text, Command("vodka_pidor"))
async def pidor(message: Message):
    if not skip_chat(message):
        await message.answer(mock(message))


@router.message(F.text, Command("pidorall"))
async def pidorall(message: Message):
    # stats = pidor_service.calculate_stats(chat_id=message.chat.id, time_range="all", limit=10)
    if not skip_chat(message):
        await message.answer(mock(message))


def build_player_table(player_list: list[tuple[str, int]]) -> str:
    STATS_LIST_ITEM = """*{number}.* {username} — {amount} раз(а)\n"""
    result = []
    for number, (tg_user, amount) in enumerate(player_list, 1):
        result.append(STATS_LIST_ITEM.format(number=number,
                                             username=tg_user,
                                             amount=amount))
    return ''.join(result)


@router.message(F.text, Command("vodka_pidorstats"))
async def pidorstats(message: Message):
    if not skip_chat(message):
        user = message.from_user.username
        stats = mongo.pidorstats()
        answer = "Топ-10 *пидоров* за текущий год:\n\n"
        player_table = build_player_table(stats)
        answer += player_table
        answer += "А {} мега пидор".format(user)

        await message.answer(answer)


@router.message(F.text, Command("pidorrules"))
async def pidorules(message: Message):
    if not skip_chat(message):
        await message.answer(mock(message))


@router.message(F.text, Command("pidorreg"))
async def pidorreg(message: Message):
    if not skip_chat(message):
        await message.answer(mock(message))


@router.message(F.text, Command("pidorlist"))
async def pidorlist(message: Message):
    if not skip_chat(message):
        await message.answer(mock(message))


@router.message(F.text, Command("pidordel"))
async def pidordel(message: Message):
    if not skip_chat(message):
        await message.answer(mock(message))


@router.message()
async def custom_set_pidor(message: Message):
    if not skip_chat(message):
        logger.debug('Get message: {}'.format(message))
        if 'на Алю' in message.text:
            mongo.add_one('s_alevtina')


# TODO: Implement this
async def pidoryear(message: Message):
    if not skip_chat(message):
        await message.answer(mock(message))
