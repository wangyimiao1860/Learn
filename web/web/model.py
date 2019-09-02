# 
import pandas  as pd

def getStore():
    # with open("web/store.txt", 'r') as f:
    #     store = f.readlines()
    # name = ["Apple","Banana","Tomato"]

    # return {name[i]: int(store[i]) for i in range(len(name))}
    store_df  = pd.read_csv("web/fruit.csv", index_col=0)
    store = {store_df['fruit'].to_list()[i]:store_df.to_dict("records")[i]  for i in range(len(store_df))}
    return store

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
        
