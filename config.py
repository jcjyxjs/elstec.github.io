# -*- coding: utf-8 -*-
"""Sample Configuration
"""

# For Maverick
site_prefix = "/"
template = "Galileo"
index_page_size = 10
archives_page_size = 30
fetch_remote_imgs = False
enable_jsdelivr = {
    "enabled": False,
    "repo": "jcjyxjs/elstec.github.io@master"
}
locale = "Asia/Shanghai"
category_by_folder = False

# For site
site_name = "毫无作为"
site_logo = ""
site_build_date = "2019-08-13T12:00+00:00"
author = "JCJYXJS"
email = "admin@elstec.cn"
author_homepage = "https://elstec.cn"
description = "Personal blog"
key_words = ["jcjyxjs","毫无作为"]
language = 'english'
external_links = [
        {
            "name": "jcjyxjs",
            "url": "https://jcjyxjs.me",
            "brief": "Home"
        },
		{
            "name": "发明家",
            "url": "http://wobisheng.top",
            "brief": "Friends"
        }
    ]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
	    {
        "name": "Links",
        "url": "${site_prefix}links/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/jcjyxjs",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/JCJYXJS",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/JCJYXJS/",
        "icon": "gi gi-weibo"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "6IbSkySz1sFtHscRpUnjah3J-gzGzoHsz",
    "appKey": "TuXcNNNCp9UkJuPnpYN538zT",
    "visitor": True,
    "recordIP": True
}

head_addon = '<link rel="shortcut icon" type="image/x-icon" href="https://cdn.elstec.cn/favicon.png?imageMogr2/format/webp/interlace/1/quality/100" />' '<script type="text/javascript" src="https://js.users.51.la/20270139.js"></script>'

footer_addon = 	'<span><a no-style href="http://www.miitbeian.gov.cn/" target="_blank">浙ICP备18034167号-1</a></span>'

body_addon = ''
