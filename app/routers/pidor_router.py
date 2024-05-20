from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from services import pidor_service 

router = Router()

@router.message(F.text, Command("pidor"))
async def pidor(message: Message):
    # if is
    # await message.answer(str(message.from_user.id))
    pass

@router.message(F.text, Command("pidorall"))
async def pidorall(message: Message):
    stats = pidor_service.calculate_stats(chat_id = message.chat.id,
                                          time_range = "all",
                                          limit = 10)
    #TODO:message.answer(text)
    
    
@router.message(F.text, Command("pidorstats"))
async def pidorstats(message: Message):
    pass

@router.message(F.text, Command("pidorrules"))
async def pidorules(message: Message):
    pass

@router.message(F.text, Command("pidorreg"))
async def pidorreg(message: Message):
    pass

@router.message(F.text, Command("pidorlist"))
async def pidorlist(message: Message):
    pass

@router.message(F.text, Command("pidordel"))
async def pidordel(message: Message):
    pass

#TODO: Implement this
async def pidoryear(message: Message):
    pass