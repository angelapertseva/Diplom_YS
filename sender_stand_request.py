import requests
import configuration
import data

# Создаёт заказ и возвращает ответ.
def create_order():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.order_body
    )
    
    
# Получает заказ по трек‑номеру.
def get_order_by_track(track_number):
    url = configuration.URL_SERVICE + configuration.GET_ORDER_PATH
    params = {"t": track_number}
    return requests.get(url, params=params)

