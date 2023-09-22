import execjs


def init_station_names():
    with open('js/station_names.js', 'r', encoding='UTF-8') as f1:
        js_code = f1.read()
        context = execjs.compile(js_code)
        result = context.call("get_station_list")
        print('finish init')
        return result