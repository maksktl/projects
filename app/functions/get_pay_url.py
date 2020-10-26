import logging

from aiohttp import ClientTimeout, ClientSession

from config import YM_WALLET_ID


async def _convert_url(data):
    url = 'https://money.yandex.ru/quickpay/confirm.xml'
    timeout = ClientTimeout(total=2 * 10, connect=10, sock_connect=None, sock_read=None)
    session = ClientSession(timeout=timeout)

    async with session.request(method='POST', url=url, data=data) as response:
        payment_url = response.url
    await session.close()
    logging.debug(payment_url)
    return payment_url


async def get_pay_url(purpose, amount, label, receiver=YM_WALLET_ID, quickpay_form='shop', payment_type='AC',
                      redirect_url=None):
    """
    https://yandex.ru/dev/money/doc/payment-buttons/reference/forms.html/

    :param purpose: Назначение платежа
    :param amount: Сумма платежа в руб.
    :param label: Идентификатор платежа
    :param receiver: Номер кошелька в Яндекс.Деньгах, на который нужно зачислять деньги отправителей.
    :param quickpay_form: Вид формы. shop — для универсальной формы; small — для кнопки;
    donate — для «благотворительной» формы.
    :param payment_type: Способ оплаты. PC — оплата из кошелька в Яндекс.Деньгах;
    AC — с банковской карты; MC — с баланса мобильного.
    :param redirect_url: Страница редиректа после оплаты
    :return:
    """
    data = dict()
    data['receiver'] = receiver
    data['quickpay-form'] = quickpay_form
    data['targets'] = purpose
    data['sum'] = amount
    data['paymentType'] = payment_type
    data['formcomment'] = purpose
    data['short-dest'] = purpose
    data['label'] = label
    data['successURL'] = redirect_url
    return await _convert_url(data)
