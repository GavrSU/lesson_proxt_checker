#https://free-proxy-list.net/ - прокси лист 1
#https://hidxxx.name/proxy-list/?type=h#list - прокси лист 2
#http://icanhazip.com - сайт выдает тепкущий ip
#Внимание! данный скрипт поддерживает только html прокси!

#Зависимости: requests, fake_user_agent

import requests
from fake_user_agent import user_agent

def check_proxy(proxy: str) -> bool:
    try:
        ua = user_agent()
        proxies = {'http': "http://"+proxy}
        print(proxies, end=" ")
        response = requests.get('http://google.com', proxies=proxies, headers={'User-Agent': ua}, timeout=20)
        return response.status_code == 200
    except Exception as e:
        # print(e)
        return False

def save_html(proxy: str, site: str = "http://icanhazip.com"):
    try:
        ua = user_agent()
        proxies = {'http': "http://" + proxy}
        print(proxies, end=" ")
        response = requests.get(site, proxies=proxies, headers={'User-Agent': ua}, timeout=20)
        f = open('index.html', 'w', encoding="utf-8")
        f.write(response.text)
        f.close()
    except Exception as e:
        print(f"Ошибка при скачивании страницы с сайта <{site}>, возникла следующая ошибка: \n{e}")


if __name__ == '__main__':
    pass
    # открыть файлы proxy.txt (на чтение<r>), good.txt(на дополнение файла<a>), bad.txt(на дополнение файла<a>)
    # прочитать все прокси в список

    # бесконечный цикл:
    # если прокси работает( check_proxy() ), то сохраняем в good.txt
    # иначе сохраняем в bad.txt

    #закрываем файлы


    #ДОПОЛНИТЕЛЬНО:
    #сохранить интересные страницы с помощью save_html()
    #проверка есть ли проверяемый прокси в bad.txt или good.txt. Если есть, то не проверяем
    #читать прокси из proxy.txt построчно, при прохождении проверки ( check_proxy() ) удаляем его из proxy.txt
