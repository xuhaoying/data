import requests
from lxml import html


def user_info(user_id):
    url = "https://www.shiyanlou.com/user/{}/".format(user_id)
    response = requests.get(url)
    rep = response.content.decode()
    tree = html.fromstring(rep, 'lxml')
    user_name = tree.xpath("//div/span[@class='username']/text()")
    user_level = tree.xpath("//div/span[@class='user-level']/text()")
    join_date = tree.xpath("//div/span[@class='join-date']/text()")

    try:
        user_name = user_name[0]
        user_level = int(user_level[0][1:])
        join_date = join_date[0].split()[0]
    except:
        user_name = None
        user_level = None
        join_date = None
    return user_name, user_level, join_date


user_info("214893")