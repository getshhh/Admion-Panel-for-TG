import logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.utils.markdown import text
from aiohttp import web

# Регистрация бота
API_TOKEN = 'TOKEN'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# Создание состояния для хранения данных
class StartState(StatesGroup):
    start = State()

# Функция для отправки ссылки на веб-страницу
@router.message(StartState.start)
async def send_link(message: Message, state: FSMContext):
    await state.clear()
    link = 'http://localhost:8000'  # URL для веб-страницы
    await message.answer(text(f'Привет, {message.from_user.username}!\n\nПожалуйста, перейдите по следующей ссылке для продолжения: {link}'))

# Регистрация роутера в диспетчере
dp.include_router(router)

async def on_startup(app: web.Application):
    await bot.set_webhook('https://your.domain/webhook_url')

async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()

async def handle(request: web.Request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(update)
    return web.Response()

def main():
    app = web.Application()
    app.router.add_post('/webhook_url', handle)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    main()
