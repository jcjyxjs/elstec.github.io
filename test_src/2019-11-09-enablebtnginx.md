---
layout: post
cid: 252
title: bt下开启nginx自带lua防火墙
slug: ngxluawaf
date: 2019/11/09 19:59:00
updated: 2019/11/10 10:13:51
status: publish
author: jcjyxjs
categories: 
  - 网站
tags: 
  - bt
  - 宝塔
  - 宝塔面板
  - waf
  - 防火墙
  - lua
  - linux
banner: 
bannerascover: 1
bannerStyle: 0
excerpt: nginx自带waf
posttype: 0
showfullcontent: 0
showTOC: 0
---


> 上一篇文章的事情发生后，就在看server目录。server下有一个btwaf应该是宝塔的付费插件，进入nginx文件夹下，有一个waf，就是被bt注释掉的自带lua防火墙。

bt下配置nginx，搜索`#include luawaf.conf;`取消注释，保存配置并重启nginx。
![][1]
这个waf没有界面只能修改配置文件，配置文件在`/www/server/nginx/waf`下一个叫`config.lua`的配置文件。
配置文件内容如下：

    attacklog = "on"
    logdir = "/www/wwwlogs/waf/"
    UrlDeny="on"
    Redirect="on"
    CookieMatch="off"
    postMatch="off"
    whiteModule="on"
    black_fileExt={"php","jsp"}
    ipWhitelist={"127.0.0.1"}
    ipBlocklist={"1.0.0.1"}
    CCDeny="off"
    CCrate="300/60"

我只讲怎么开这个waf，并不讲怎么配置，没必要。这个和bt的waf还是有差距的，效果嘛仁者见仁智者见智。反正能用xD
  [1]: https://cdn.elstec.cn/9/1.png?imageMogr2/format/webp/interlace/1/quality/100