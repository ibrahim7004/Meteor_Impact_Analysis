import pandas as pd

def generate():
    df = pd.read_csv("D:/ds_proj/excel_files/predicted_dataset1.csv")

    cols = ["Radius","Volume","Density","Mass","Radiated Energy","Impact Energy"]
    df = df.sort_values(by=["Impact Energy"])
    diff = df["Impact Energy"].diff()

    # Select the 20 rows with the largest gaps between consecutive 'Impact Energy' values
    idx = diff.nlargest(20).index
    cols = ["Radius","Volume","Density","Mass","Radiated Energy","Impact Energy"]
    df_new = df.loc[idx, cols]

    # Round off all values in the DataFrame to 1 decimal point
    df_new = df_new.round(1)

    df_new.to_csv("D:/ds_proj/excel_files/output.csv", index=False)
    return df_new









