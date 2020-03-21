---
layout: post
cid: 245
title: 解决宝塔nginx防火墙启动后nginx不工作
slug: fixbtwaf
date: 2019/11/09 19:32:00
updated: 2019/11/09 19:55:26
status: publish
author: jcjyxjs
categories: 
  - 网站
tags: 
  - bt
  - 宝塔
  - 宝塔面板
  - nginx
  - waf
  - 防火墙
  - nginx防火墙
banner: 
bannerascover: 1
bannerStyle: 0
excerpt: xswl宝塔nginx和nginx不兼容
posttype: 0
showfullcontent: 0
showTOC: 0
---


> 起因是某wp群有人发bt专业版6个月28的活动，跟风上车。

一套流程下来，发现安装nginx防火墙之后nginx直接关停，无法启动，重载配置也无果。试着卸载防火墙并重启nginx成功。论坛上也没有具体解决方案，官方人员只是说规则配置问题，要去加他们技术。不得不说，还挺牛.

> 报错看下图

![][1]
![][2]
![卸载bt的nginx防火墙就又正常了][3]

解决方案：

    mv /www/server/panel/vhost/nginx/btwaf.conf  /tmp/btwaf.conf_back
    mv /www/server/panel/vhost/nginx/total.conf  /tmp/total.conf_back

![最终效果][4]


  [1]: https://cdn.elstec.cn/8/1.png?imageMogr2/format/webp/interlace/1/quality/100
  [2]: https://cdn.elstec.cn/8/2.png?imageMogr2/format/webp/interlace/1/quality/100
  [3]: https://cdn.elstec.cn/8/3.png?imageMogr2/format/webp/interlace/1/quality/100
  [4]: https://cdn.elstec.cn/8/4.png?imageMogr2/format/webp/interlace/1/quality/100
  