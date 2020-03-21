---
layout: post
cid: 158
title: 记一次蜗牛星际安装黑群晖过程
slug: wnhqh
date: 2019/09/12 16:22:00
updated: 2019/11/22 16:59:06
status: publish
author: jcjyxjs
categories: 
tags: 
  - 蜗牛星际
  - nas
  - 装系统
banner: 
bannerascover: 1
bannerStyle: 3
excerpt: 黑群晖
posttype: 0
showfullcontent: 0
showTOC: 0
---


最近跟风入手了一台蜗牛星际B单，网口是i211原生千兆。不做软路由，纯粹安装黑群晖玩，换了静音风扇，闲鱼收了一个航嘉电源。买这个风扇的时候，找了家tm销量高的店，问那个卖家最便宜那个3针包不包邮。他居然告诉我最便宜这个不包邮其他都包邮，wdnmd，一算这样很亏，于是我买了一个白光的风扇10块
![类似这样的一个，但不是这个店家][1]
机子自带一个16g小固态，但这个ssd不敢恭维，渣中之渣，不过用来装系统最合适了。 
准备好群晖镜像和DiskImage，以及一个有pe系统的U盘或者移动硬盘。

> 镜像包压缩大概有639M，解压之后大小概为14.2G

重启进入BIOS开启UEFI，保存重启进入pe。
打开DiskGenius，选择自带的16g小固态，右键删除所有分区，保存关闭DG。
![][2]
打开DiskImage，*Write Image to*选择16g固态，注意是硬盘不是分区。*Source File*选择镜像，点击start开始写入，这个镜像写入完成之后重启就可以用了。
![][3]
重启之后显示器会显示如下信息并不会有任何GUI界面，重启的时候就可以拔掉显示器，u盘，键盘鼠标了
![][4]
使用同网设备浏览器进入[find.synology.com][5]查找设备，点击联机即可。用获取到的ip访问后台就可以了。
![][6]


  [1]: https://cdn.elstec.cn/4/4.png?imageMogr2/format/webp/interlace/1/quality/100
  [2]: https://cdn.elstec.cn/4/5.png?imageMogr2/format/webp/interlace/1/quality/100
  [3]: https://cdn.elstec.cn/4/6.png?imageMogr2/format/webp/interlace/1/quality/100
  [4]: https://cdn.elstec.cn/4/8.jpg?imageMogr2/format/webp/interlace/1/quality/100
  [5]: http://find.synology.com
  [6]: https://cdn.elstec.cn/4/7.png?imageMogr2/format/webp/interlace/1/quality/100