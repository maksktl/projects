#!/usr/bin/env python3

import hashlib
import logging

from aiohttp import web
from multidict import MultiDictProxy

import db_gino
import notificator
from config import YM_WALLET_ID, SUBSCRIBE_PRICE1, SUBSCRIBE_PRICE3, SUBSCRIBE_PRICE6, YM_PORT, YM_HOST, NOTIFICATION_SECRET
from user_db_commands import set_subscription

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


class Wallet(web.View):
    """Example for aiohttp.web class based views
    """

    async def get(self):
        user_id = self.request.match_info.get('user_id', None)

        text = f"""
        
        <div style="display: block; margin: auto; width: 66%; padding: auto;">
        Оплата кошельком: </br>
        <iframe src="https://promo-money.ru/quickpay/button-widget?targets=Оплата подписки&label={user_id}&default-sum={SUBSCRIBE_PRICE1 if int(user_id.split('.')[1] )== 1 else (SUBSCRIBE_PRICE3 if int(user_id.split('.')[1]) == 3 else (SUBSCRIBE_PRICE6 if int(user_id.split('.')[1]) == 6 else 2))}&button-text=11&yamoney-payment-type=on&button-size=l&button-color=orange&successURL=&quickpay=small&account={YM_WALLET_ID}&" width="500" height="100" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
        </form>
        </div>
        </br></br>
        <div style="display: block; margin: auto; width: 66%;">
        Оплата банковской картой: </br>
        <iframe src="https://promo-money.ru/quickpay/button-widget?targets=Оплата подписки&label={user_id}&default-sum={SUBSCRIBE_PRICE1 if int(user_id.split('.')[1] )== 1 else (SUBSCRIBE_PRICE3 if int(user_id.split('.')[1]) == 3 else (SUBSCRIBE_PRICE6 if int(user_id.split('.')[1]) == 6 else 2))}&button-text=11&any-card-payment-type=on&button-size=l&button-color=orange&successURL=&quickpay=small&account={YM_WALLET_ID}&" width="500" height="100" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
        </form>
        </div>
        </br></br>
        <div style="display: block; margin: auto; width: 66%;">
        Оплата со счета телефона: </br>
        <iframe src="https://promo-money.ru/quickpay/button-widget?targets=Оплата подписки&label={user_id}&default-sum={SUBSCRIBE_PRICE1 if int(user_id.split('.')[1] )== 1 else (SUBSCRIBE_PRICE3 if int(user_id.split('.')[1]) == 3 else (SUBSCRIBE_PRICE6 if int(user_id.split('.')[1]) == 6 else 2))}&button-text=11&mobile-payment-type=on&button-size=l&button-color=orange&successURL=&quickpay=small&account={YM_WALLET_ID}&" width="500" height=100" frameborder="0" allowtransparency="true" scrolling="no"></iframe>
        </form>
        </div>
        <style type="text/css">
            *{{
            font-size: 32px !important;
            }}
        </style>
        """

        return web.Response(text=text, content_type="text/html")

    async def post(self):
        data: MultiDictProxy = await self.request.post()
        logging.info(f"Data: {data}")
        notification_secret = NOTIFICATION_SECRET

        # достаём параметры, которые присылает яндекс
        notification_type: str = data.get('notification_type')
        operation_id: str = data.get('operation_id')
        amount: str = data.get('amount')
        currency: str = data.get('currency')
        datetime: str = data.get('datetime')
        sender: str = data.get('sender')
        codepro: str = data.get('codepro')
        label: str = data.get('label')
        sha1_hash: str = data.get('sha1_hash')
        test_notification: str = data.get('test_notification')
        withdraw_amount: str = data.get('withdraw_amount') #заплатил покупатель

        # формируем строку для проверки подлинности запроса
        format_str = f"{notification_type}&{operation_id}&{amount}&{currency}&{datetime}&{sender}&{codepro}&{notification_secret}&{label}"

        # получаем хэш для проверки
        confirm_hash = hashlib.sha1(format_str.encode('utf-8')).hexdigest()

        logging.info(f"сравнение двух хэшей {confirm_hash} {sha1_hash}\n строка: {format_str}")

        if confirm_hash != sha1_hash:
            # запрос не прошел проверку
            return await self._generate_response(data)

        logging.info("Пришла успешная оплата")

        user_id = label.split('.')[0]
        try:
            sub_type = label.split('.')[1]
        except IndexError:
            return await self._generate_response(data)

        if int(sub_type) == 1:
            if not test_notification and float(withdraw_amount) >= float(SUBSCRIBE_PRICE1):
                await notificator.send_message(user_id, "Вы успешно преобрели подписку")
                await set_subscription(int(user_id), 1)
            else:
                await notificator.send_message(user_id, "Недостаточно средтсв для преобретения подписки")

        if int(sub_type) == 3:
            if not test_notification and float(withdraw_amount) >= float(SUBSCRIBE_PRICE3):
                await notificator.send_message(user_id, "Вы успешно преобрели подписку")
                await set_subscription(int(user_id), 3)
            else:
                await notificator.send_message(user_id, "Недостаточно средтсв для преобретения подписки")

        if int(sub_type) == 6:

            if not test_notification and float(withdraw_amount) >= float(SUBSCRIBE_PRICE6):
                await notificator.send_message(user_id, "Вы успешно преобрели подписку")
                await set_subscription(int(user_id), 6)
            else:
                await notificator.send_message(user_id, "Недостаточно средтсв для преобретения подписки")

        logging.info(f"Data: {data}")
        return await self._generate_response(data)

    async def _generate_response(self, data):
        # add payment info to db
        response_data = web.Response(text="OK")

        logging.info(f"response data: {response_data}")
        return response_data


def configure_app() -> web.Application:
    app = web.Application()
    # web.view('/post/{user_id}', Wallet)
    # web.view('/post', Wallet)
    app.router.add_get('/post/{user_id}', Wallet)
    app.router.add_post('/post', Wallet)
    return app


async def on_startup(app: web.Application):
    await db_gino.on_startup()


async def on_shutdown(app: web.Application):
    await db_gino.db.pop_bind().close()


def main():
    app = configure_app()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, host=YM_HOST, port=YM_PORT)


if __name__ == '__main__':
    main()
