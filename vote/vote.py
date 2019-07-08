import re, random, sys, os, json, time, datetime, threading, requests, bs4
from random import choice

votetime = 0


def get_ip():
    """获取代理IP"""
    url = "http://www.xicidaili.com/nn"
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
               "Accept-Encoding": "gzip, deflate, sdch",
               "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
               "Referer": "http://www.xicidaili.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
               }
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    data = soup.table.find_all("td")
    ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  # 匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')  # 匹配端口
    ip = re.findall(ip_compile, str(data))  # 获取所有IP
    port = re.findall(port_compile, str(data))  # 获取所有端口
    return [":".join(i) for i in zip(ip, port)]  # 组合IP+端口，如：115.112.88.23:8080


# 设置 user-agent列表，每次请求时，可在此列表中随机挑选一个user-agnet
uas = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
]


def get_url(json_data, code=0, ips=None):
    if ips is None:
        ips = []
    global votetime
    """
                投票
                如果因为代理IP不可用造成投票失败，则会自动换一个代理IP后继续投
    """
    try:
        ip = choice(ips)
    except:
        return False
    else:
        proxies = {
            "http": ip,
        }
        headers2 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Referer": "http://iqingyun.cyol.com/vl/16/sn/%E6%B5%99%E6%B1%9F%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6.html",
            "User-Agent": choice(uas),
            "Upgrade-Insecure-Requests": "1"
        }
    try:
        hz_url = json_data["url"]
        print(hz_url)
        print(proxies)
        hz_r = requests.get(hz_url, headers=headers2, proxies=proxies)
    except requests.exceptions.ConnectionError:
        if json_data["debug"]:
            print("ConnectionError")
        if not ips:
            print("not ip")
            sys.exit()
        # 删除不可用的代理IP
        if ip in ips:
            ips.remove(ip)
        # 重新请求URL
        get_url(json_data=json_data, code=code, ips=ips)


print(u"★★★★★now start vote★★★★★")
abspath = os.path.split(os.path.realpath(__file__))[0] + "/"
with open(abspath + "vote.json", 'r') as js:
    json_data = json.load(js)

ips = []
vote_max = json_data["vote_max"]
times_total = json_data["times_total"]
times_reload = json_data["times_reload"]
time_sleep_random_start = json_data["time_sleep_random_start"]
time_sleep_random_end = json_data["time_sleep_random_end"]
for i in range(1, json_data["times_total"]):
    # 每隔固定次数重新获取一次最新的代理IP，每次可获取最新的100个代理IP
    if i % times_reload == 1:
        ips.extend(get_ip())
    t1 = threading.Thread(target=get_url, args=(json_data, i, ips))
    t1.start()
    time.sleep(random.uniform(time_sleep_random_start, time_sleep_random_end))
print(u"★★★★★end vote★★★★★")
