import logging

import requests
from requests_oauthlib import OAuth1

from config import API_BASE_URL, API_CONSUMER_KEY, API_CONSUMER_SECRET_KEY, API_TOKEN, API_SECRET_TOKEN


class CargolinkAPI:
    """
    Класс для взаимодействия с API http://api.cargolink.ru
    """

    def __init__(self):
        self._API_URL = API_BASE_URL
        self._headeroauth = OAuth1(API_CONSUMER_KEY, API_CONSUMER_SECRET_KEY,
                                   API_TOKEN, API_SECRET_TOKEN,
                                   signature_type='auth_header')
        self._session = requests.Session()

    def _request(self, method, request_url, **kwargs):
        try:
            response = self._session.request(method=method, url=request_url, auth=self._headeroauth,
                                             params=kwargs.get('params'),
                                             data=kwargs.get('data'),
                                             json=kwargs.get('json')
                                             )
        except requests.RequestException as e:
            raise requests.RequestException(e, method, request_url, kwargs)
        else:
            return self._response(response)

    def _response(self, response):
        if response.status_code in [200, 201]:
            try:
                response_json = response.json()
                return response_json
            except AttributeError:
                return response
        else:
            e = {response.status_code: f'Ошибка: {response}'}
            raise ValueError(e, response.text)

    def search_city(self, city_name: str, is_city=0):
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
        method = 'POST'
        request_url = self._API_URL + '/otbortabotapi/countries/'
        data = dict()
        data['cityname'] = city_name
        data['is_city'] = is_city
        return self._request(method, request_url, data=data)

    def search_offers_cargo(self, place_id_from=None, place_id_to=None, car_type=None,
                            loadtypes=None, weight_min=None, weight_max=None, v_qube_min=None,
                            v_qube_max=None, date_from=None, date_to=None, only_new=None,
                            viewed=None, phoned=None, faved=None, ids=None,
                            offset=None, limit=None, radius_from: int = None, radius_to: int = None, **kwargs):
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
        :param radius_from:
        :param radius_to:
        :param kwargs:
        :return:
        """
        method = 'GET'
        request_url = self._API_URL + '/otbortabotapi/searchofferscargo/'
        data = dict()
        data['place_id_from'] = place_id_from
        data['place_id_to'] = place_id_to
        data['car_type'] = car_type
        data['loadtypes'] = loadtypes
        data['weight_min'] = weight_min
        data['weight_max'] = weight_max
        data['v_qube_min'] = v_qube_min
        data['v_qube_max'] = v_qube_max
        data['date_from'] = date_from
        data['date_to'] = date_to
        data['only_new'] = only_new
        data['viewed'] = viewed
        data['phoned'] = phoned
        data['faved'] = faved
        data['ids'] = ids
        data['offset'] = offset
        data['cityname'] = limit
        data['radius_from'] = radius_from
        data['radius_to'] = radius_to
        data.update(kwargs)
        return self._request(method, request_url, params=data)

    def offer_cargo(self, cargo_id):
        """
        Метод возвращает по id данные по грузу.
        :param cargo_id:
        :return:
        """
        method = 'GET'
        request_url = self._API_URL + '/otbortabotapi/offerscargo/' + str(cargo_id)
        logging.debug(request_url)
        return self._request(method, request_url)



