import pandas as pd

#%%
# read the file to a dataframe
FILE = 'scores.csv'
scores = pd.read_csv(FILE, delimiter=',', index_col=0, header=0)

#%%
def assign_point(score):
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0

#%%
means = scores.mean()
points = means.transform(assign_point)
print(points)
points.mean()
# %%