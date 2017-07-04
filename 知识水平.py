import time
import urllib
from urllib.request import urlopen
import ssl
context = ssl._create_unverified_context()

try:
    QUOTES_URL = "https://raw.githubusercontent.com/Calvin-Xu/Mogic/master/quotes_utf-8.txt"
    quotes = []

    for quote in urlopen(QUOTES_URL, context=context).readlines():
        quotes.append(str(quote.strip(), encoding="utf-8"))

    a = quotes

    translations = {item : a[index+1] for index, item in enumerate(a) if index % 2 == 0}

    print('-' * 10)
    time.sleep(1)
    print("Version 5.1\nCalvin Xu 制作")
    time.sleep(1)
    print("输入 /help 得到帮助")
    time.sleep(1)
    print('-' * 10)
    time.sleep(0.5)

    try:
        while True:
            req = input("输入: ")

            if req == "/help":
                print('-' * 10)
                print("""
                      Ver.1.0:
                      输入中文，得到长者英文语录翻译，提高知识水平
                      ( NFLS 洋文好的人多的很哪!)
                      输入 \"/语录\", 得到人生经验
                      输入\"/三篇\"阅读完整蛤三篇
                      按 e 可赛艇
                      更多资源请按 r

                      Ver.2.0: 加入模糊搜索功能

                      Ver.3.0:
                      加入外挂文档功能

                      Ver.4.0
                      加入完整三篇, excited!

                      Ver.5.0
                      所有文档存储于服务器端, 出了事我们跑得比谁都快
                      Ver.5.1
                      网络连接错误提示

                      Ver.6.0
                      完善模糊搜索功能，使用算法而非手动排除
                      Ver.6.1
                      模糊搜索 bug fix
                      """)
                print('-' * 10)
            else:
                pass


            if req == "/语录":
                print('-' * 10)
                print("长者 (前国家领导人江泽民) 语录 (中英对照):")
                for ori, trans in list(translations.items()):
                    print(f"{ori} <----> {trans}")
                    time.sleep(0.3)
                print('-' * 10)
            else:
                pass


            if req == "e":
                for i in range(1, 65):
                    print(f"excited\n+{i}s\n")
                    time.sleep(0.1)

                print('-' * 10)
                print("Made by NFLS - CX")
                print("Disclaimer: 翻译带强烈个人臆断")
                print("2017 届 1 班坠吼!")
                print("Stay young, stay simple")
                print("2017-6-26")
                print('-' * 10)
            else:
                pass


            if req == "r":
                print('-' * 10)
                print("长者 Wikipedia 词条: https://en.wikipedia.org/wiki/Jiang_Zemin")
                time.sleep(0.5)
                print("长者 Wikiquote 词条: https://zh.wikiquote.org/wiki/%E6%B1%9F%E6%B3%BD%E6%B0%91#.E8.A7.86.E5.AF.9F.E8.81.94.E5.B7.A5.E5.9B.BD.E6.9C.BA.E4.BA.8C.E9.99.A2")
                time.sleep(0.5)
                print("NFLS水上运动讨论群 ID: 527623612")
                print('-' * 10)
            else:
                pass


            if req == "/三篇":
                print("""
                      视察二院，请按 1
                      怒斥记者，请按 2
                      谈笑风生，请按 3
                      """)
                choice = input("输入: ")
                if choice == "1":
                    print("----------视察二院----------\n")
                    for quote in urlopen("https://raw.githubusercontent.com/Calvin-Xu/Mogic/master/quote1.txt", context=context).readlines():
                            print(str(quote, encoding="utf-8"))
                            time.sleep(0.5)

                elif choice == "2":
                    print("----------怒斥记者----------\n")
                    for quote in urlopen("https://raw.githubusercontent.com/Calvin-Xu/Mogic/master/quote2.txt", context=context).readlines():
                            print(str(quote, encoding="utf-8"))
                            time.sleep(1)

                elif choice == "3":
                    print("----------谈笑风生----------\n")
                    for quote in urlopen("https://raw.githubusercontent.com/Calvin-Xu/Mogic/master/quote3.txt", context=context).readlines():
                            print(str(quote, encoding="utf-8"))
                            time.sleep(0.1)

                else:
                    pass


            if req != "/help" and req != "/语录" and req != "e" and req != "r" and req != "/三篇":
                print('-' * 10)
                print(f"你输入了: \"{req}\"")
                result = translations.get(req)
                if result:
                    print("English: ")
                    print(result)
                elif "邓小平" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"邓小平的理论\"（原话如此）。")
                elif "欧盟" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"欧盟呢最近发表了一个报告\"（原话如此）。")
                elif "选举" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"选举的法\"（原话如此）。")
                elif "天堂" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"天堂的下面是你们的天堂\"（原话如此）。")
                elif "识得" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"识得唔识得啊\"（原话如此）。")
                elif "得罪" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"我今天得罪了你们一下\"（原话如此）。")
                elif "生气" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"我生气了！\"（原话如此）。")
                elif "经验" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"人生的经验\"（原话如此）。")
                elif "华莱士" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"美国的华莱士\"（原话如此）。")
                elif "批判" in req:
                    print(f"无 \"{req}\" 条目。请重新输入")
                    print("你可能找的是\"就把我批判一番\"（原话如此）。")

                else:
                    try:
                        pool = list(translations.keys())

                        element = list(req)

                        for seek in element:
                            indices = [i for i, s in enumerate(pool) if seek in s]
                            tar1 = int(indices[-1])
                            tar2 = int(indices[0])

                        print(f"无 \"{req}\" 条目。请重新输入")
                        print(f"""你可能找的是
\"{pool[tar1]}\" 或
\"{pool[tar2]}\"
(原话如此）。""")

                        print('-' * 10)
                    except IndexError:
                        print("模糊搜索无效，请重新输入，提供更多关键词。")
            else:
                pass
    except KeyboardInterrupt:
        print("\nBye\n")
except urllib.error.HTTPError as err:
   if err.code == 404:
       print("\nWarning: Page not found!\n")
       exit(0)
   elif err.code == 403:
       print("\nWarning: Access denied!\n")
       exit(0)
   else:
       print("\nWarning: Something happened! Error code", err.code)
       print(" ")
       exit(0)
except urllib.error.URLError as err:
    print("\nWarning: Some other error happened:", err.reason)
    print(" ")
    exit(0)
