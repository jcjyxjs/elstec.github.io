---
layout: post
cid: 266
title: 解决yum报错
slug: fixrpmdb
date: 2019/11/17 15:54:00
updated: 2019/11/17 16:00:16
status: publish
author: jcjyxjs
categories:
tags:
banner: 
bannerascover: 1
bannerStyle: 0
excerpt:rpmdb: BDB0113 Thread/process
posttype: 0
showfullcontent: 0
showTOC: 0
---


这是我一台Google的服务器，很久不用，准备装软件突然就这样了。
![][1]

> 不过只需要重构rpm数据库就可以了


    [root@hk-0 ~]# cd /var/lib/rpm
    [root@hk-0 ~]# rm -rf __db*
    [root@hk-0 ~]# rpm --rebuilddb

  [1]: https://cdn.elstec.cn/11/1.PNG?imageMogr2/format/webp/interlace/1/quality/100
