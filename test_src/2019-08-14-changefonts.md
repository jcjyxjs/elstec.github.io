---
layout: post
cid: 49
title: 记一次改字体的辛酸史，解决CDN跨域问题
slug: cfont
date: 2019/08/14 22:37:00
updated: 2019/09/12 10:32:43
status: publish
author: jcjyxjs
categories: 
  - 网站
tags: 
  - 腾讯云
  - 改字体
  - 跨域访问
  - CDN
banner: 
bannerascover: 1
bannerStyle: 0
excerpt: 改字体
posttype: 0
showfullcontent: 0
showTOC: 0
---


> 建议本文搭配 *[使用Fontmin生成WebFont压缩字体][1]* 食用更佳

今天看到主题作者主页大标题用了这个字体，我一想哇还挺好看，也想自己整一个，看了看主题设置并没有更改字体的设置，只有头部标签引用,又回头看了看原页面，注意到了这两行代码，翻遍了他所有的评论知道这个字体叫**方正粗金陵繁体**

> ![①][2]
> ![②][3]

于是我从方正官网下到了这个字体的ttf版本，并相应转成了***.eot***和***.woff***格式。
新建一个css，码入以下代码，因为针对`class`为`brand`的文字字体替换，所以直接定义

    @font-face {
        font-family: 'f';
        src: url('https://cdn.elstec.cn/font/f.eot?#iefix') format('eot');/*IE*/
        src: url('https://cdn.elstec.cn/font/f.woff') format('woff'), url('f.ttf') format('truetype');/*non-IE*/
        }
        
        div.brand {
            font-family: 'f';
        }
        
主题设置`head`**标签输出内容**

    <link rel="stylesheet" href="https://cdn.elstec.cn/zt.css" />
    <style>.brand{font-family:'f';font-weight:normal;}</style>

我直接把字体重命名为f，因为好打。刷新一看，字体没更新，看到不允许跨域访问。
![ ￣﹃￣ ][4]
解决方案如下:
在`nginx`配置文件中做如下配置  

    location ~ .*\.(eot|ttf|ttc|otf|eot|woff|woff2|svg)(.*) {
        add_header Access-Control-Allow-Origin http(s)://example.com; 
    }

在CDN进行`HTTP Header`配置，以腾讯云为例

> 在CDN设置中找到高级配置，添加`HTTP Header`，参数选择`Access-Control-Allow-Origin`，取值是你的域名完整格式，添加该配置等待CDN生效即可。


  [1]: https://elstec.cn/archives/fwbf/
  [2]: https://cdn.elstec.cn/font.png?imageMogr2/format/webp/interlace/1/quality/100
  [3]: https://cdn.elstec.cn/branda.png?imageMogr2/format/webp/interlace/1/quality/100
  [4]: https://cdn.elstec.cn/er1.png?imageMogr2/format/webp/interlace/1/quality/100