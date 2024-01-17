import pandas as pd

Data = [{'Name': 'John', 'Age': 25, 'City': 'New York'},
        {'Name': 'trevor', 'Age': 30, 'City': 'San Francisco'},
        {'Name': 'jane', 'Age': 42, 'City': 'kenya'},
        {'Name': 'ryan', 'Age': 56, 'City': 'japan'},
        {'Name': 'bryan', 'Age': 12, 'City': 'nakuru'},
        {'Name': 'xavier', 'Age': 30, 'City': 'eastleigh'},
        {'Name': 'ken', 'Age': 22, 'City': 'mombasa'},
        {'Name': 'vox', 'Age': 45, 'City': 'kisumu'},
        ]


pd.DataFrame(Data)

data.to_csv("data/data.csv",index=False)