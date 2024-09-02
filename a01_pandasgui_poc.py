import pandas as pd
import pandasgui

fn = 'data\wf7333_activity_20230101_1231_2.csv'
df = pd.read_csv(fn)
pandasgui.show(df)
