import pandas as pd
import json
import matplotlib.pyplot as mplt
import seaborn as sns
splt = mplt
# Загрузка из файла events.json
with open("events.json", "r") as file_events:
    data = json.load(file_events)
    # print(data)
    # Загружаем данные из раздела "events"
    df = pd.DataFrame(data["events"])
    # print(df)
    # Подсчитываем количество каждой из "signature"
    counts = df["signature"].value_counts()
    # Подготавливаем и отображаем график
    mplt.figure(figsize=(12, 8))
    counts.plot(kind='bar')
    print(counts)
    # print(counts.plot(kind='bar'))
    mplt.title("Event Signature Frequency")
    mplt.ylabel("Count")
    mplt.xlabel("Signature Name")
    mplt.xticks(rotation=45, ha="right")
    mplt.tight_layout()
    mplt.show()

    splt.figure(figsize=(18, 8))
    sns.countplot(data=df, y='signature', order=df['signature'].value_counts().index)
    splt.title("Event Signature Frequency")
    splt.ylabel("Signature Name")
    splt.xlabel("Count")
    splt.show()
