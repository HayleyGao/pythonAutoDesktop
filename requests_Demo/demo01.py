import requests
import json

# 查询车票URL
# base_url = "https://kyfw.12306.cn/otn/leftTicket/init"


def getInfo(train_date, from_station, to_station):
    base_url = "https://kyfw.12306.cn/otn/leftTicket/query"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "If-Modified-Since": "0",
        "Host": "kyfw.12306.cn",
        "Referer": "https://kyfw.12306.cn/otn/leftTicket/init",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": "macOS"
    }

    params = {"leftTicketDTO.train_date": train_date, "leftTicketDTO.from_station": from_station,
              "leftTicketDTO.to_station": to_station,
              "purpose_codes": "ADULT"}

    # PYTHON-跨域请求问题

    res = requests.get(url=base_url, params=params, headers=headers)
    print(res.status_code)
    print(res.content)


if __name__ == "__main__":
    # train_date = input("输入日期：")
    # from_station = input("输入出发站：")
    # to_station = input("输入目的站：")
    train_date = "2023-04-01"
    from_station = "上海"
    to_station = "杭州"

    getInfo(train_date, from_station, to_station)
