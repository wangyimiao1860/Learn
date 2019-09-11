# 
import pandas  as pd
import pymysql

def getStore():
    coon = pymysql.connect(
         host = 'localhost',user = 'root',passwd = '11111111',
         port = 3306,db = 'ods',charset = 'utf8'
         #port必须写int类型
         #charset必须写utf8，不能写utf-8
     )
    cur = coon.cursor()  #建立游标
    cur.execute("select * from ods.o_fruit_list_d")  #查询数据
   res = cur.fetchall()    #获取结果
   print(res)
   #cur.close()     #关闭游标
   #coon.close()    #关闭连接
   
   #如果是插入数据，则要commit一下，把第9行换成以下两行
   #cur.execute('insert into stu(name,sex) VALUE ("pzp","man");')
   #coon.commit()


#def getStore():
#    # with open("web/store.txt", 'r') as f:
#    #     store = f.readlines()
#    # name = ["Apple","Banana","Tomato"]
#
#    # return {name[i]: int(store[i]) for i in range(len(name))}
#    store_df  = pd.read_csv("web/fruit.csv", index_col=0)
#    store = {store_df['fruit'].to_list()[i]:store_df.to_dict("records")[i]  for i in range(len(store_df))}
#    return store

def update_store(fruit, num):
    # with open("web/store.txt", 'r') as f:
    #     store = [int(x) for x in f.readlines()]
    #     print(store)
    # if fruit == "Apple":
    #     store[0] = int(store[0]) - int(num)
    # elif fruit == "Banana":
    #     store[1] = int(store[1]) - int(num)
    # elif fruit == "Tomato":
    #     store[2] = int(store[2]) - int(num)
    # with open("web/store.txt", 'w') as f:
    #     print(store)
    #     print("\n".join([str(x) for x in store]))
    #     f.writelines("\n".join([str(x) for x in store]))

    store_df  = pd.read_csv("web/fruit.csv", index_col=0)
    print(store_df.dtypes)
    row = store_df.query("fruit == 'Apple'")
    print(row.num.values[0])
    store_df.loc[row.index[0], 'num'] = row.num.values[0] - num
    store_df.to_csv("web/fruit.csv")

def add_buy_record():
    pass




# todo : 
        
