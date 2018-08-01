INIT_HEADERS = '''
GET https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA3NTE5MzQzMA==&f=json&offset=11&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO%2FSiMSeadzPI%3D&wxtoken=&appmsg_token=968_BTl67wXPJHLBjbJU4Lp3Q_mCR1JZ5XdfKSHlvw~~&x5=1&f=json HTTP/1.1
Host: mp.weixin.qq.com
Connection: keep-alive
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 8.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060739) NetType/WIFI Language/zh_CN
Accept: */*
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA3NTE5MzQzMA==&scene=124&devicetype=android-26&version=26060739&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO%2FSiMSeadzPI%3D&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: pgv_info=ssid=s8958678400; pgv_pvid=9011907515; ts_uid=6708098099; tvfe_boss_uuid=f9f47dbb77347813; rewardsn=; wxtokenkey=777; wxuin=0; devicetype=android-26; version=26060739; lang=zh_CN; pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO/SiMSeadzPI=; wap_sid2=COq2kioSXFc4R0xwbnMwUXhPaDFlTUpCLUZEZE5WUHI0UG15M1NVdk82Um50S1hkajJ0Nm5MLUhDV1ZnbzhVSThpYVRFclY2bUpOV1dXYy1Rc3VHY0VIQ3ByZUZjZ0RBQUF+MPnrhtsFOA1AlU4=
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.7&TBSVC=43610&CO=BK&COVC=044033&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MI6 &RL=1080*1920&OS=8.0.0&API=26
Q-GUID: 608bfe6fe0080f54b9d6f9c013b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
                        '''

DATA_URL_PARAMS = """f=json&mock=&uin=777&key=777&pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO%25252FSiMSeadzPI%25253D&wxtoken=777&devicetype=android-26&clientversion=26060739&appmsg_token=968_OCXzXpY4M3pPXjGMOXqkd7_cj8I1udi9Qlzn0uLCovJnde25hCMqVaaI4Go~&x5=1&f=json """

BODY = 'r=0.001156536762126903&__biz=MzA3NTE5MzQzMA%3D%3D&appmsg_type=9&mid=2655011333&sn=73a8e14a5686e2c07d6be637ed136aa4&idx=2&scene=38&title=%25E2%2580%259C%25E6%2588%2598%25E5%258F%258B%25EF%25BC%258C%25E5%2588%25AB%25E5%25BF%2598%25E6%25B6%2582%25E6%258A%25B9%25E9%2598%25B2%25E6%2599%2592%25E9%259C%259C%25EF%25BC%2581%25E2%2580%259D&ct=1532990518&abtest_cookie=AgABAAoACwACACWXHgA7mR4AAAA%3D&devicetype=android-26&version=26060739&is_need_ticket=0&is_need_ad=1&comment_id=392557454476591104&is_need_reward=0&both_ad=0&reward_uin_count=0&send_time=&msg_daily_idx=1&is_original=0&is_only_read=1&req_id=0121YBve5uV3qB3eiUprdDVC&pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO%25252FSiMSeadzPI%25253D&is_temp_url=0&item_show_type=undefined&tmp_version=1'

MESSAGE_HEADERS = '''  
Host: mp.weixin.qq.com
Connection: keep-alive
Content-Length: 745
Origin: https://mp.weixin.qq.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 8.0; MI 6 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060739) NetType/WIFI Language/zh_CN
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
Referer: https://mp.weixin.qq.com/s?__biz=MzA3NTE5MzQzMA==&mid=2655011333&idx=2&sn=73a8e14a5686e2c07d6be637ed136aa4&chksm=84c0af3cb3b7262a553593eb7429466108ac89f4678bb179a37e8161739ccafc7fcb5b416e6a&scene=38&ascene=0&devicetype=android-26&version=26060739&nettype=WIFI&abtest_cookie=AgABAAoACwACACWXHgA7mR4AAAA%3D&lang=zh_CN&pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO%2FSiMSeadzPI%3D&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: pgv_info=ssid=s8958678400; pgv_pvid=9011907515; ts_uid=6708098099; tvfe_boss_uuid=f9f47dbb77347813; rewardsn=; wxtokenkey=777; wxuin=0; devicetype=android-26; version=26060739; lang=zh_CN; pass_ticket=LGth1xNeWdpgxHksnTPY1F0tcPlqtRyO/SiMSeadzPI=; wap_sid2=COq2kioSXFc4R0xwbnMwUXhPaDFlTUpCLUZEZE1HQXJPT1d0Z1cxM05QcDMxOW1GelE4bndUR1NITUVyLXQ5eTN3OV9jS2ZHNWpCQTYtU0tScFRUM0VnVWZjck5zZ0RBQUF+MMjshtsFOA1AAQ==
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.7&TBSVC=43610&CO=BK&COVC=044033&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MI6 &RL=1080*1920&OS=8.0.0&API=26
Q-GUID: 608bfe6fe0080f54b9d6f9c013b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
                '''