import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

if __name__ == "__main__":
    irysy = pd.read_csv("dane/iris.data", names=["sep length", "sep width", "pet length", "pet width", "class"])
    #  print(irysy.mean())
    #  print(irysy.std())
    # print(irysy.median())
    # print(irysy.min())
    # print(irysy.max())
    # print(irysy.groupby("class").size())
    # licz = irysy.groupby("class").size()
    # print(licz*100/licz.sum())
    # print(irysy.corr())
    sea.distplot(irysy["pet length"], bins=20, kde=False)
    plt.show()




#with open ("dane/iris.data", "r") as irysy:
