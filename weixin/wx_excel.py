import pymongo,logging,xlwt,pandas as pd,numpy as np,matplotlib.pyplot as plt,datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

conn = pymongo.MongoClient("localhost:27017")
db = conn["广东共青团"]

def read_mongodb_to_excel():
    workbook = xlwt.Workbook(encoding="utf-8")
    booksheet = workbook.add_sheet("Sheet 1".capitalize(), cell_overwrite_ok=True)
    collection_name = db.collection_names()[0]
    collection = db[collection_name]
    logger.info("公众号"+collection_name+"发布了"+str(collection.count())+"篇文章")
    datas = collection.find()
    keys = list(datas[0].keys())
    # print(keys)
    keys.pop(0)
    for i,key in enumerate(keys):
        booksheet.write(0,i,key)

    for i,data in enumerate(datas,start=1):
        data = list(data.values())
        data.pop(0)
        for j in range(len(data)):
            booksheet.write(i, j, data[j])
    # workbook.save("weixin_" + collection_name + ".xls")
    workbook.save("weixin_" + "广东共青团" + ".xls")


def read_excel_data():
    import time
    # ts = time.strptime("2018-06-10 15:37:54", "%Y-%m-%d %H:%M:%S")
    # now = time.mktime(ts)
    # year = now.strftime("%Y")
    year = datetime.datetime.strptime("2018-06-10 15:37:54","%Y-%m-%d %H:%M:%S").year
    print(year)
    import re


read_mongodb_to_excel()
# read_excel_data()