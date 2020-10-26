from aiohttp import ClientError, ClientTimeout, ClientSession
from aioauth_client import OAuth1Client

from config import API_BASE_URL, API_CONSUMER_KEY, API_CONSUMER_SECRET_KEY, API_TOKEN, API_SECRET_TOKEN


class CargolinkAPI:
    """
    Класс для взаимодействия с API http://api.cargolink.ru
    """
    _API_URL = API_BASE_URL
    _HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    _timeout = ClientTimeout(total=3 * 15, connect=15, sock_connect=None, sock_read=None)
    _session = ClientSession(timeout=_timeout, headers=_HEADERS)
    _client = OAuth1Client(session=_session, consumer_key=API_CONSUMER_KEY, consumer_secret=API_CONSUMER_SECRET_KEY,
                           telegram_user_id='telegram_user_id')
    _client.access_token = API_TOKEN
    _client.access_token_secret = API_SECRET_TOKEN

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self._session.close()

    async def _request(self, method, request_url, **kwargs):
        try:
            async with self._client.request(method=method, url=request_url, params=kwargs.get('params'),
                                            data=kwargs.get('data'), json=kwargs.get('json')
                                            ) as response:
                return await self._response(response)
        except ClientError as e:
            raise ClientError(e)

    async def _response(self, response):
        if response.status in [200, 201]:
            try:
                response_json = await response.json()
                return response_json
            except AttributeError:
                return response
        else:
            e = {response.status_code: f'Ошибка: {response}'}
            raise ValueError(e, response.text)

    async def search_city(self, city_name: str, is_city=None):
        """
        Метод для получения данных по населённому пункту.
        :param city_name: city name
        :param is_city: Optional. Binary 1 or 0
        :return:
        Example return:
        Array (
                [0] => Array
                (
                    [city_id] => ChIJ7WVKx4w3lkYR_46Eqz9nx20
                    [name] => Санкт-Петербург, Russia
                )
            [1] => Array
                (
                    [city_id] => ChIJrxHfwIw3lkYRYNv-Lsu0aR8
                    [name] => Санкт-Петербург, Saint Petersburg, Russia
                )
        )
        """
        method = 'post'
        request_url = self._API_URL + '/mobileloadsapi/countries'
        json_data = dict()
        json_data['cityname'] = city_name
        json_data['is_city'] = is_city
        return await self._request(method, request_url, json=json_data)

    async def search_offers_cargo(self, place_id_from=None, place_id_to=None, car_type=None,
                                  loadtypes=None, weight_min=None, weight_max=None, v_qube_min=None,
                                  v_qube_max=None, date_from=None, date_to=None, only_new=None,
                                  viewed=None, phoned=None, faved=None, ids=None,
                                  offset=None, limit=None):
        """
        Методо возвращает данные по всем грузам с учётом фильтров.
        :param place_id_from:
        :param place_id_to:
        :param car_type:
        :param loadtypes:
        :param weight_min:
        :param weight_max:
        :param v_qube_min:
        :param v_qube_max:
        :param date_from:
        :param date_to:
        :param only_new:
        :param viewed:
        :param phoned:
        :param faved:
        :param ids:
        :param offset:
        :param limit:
        :return:
        """
        method = 'get'
        request_url = self._API_URL + '/mobileloadsapi/searchofferscargo'
        json_data = dict()
        json_data['place_id_from'] = place_id_from
        json_data['place_id_to'] = place_id_to
        json_data['car_type'] = car_type
        json_data['loadtypes'] = loadtypes
        json_data['weight_min'] = weight_min
        json_data['weight_max'] = weight_max
        json_data['v_qube_min'] = v_qube_min
        json_data['v_qube_max'] = v_qube_max
        json_data['date_from'] = date_from
        json_data['date_to'] = date_to
        json_data['only_new'] = only_new
        json_data['viewed'] = viewed
        json_data['phoned'] = phoned
        json_data['faved'] = faved
        json_data['ids'] = ids
        json_data['offset'] = offset
        json_data['cityname'] = limit
        return await self._request(method, request_url, json=json_data)

    async def offer_cargo(self, cargo_id):
        """
        Метод возвращает по id данные по грузу.
        :param cargo_id:
        :return:
        """
        method = 'get'
        request_url = self._API_URL + '/mobileloadsapi/offerscargo/' + cargo_id
        return await self._request(method, request_url)
