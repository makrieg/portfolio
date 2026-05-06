
from sklearn.datasets import fetch_california_housing
import pandas as pd

california = fetch_california_housing()

#print(california.DESCR)

print(california.data.shape)
print(california.target.shape)

pd.set_option("display.precision", 4)
pd.set_option("display.max_columns", 9)
pd.set_option("display.width", None)


cali_df = pd.DataFrame(california.data, columns=california.feature_names)

cali_df['MedHouseValue'] = pd.Series(california.target)

print(cali_df.head())

sample_df = cali_df.sample(frac=0.1, random_state=17)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=2)
sns.set_style("whitegrid")

for feature in california.feature_names:
    plt.figure(figsize=(8,4.5))
    sns.scatterplot(
        data=sample_df,
        x=feature,
        y='MedHouseValue',
        hue='MedHouseValue',
        palette="cool",
        legend=False
    )

    plt.show()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    california.data, california.target, random_state=11)

print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X=x_train, y=y_train)


for i, name in enumerate(california.feature_names):
    print(f"{name}: {lr.coef_[i]:.4f}")

predicted = lr.predict(X=x_test)
expected = y_test

df = pd.DataFrame()

df["expected"] = pd.Series(expected)
df["predicted"] = pd.Series(predicted)

import matplotlib.pyplot as plt2

figure = plt2.figure(figsize=(9, 9))

axes = sns.scatterplot(
    data=df,
    x="expected",
    y="predicted",
    hue="predicted",
    palette="cool",
    legend=False
)

start = min(df.expected.min(), df.predicted.min())
end = max(df.expected.max(), df.predicted.max())

axes.set_xlim(start, end)
axes.set_ylim(start, end)

line = plt2.plot([start, end], [start, end], "k--")
plt2.show()
